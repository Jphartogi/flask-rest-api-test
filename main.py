from flask import Flask,jsonify,request
import os
app = Flask(__name__)

# Environment variable
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv("URL_HOST")
PORT = int(os.getenv("PORT"))
@app.route('/',methods = ['POST', 'GET'])
def check_for_update():
    return jsonify(message="Hello World!")

if __name__ == '__main__':
	app.run(host=HOST, port=PORT)
