from flask import flask

app = Flask(__name__)

playlist = [
    {"id": 1, "titulo": "Bohemian Rhapsody", "artista": "Queen"}
    {"id": 2, "titulo": "Shape of You", "artista": "Ed Sheeran"}
]

@app.route('musicas', methods=['GET'])
def get_musicas():
    return jsonify({"playlist": playlist, "total": len(playlist)})

@app.route('/musicas', methods=['POST'])
def add_musica():
    nova_musica = request.json

    nova_musica["id"] = len(playlist) + 1

    playlist.append(nova_musica)
    return jsonify({"mensagem": "Música cadastrada com sucesso!", "musica": nova_musica}), 201

if __name__ == '__main__':
    app.run(debug=True)