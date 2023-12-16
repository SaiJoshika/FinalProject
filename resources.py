from flask_restful import Resource, reqparse
from utils.data_utils import read_data, write_data

class ListingResource(Resource):
    def get(self, listing_id=None):
        # Implement GET endpoints
        pass

    def post(self):
        # Implement POST endpoint
        pass

    def patch(self, listing_id):
        # Implement PATCH endpoint
        pass

    def delete(self, listing_id):
        # Implement DELETE endpoint
        pass

class SearchResource(Resource):
    def post(self):
        # Implement search endpoint
        pass
