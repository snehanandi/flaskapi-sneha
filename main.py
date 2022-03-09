from flask import Flask , jsonify
from flask_restful import Resource , Api
from flask_cors import CORS

app=Flask(__name__)
api=Api(app)
CORS(app)

class Status (Resource):
    def get(self):
        try:
            return {'data': 'Api is running'}
        except:
            return {'data': 'an error occured during fetching API'}

class Sum(Resource):
    def get(self, a,b):
        return jsonify({'data': a+b})

api.add_resource(Status,'/')
api.add_resource(Sum,'/add/<int:a>,<int:b>')

if __name__=='__main__':
    app.run()
    


        