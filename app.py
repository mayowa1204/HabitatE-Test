from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class Aunctions(Resource):
    async def get(self):
     
        return{"data":"Hello There"}

api.add_resource(Aunctions, "/aunctions")

if __name__ == "__main__":
    app.run(debug=True)