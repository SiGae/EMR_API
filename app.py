from flask import Flask, request
import database

from Controller import c_info, c_concept, c_search

app = Flask(__name__)


@app.get('/info/<target>')
def get_info(target):
    methodToCall = getattr(c_info, 'get_' + target)
    response_data = methodToCall(database.Session())
    return response_data


@app.get('/concept')
def get_concept():
    parameter_dict = request.args.to_dict()
    method_to_call = getattr(c_concept, 'get_concept')
    response_data = method_to_call(database.Session(), parameter_dict)
    return response_data


@app.get('/search/<target>')
def get_search(target):
    parameter_dict = request.args.to_dict()
    method_to_call = getattr(c_search, 'get_' + target)
    response_data = method_to_call(parameter_dict, database.Session())
    return response_data


if __name__ == '__main__':
    app.run(debug=True)

