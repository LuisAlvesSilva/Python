"""# Faca um jogo de pedra papel e tesoura, onde o jogador e o computador escolhem entre 0-pedra 1-Papel 2-Tesoura 
# (a jogado do computador eh aleatoria). 
# Jogo da pedra, tesoura e papel

import random

perguntar = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))
computador = random.randint(0,2)

if computador == 0:
    print('O computador escolheu: Pedra')
    if perguntar == 0:
        print("Empate!")
    elif perguntar == 1:
        print("Jogador perdeu")
    elif perguntar == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    print('O computador escolheu: Papel')
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate!")
    elif perguntar == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    print('O computador escolheu: Tesoura')
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")"""

##Usando o Streamlit


import streamlit as st
import random

class JogoPedraPapelTesoura:
    def __init__(self):
        self.opcoes = ["Pedra", "Papel", "Tesoura"]
        self.resultados = [
            ["Empate!", "Jogador perdeu", "Jogador venceu"],
            ["Jogador venceu", "Empate!", "Computador venceu"],
            ["Computador venceu", "Jogador venceu", "Empate!"]
        ]

    def jogar(self, escolha):
        computador = random.randint(0, 2)
        resultado = self.resultados[escolha][computador]
        return self.opcoes[escolha], self.opcoes[computador], resultado

def main():
    st.title("Jogo de Pedra, Papel e Tesoura")
    jogo = JogoPedraPapelTesoura()
    escolha = st.radio("Escolha uma opção para jogar:", jogo.opcoes)

    if st.button("Jogar"):
        escolha_index = jogo.opcoes.index(escolha)
        jogador, computador, resultado = jogo.jogar(escolha_index)
        st.write(f"Jogador: {jogador}")
        st.write(f"Computador: {computador}")
        st.write(resultado)

if __name__ == "__main__":
    main()
