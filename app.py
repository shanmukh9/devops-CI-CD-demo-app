from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Everyone! Thank you for joining"

# run the app.
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
