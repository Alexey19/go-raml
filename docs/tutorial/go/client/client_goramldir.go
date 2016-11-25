package main

import (
	"net/http"
)

const (
	defaultBaseURI = "http://localhost:5000"
)

type goramldir struct {
	client     http.Client
	AuthHeader string // Authorization header, will be sent on each request if not empty
	BaseURI    string
	common     service // Reuse a single struct instead of allocating one for each service on the heap.

	Users *UsersService
}

type service struct {
	client *goramldir
}

func Newgoramldir() *goramldir {
	c := &goramldir{
		BaseURI: defaultBaseURI,
		client:  http.Client{},
	}
	c.common.client = c

	c.Users = (*UsersService)(&c.common)

	return c
}
