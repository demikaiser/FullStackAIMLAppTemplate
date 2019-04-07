from flask import Flask
from flask_cors import CORS


import aiml

app = Flask(__name__)
CORS(app)  # CORS is needed for Cross Origin Resource Sharing.


@app.route('/', methods=['GET'])
def get_results():
    return aiml.run()


if __name__ == '__main__':
    app.run(debug=True)




