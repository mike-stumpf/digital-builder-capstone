from flask import request
from flask_restx import Namespace, reqparse, Resource
from modules.data import *
from modules.util import *

api = Namespace('data', description='Data related operations', validate=True)

parser = reqparse.RequestParser()
parser.add_argument(
    ingest_arg_filename,
	required=True,
    help='The filename to be ingested',
	trim=True
)
parser.add_argument(
    ingest_arg_type,
	required=True,
    choices=(zillow_data_type_condo, zillow_data_type_sfr),
    help='The type of data being uploaded',
	default=zillow_data_type_condo
)

@api.route('/ingest')
class DataClass(Resource):
	@api.expect(parser)
	def post(self):
		args = parser.parse_args()
		raw_data = ingest_zillow_csv(args[ingest_arg_filename])
		filtered_data = filter_normalise_zillow_data(raw_data, args[ingest_arg_type])
		# todo, store results in db
		return filtered_data





#https://www.codementor.io/@sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
#https://stackoverflow.com/questions/7907596/json-dumps-vs-flask-jsonify