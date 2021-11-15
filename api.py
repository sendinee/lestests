import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>API</h1>
<p>API test</p>'''



@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Erreur: Pas de Id. S'il vous plaît votre Id"
    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)

app.run()

#http://127.0.0.1:5000/api/v1/resources/books?id=0
#http://127.0.0.1:5000/api/v1/resources/books?id=1
#http://127.0.0.1:5000/api/v1/resources/books?id=2
#http://127.0.0.1:5000/api/v1/resources/books?id=3
