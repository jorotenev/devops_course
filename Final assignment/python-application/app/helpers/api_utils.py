import json

from flask import Response


def make_json_response(json_str, status_code=200, mimetype='application/json'):
    if isinstance(json_str, (dict, list)):
        json_str = json.dumps(json_str)
    if not isinstance(json_str, str):
        raise ValueError("only strings, dicts and lists are accepted")

    return Response(json_str, status=status_code, mimetype=mimetype)


