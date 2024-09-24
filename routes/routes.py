from flask import Flask, jsonify
import jose
import datetime
from database.data import sobrenomePilotos
from service.pilotsService import show_pilots

app = Flask(__name__)

@app.route('/check', methods=['GET'])
def health_check():
    return 'Running'

@app.route('/pilots', methods=['GET'])
def get_pilotos():
    pilotos = show_pilots()
    return jsonify(pilotos)




if __name__ == '__main__':
    app.run(debug=True)
