import database.data as data

def show_pilots():
    pilotos = []
    for i in range(len(data.sobrenomePilotos)):
        piloto = f'{data.nomePilotos[i]} {data.sobrenomePilotos[i]}'
        pilotos.append(piloto)
    return pilotos
