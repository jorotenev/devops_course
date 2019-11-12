from . import api
from app.helpers.api_utils import make_json_response


@api.route('/api_ping')
def ping():
    return make_json_response({"result": "pong"})


