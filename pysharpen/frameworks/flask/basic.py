from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_from_flask():
    hello = {"message": "Hello from Flask!"}
    return json.dumps(hello)

if __name__ == "__main__":
    app.run(port=8080)
