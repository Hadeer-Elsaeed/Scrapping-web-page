from flask_restful import Resource
from controllers.get_api_controller import GetController
from controllers.post_api_controller import PostController
from controllers.put_api_controller import PutController
from controllers.delete_api_controller import DeleteController

class RestExcel(Resource):
    def __init__(self):
        self.get_controller = GetController()
        self.post_controller = PostController()
        self.put_controller = PutController()
        self.delete_controller = DeleteController()

    def get(self):
        return self.get_controller.handle_request()

    def post(self):
        return self.post_controller.handle_request()

    def put(self):
       return self.put_controller.handle_request()

    def delete(self):
        return self.delete_controller.handle_request()
