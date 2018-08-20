from flask_restful import Resource
from flask import request

class PhoneBookResource(Resource):
    def get(self):
        """
        Get all contacts

        params: self

        returns: {"message": "success", [{"georgreen": 254709845454}]}
        """
        user_name = request.args.get('user_name')

        if not user_name.isalnum():
            return {"message": "Bad data"}, 400

        return {"message": "hello from phone book"}, 200
