from flask_restful import Resource

class PhoneBookResource(Resource):
    def get(self):
        return {"message": "hello from phone book"}
