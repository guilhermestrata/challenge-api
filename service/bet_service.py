import random
from database.data import nomePilotos, sobrenomePilotos

saldo = 100

def apostar_posicao_final(piloto, posicao, moedas):
    global saldo 
    posicao_final = random.randint(1, len(nomePilotos))
    if posicao == posicao_final:
        saldo += moedas * 1.5 
        return f'Você ganhou! O piloto {piloto} terminou em {posicao_final}.', saldo
    else:
        saldo -= moedas  
        return f'Você perdeu! O piloto {piloto} terminou em {posicao_final}.', saldo


def apostar_podio(pilotos, moedas):
    global saldo 

    podio_real = random.sample(nomePilotos, 3)

    acertos = sum(1 for piloto in pilotos if piloto in podio_real)

    if acertos == 3:
        premio = 200
    elif acertos == 2:
        premio = 70
    elif acertos == 1:
        premio = 30
    else:
        premio = -100

    novo_saldo = saldo + premio  

    saldo = novo_saldo

    return podio_real, acertos, novo_saldo


def apostar_pit_stop(piloto, moedas):
    global saldo  
    vencedor = random.choice(nomePilotos)
    if piloto == vencedor:
        saldo += moedas * 2
        return vencedor, saldo
    else:
        saldo -= moedas
        return vencedor, saldo


def apostar_volta_rapida(piloto, moedas):
    global saldo 
    vencedor = random.choice(nomePilotos)
    if piloto == vencedor:
        saldo += moedas * 2
        return vencedor, saldo
    else:
        saldo -= moedas
        return vencedor, saldo

