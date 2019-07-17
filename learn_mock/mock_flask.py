from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)

tasks = {
    "data": {
        "name": "test",
        "age": "25"
    },
    "code": 10000,
    "message": "成功"
}


@app.route("/task", methods=['GET'])
def get_all_task():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8989,
        debug=True
        )
