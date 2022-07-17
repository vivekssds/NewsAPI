from flask import Flask,jsonify,request
from Processor import controller
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/news/<int:N>', methods=['GET'])
def topnews(N):
    if controller.commoncontroller.validate(N):
        result=controller.commoncontroller.processrequest(N)
        return result
    else:
        return "Not a Valid Request"


@app.route('/cleancache/', methods=['GET'])
def cleancache():
    response=controller.commoncontroller.processredisrequest(app,0)
    return response


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=os.environ.get('DEBUG')=='1')