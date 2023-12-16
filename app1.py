from flask import Flask
from flask_restful import Api
from resources import ListingResource, SearchResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ListingResource, '/listings', '/listings/<int:listing_id>')
api.add_resource(SearchResource, '/listing/search')
