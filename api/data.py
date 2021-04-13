from flask import make_response
from flask_restx import inputs, Namespace, reqparse, Resource
from modules.data import *

api = Namespace('data', description='Data related operations', validate=True)

base_parser = reqparse.RequestParser()
base_parser.add_argument(
    arg_baseline_raw_data,
    type=inputs.boolean,
    required=True,
    default=False,
    help='Return raw data instead of formatted output'
)
base_parser.add_argument(
    arg_baseline_amfam_only,
    type=inputs.boolean,
    required=True,
    default=True,
    help='Return data for AmFam operating states only'
)
base_parser.add_argument(
    arg_housing_type,
    required=True,
    choices=(zillow_data_type_condo, zillow_data_type_sfr),
    help='Housing type to analyse',
    default=zillow_data_type_condo
)


@api.route('/baseline')
class BaselineClass(Resource):
    @api.expect(base_parser)
    def get(self):
        headers = {'Content-Type': 'text/csv'}
        args = base_parser.parse_args()
        amfam_data_only = args[arg_baseline_amfam_only]
        raw_data = args[arg_baseline_raw_data]
        housing_type = args[arg_housing_type]
        data = get_baseline_data(amfam_data_only, housing_type, raw_data)
        return make_response(data.head(25).to_csv(), 200, headers)


@api.route('/leaders')
class ForecastClass(Resource):
    @api.expect(base_parser)
    def get(self):
        headers = {'Content-Type': 'text/csv'}
        args = base_parser.parse_args()
        amfam_data_only = args[arg_baseline_amfam_only]
        raw_data = args[arg_baseline_raw_data]
        housing_type = args[arg_housing_type]
        data = get_leaders_data(amfam_data_only, housing_type, raw_data)
        return make_response(data, 200, headers)
