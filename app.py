import os.path
from typing import Optional

from flask import Flask, request, jsonify, Response

from constans import DATA_DIR
from utils import dict_of_utils

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    try:
        file_name: Optional[str] = request.args['file_name']
        cmd1: str = request.args['cmd1']
        value1: Optional[str] = request.args['value1']
        cmd2: Optional[str] = request.args['cmd2']
        value2: Optional[str] = request.args['value2']
    except KeyError:
        return Response({'error': 'Ужасные данные'}, 400)

    path: str = f'{DATA_DIR}\\{file_name}'

    if not os.path.exists(path):
        return Response('Файл не найден', status=400)

    with open(path) as file:
        data: list[str] = file.readlines()

    first_func = dict_of_utils[cmd1]
    first_res: Optional[list[str]] = first_func(param=value1, data=data)
    if cmd2 is not None:
        second_func = dict_of_utils[cmd2]
        second_res: Optional[list[str]] = second_func(param=value2, data=first_res)
        return jsonify(second_res)
    else:
        return jsonify(first_res)


if __name__ == '__main__':
    app.run()
