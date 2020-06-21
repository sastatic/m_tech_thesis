from flask import Flask
from flask_cors import CORS
import server_set_up.controller as controller
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def process_image():
    response = controller.main(os.path.join(os.getcwd(), 'resources'))
    return response


if __name__ == "__main__":
    print("app start")
    app.run(debug=True)
