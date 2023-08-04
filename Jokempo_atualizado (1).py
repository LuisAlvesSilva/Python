import random
import streamlit as st


class Jogo:
    def __init__(self):
        self.opcoes = ["Pedra", "Papel", "Tesoura", "Ataque Aéreo"]
        self.resultados = [
            ["Empate!", "Você Perdeu", "Você Ganhou", "Você Ganhou"],  # Resultados para "Pedra"
            ["Você Ganhou", "Empate!", "Joye Ganhou", "Você Ganhou"],  # Resultados para "Papel"
            ["Joye Ganhou", "Você Ganhou", "Empate!", "Você Ganhou"],  # Resultados para "Tesoura"
            ["Você Perdeu", "Você Perdeu", "Você Perdeu", "Empate!"]  # Resultados para "Ataque Aéreo"
        ]

    def jogar(self, escolher):
        computador = random.randint(0, 2)  # Gera um número aleatório para a escolha do computador
        if escolher == 3:  # Se o jogador escolher "Ataque Aéreo"
            resultado = "Você Ganhou"
            st.video("https://www.youtube.com/watch?v=5CkX3NvVNTc&ab_channel=bows")  # Exibe o vídeo
        else:
            resultado = self.resultados[escolher][computador]  # Obtém o resultado com base nas escolhas do jogador e do computador
        return self.opcoes[escolher], self.opcoes[computador], resultado  # Retorna as escolhas e o resultado


def main():
    st.title("Jogo do Pedra, Papel, Tesoura ou Ataque Aéreo")
    jogo = Jogo()  # Instancia um objeto da classe Jogo
    escolher = st.radio("Escolha uma opção para jogar", jogo.opcoes)  # Cria uma opção de escolha para o jogador

    if st.button("Jogar"):  # Se o botão "Jogar" for pressionado
        escolha_index = jogo.opcoes.index(escolher)  # Obtém o índice da escolha do jogador
        jogador, computador, resultado = jogo.jogar(escolha_index)  # Executa o jogo e obtém as escolhas e o resultado
        st.write(f"Jogador: {jogador}")  # Exibe a escolha do jogador
        st.write(f"Computador: {computador}")  # Exibe a escolha do computador
        st.write(resultado)  # Exibe o resultado


if __name__ == "__main__":
    main()
