from flask import Flask, request, jsonify
from service.bet_service import (apostar_posicao_final, apostar_podio, apostar_pit_stop, apostar_volta_rapida)
from database.data import nomePilotos


app = Flask(__name__)

@app.route('/apostar/posicao', methods=['POST'])
def aposta_posicao():
    data = request.get_json()
    piloto = data.get('piloto')
    posicao = data.get('posicao')
    moedas = data.get('moedas')
    
    if piloto not in nomePilotos:
        return jsonify({'mensagem': 'Piloto não encontrado.'}), 400
    
    mensagem, novo_saldo = apostar_posicao_final(piloto, posicao, moedas)
    return jsonify({'mensagem': mensagem, 'saldo': novo_saldo})

@app.route('/apostar/podio', methods=['POST'])
def aposta_podio():
    data = request.get_json()
    pilotos = data.get('pilotos')
    moedas = data.get('moedas')
    
    for piloto in pilotos:
        if piloto not in nomePilotos:
            return jsonify({'mensagem': f'Piloto {piloto} não encontrado.'}), 400
            
    podio, acertos, novo_saldo = apostar_podio(pilotos, moedas)
    return jsonify({'podio': podio, 'acertos': acertos, 'saldo': novo_saldo})

@app.route('/apostar/pitstop', methods=['POST'])
def aposta_pitstop():
    data = request.get_json()
    piloto = data.get('piloto')
    moedas = data.get('moedas')
    
    if piloto not in nomePilotos:
        return jsonify({'mensagem': 'Piloto não encontrado.'}), 400
    
    vencedor, novo_saldo = apostar_pit_stop(piloto, moedas)
    return jsonify({'vencedor': vencedor, 'saldo': novo_saldo})

@app.route('/apostar/volta-rapida', methods=['POST'])
def aposta_volta_rapida():
    data = request.get_json()
    piloto = data.get('piloto')
    moedas = data.get('moedas')
    
    if piloto not in nomePilotos:
        return jsonify({'mensagem': 'Piloto não encontrado.'}), 400
    
    vencedor, novo_saldo = apostar_volta_rapida(piloto, moedas)
    return jsonify({'vencedor': vencedor, 'saldo': novo_saldo})

@app.route('/check', methods=['GET'])
def health_check():
    return 'Running'

if __name__ == '__main__':
    app.run(debug=True)