#!/usr/bin/env python3

import mariadb

from flask import Flask, jsonify


app = Flask(__name__)
app.config.from_json('config.json')

config = {
    'port': 3306,
    'user': 'awendelk',
    'host': app.config['MARIADB_HOST'],
    'password': app.config['MARIADB_PASSSWORD'],
    'database': 'demo'
}


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/api/user', methods=['GET'])
def index():
    # connection for MariaDB
    conn = mariadb.connect(**config)

    # create a connection cursor
    cur = conn.cursor()

    # execute a SQL statement
    cur.execute('select * from user')

    # serialize results into JSON
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []

    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
