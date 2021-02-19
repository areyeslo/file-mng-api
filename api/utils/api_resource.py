from flask import request, jsonify
from urllib.parse import unquote_plus


def get_query_param_str(param):
    param_value = request.args.get(param)
    return unquote_plus(param_value).strip() if param_value and isinstance(param_value, str) else None
