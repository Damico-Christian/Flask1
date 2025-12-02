from flask import Flask, jsonify, request
from flask_cors import CORS
from database_wrapper import DatabaseWrapper

app = Flask(__name__)
CORS(app)

#credenziali del db Aiven
db = DatabaseWrapper(
    host="mysql-1197a299-iisgalvanimi-2ff7.g.aivencloud.com",
    user="avnadmin",
    password="AVNS_EkGkeBVLvXC726rqo8_",
    database="defaultdb",
    port=22433  
)


#restituisce tutta la lista
@app.route("/spesa", methods=["GET"])
def get_spesa():
    lista = db.get_lista_spesa()
    return jsonify(lista)

#aggiunge un elemento
@app.route("/spesa", methods=["POST"])
def aggiungi_spesa():
    dati = request.json           #prende il JSON inviato da Angular
    elemento = dati["elemento"]   #lo mettiamo in una variabile
    db.aggiungi_elemento(elemento)
    return jsonify({"msg": "Aggiunto"})
    
if __name__ == '__main__':
    app.run(debug=True)