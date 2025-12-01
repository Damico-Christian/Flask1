from flask import Flask, jsonify # type: ignore
from flask_cors import CORS  # type: ignore
app = Flask(__name__)
CORS(app) #abilita CORS per TUTTE le route
@app.route("/profilo")
def profilo():
    return jsonify({
    "nome": "Christian",
    "professione": "Studente",
    "status": "swag"
})
if __name__ == "__main__":
    app.run(debug=True, port=5000)