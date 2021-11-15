from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>API</h1>
<p>API test</p>'''
