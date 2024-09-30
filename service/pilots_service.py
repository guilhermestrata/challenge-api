from database.data import nomePilotos, sobrenomePilotos, equipesPilotos

def show_pilots():
    pilotos = []
    for i in range(len(nomePilotos)):
        piloto = {
            'nome': nomePilotos[i],
            'sobrenome': sobrenomePilotos[i],
            'equipe': equipesPilotos[i]
        }
        pilotos.append(piloto)
    return pilotos
