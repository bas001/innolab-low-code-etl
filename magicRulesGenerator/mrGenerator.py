from flask import Flask, Response, request
import parser
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.post("/convert")
@cross_origin()
def hello_world():
    decode = request.data.decode('utf-8')
    print(decode)
    response = Response(parser.generate(decode), mimetype='text/plain')
    return response
