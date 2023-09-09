# A simple web app that demonstrates GET and POST API functionality

from flask import Flask, request, jsonify

# Create the App

app = Flask(__name__)
@app.route("/")
def hello():
    """
    A simple home page display of hello.
    :return:
    """
    return "This is the home page of the App."

@app.route("/get-user/<user_id>")
def get_user(user_id):
    """
    A very basic GET API that can take in some query parameters.
    :param user_id: The user ID for which we return information.
    :return:
    """
    user_data = {
        "user_id" : user_id
    }

    extra = request.args.get("extra")
    if extra:
        user_data["how_is_meera"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    """
    Sends request data back to the requester as a response.
    """
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)