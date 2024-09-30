# **Apostas de Corrida API**

## **Descrição**

Este projeto implementa uma API de apostas para corridas, permitindo que os usuários apostem em diferentes eventos de uma corrida, como:

- Aposta no pódio (1º, 2º e 3º lugares)
- Aposta na posição final de um piloto
- Aposta no piloto que fará o pitstop mais rápido
- Aposta no piloto que fará a volta mais rápida

O saldo do usuário é atualizado com base nos resultados das apostas, e o sistema mantém um saldo inicial de 100 moedas.

## **Funcionalidades**

- **Apostas no pódio completo**: Aposte nos três primeiros lugares. Dependendo da precisão, o usuário ganha recompensas em moedas:
  - 1 acerto: +30 moedas
  - 2 acertos: +70 moedas
  - 3 acertos: +200 moedas
- **Apostas na posição final**: Aposte na posição final de um piloto específico.
- **Aposta no pitstop mais rápido**: Escolha o piloto que você acredita que terá o pitstop mais rápido.
- **Aposta na volta mais rápida**: Aposta no piloto que você acha que fará a volta mais rápida.

## **Rotas da API**

### **POST /apostar/posicao**
Aposta na posição final de um piloto.

**Exemplo de corpo da requisição:**
