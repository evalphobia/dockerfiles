"""Server app for DataRobot Prime prediction."""
# -*- coding: utf-8 -*-

from bottle import get, post, run, request, response, error, BaseRequest
import json
import os
import pandas
import prime3 as prime  # DataRobot Prime module


@get('/status')
def get_status():
    """Return 200 reponse."""
    response.content_type = 'application/json'
    return json.dumps({'status': 'ok', 'error': None, 'code': 200})


@post('/predict')
def post_predict():
    """Run DataRobot Prime.

    @json {Object} - must include all of the columns for prediction
    """
    return _run_predict()


@post('/predict/<key>')
def post_predict_key(key='id'):
    """Run DataRobot Prime with key.

    @json {Object} - must include all of the columns for prediction
    """
    return _run_predict(key)


def _run_predict(key='id'):
    """Run DataRobot prime by POST method.

    @json {Object} - must include all of the columns for prediction
    """
    params = _to_list(request.json)
    ds = pandas.DataFrame.from_dict(params)
    ds = prime.rename_columns(ds)
    ds = prime.convert_bool(ds)
    prime.validate_columns(ds.columns)
    ds = prime.parse_numeric_types(ds)
    ds = prime.add_missing_indicators(ds)
    ds = prime.impute_values(ds)
    ds = prime.combine_small_levels(ds)
    predicts = prime.predict_dataframe(ds)

    if key in params[0]:
        result = [{key: params[i][key], 'predict': predicts[i]} for i in range(predicts.size)]
        return {'error': None, 'code': 200, 'data': result}
    else:
        return {'error': None, 'code': 200, 'predicts': predicts.tolist()}


def _to_list(val):
    """Return the variable converted to list type."""
    if isinstance(val, list):
        return val
    else:
        return [val]


@error(404)
def error404(e):
    """Return 404 error message."""
    response.content_type = 'application/json'
    return json.dumps({'status': 'Not Found', 'error': str(e.exception), 'code': 404})


@error(500)
def error500(e):
    """Return 500 error message."""
    response.content_type = 'application/json'
    result = {'status': 'Internal Server Error', 'error': str(e.exception), 'code': 500}
    return json.dumps(result)


if __name__ == '__main__':
    KB = 1024
    MB = KB * KB
    BaseRequest.MEMFILE_MAX = 2 * MB

    port = 8080
    if "DR_SERVER_PORT" in os.environ:
        port = os.environ["DR_SERVER_PORT"]
    run(host='0.0.0.0', port=port)
