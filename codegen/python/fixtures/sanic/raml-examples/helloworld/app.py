# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from sanic import Sanic
from sanic.response import json

try:
    from helloworld_if import helloworld_if

except ImportError:
    from .helloworld_if import helloworld_if


import os
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Sanic(__name__)

app.blueprint(helloworld_if)


app.static('/apidocs', dir_path + '/apidocs')
app.static('/', dir_path + '/index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000, workers=2)
