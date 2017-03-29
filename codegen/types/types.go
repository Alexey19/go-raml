package types

import (
	"encoding/json"

	"github.com/Jumpscale/go-raml/codegen/commons"
	"github.com/Jumpscale/go-raml/raml"
)

type TypeInBody struct {
	Properties map[string]interface{}
	Endpoint   *Endpoint
	ReqResp    int
	RespCode   raml.HTTPCode
}
type TypeTask struct {
	Type interface{}
	Name string
	Pkg  string
}

func AllTypes(apiDef *raml.APIDefinition, pkgName string) map[string]TypeTask {
	mtt := map[string]TypeTask{}

	// from types
	for name, tip := range apiDef.Types {
		mtt[name] = TypeTask{
			Type: tip,
			Pkg:  pkgName,
			Name: name,
		}
	}
	for _, endpoints := range getAllEndpoints(apiDef) {
		for _, ep := range endpoints {
			tts := getTypesOfEndpoint(ep, pkgName)
			for _, tt := range tts {
				mtt[tt.Name] = tt
			}
		}
	}
	return mtt
}

func getTypesOfEndpoint(ep Endpoint, pkg string) []TypeTask {
	tts := []TypeTask{}

	tts = append(tts, getTypesOfBody(ep, &ep.Method.Bodies, pkg, HTTPRequest, "0")...)

	for respCode, resp := range ep.Method.Responses {
		tts = append(tts, getTypesOfBody(ep, &resp.Bodies, pkg, HTTPResponse, respCode)...)
	}
	return tts
}
func getTypesOfBody(ep Endpoint, body *raml.Bodies, pkg string,
	reqRespType int, respCode raml.HTTPCode) []TypeTask {
	tts := []TypeTask{}

	// for type defined in body.ApplicationJSON.Type
	if body != nil && body.ApplicationJSON != nil {
		tip := body.ApplicationJSON.TypeString()
		if singleLineNewType(tip) {
			tt := TypeTask{
				Type: tip,
				Pkg:  pkg,
				Name: tip,
			}
			tts = append(tts, tt)
		}
	}

	// for type defined in method body.ApplicationJSON.Properties
	if !commons.HasJSONBody(body) {
		return tts
	}

	tib := TypeInBody{
		Properties: getBodyProperties(body),
		Endpoint:   &ep,
		ReqResp:    reqRespType,
		RespCode:   respCode,
	}
	tt := TypeTask{
		Pkg:  pkg,
		Type: tib,
		Name: tib.Endpoint.Addr + ":" + tib.Endpoint.Verb + ":body",
	}
	tts = append(tts, tt)
	return tts
}

// get properties of a body
// TODO : move it to 'raml' package
func getBodyProperties(body *raml.Bodies) map[string]interface{} {
	if body.ApplicationJSON.TypeString() == "" {
		return body.ApplicationJSON.Properties
	}

	var js raml.JSONSchema
	if err := json.Unmarshal([]byte(body.ApplicationJSON.TypeString()), &js); err != nil {
		panic("failed to unmarshal json schema:" + body.ApplicationJSON.TypeString())
	}
	return js.RAMLProperties()

}

// single line type definition that need to be
// defined as a new type
func singleLineNewType(tip string) bool {
	if _, isMultiple := commons.MultipleInheritance(tip); isMultiple {
		return true
	}
	if commons.IsUnion(tip) {
		return true
	}
	return false
}
