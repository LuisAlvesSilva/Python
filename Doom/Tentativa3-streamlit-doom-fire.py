import streamlit as st
import numpy as np

# Configurações da página
st.set_page_config(
    page_title="Doom Fire",
    layout="wide"
)

# Renderiza o canvas
canvas = st.empty()

# Função para renderizar o fogo
def renderFire(fire):
    # Escala os valores de intensidade do fogo para o intervalo 0-255
    fire = fire * 255 // np.max(fire)

    # Cria uma imagem em escala de cinza com base no array do fogo
    image = np.repeat(fire[:, :, np.newaxis], 3, axis=2).astype(np.uint8)

    # Renderiza a imagem no canvas
    canvas.image(image, use_column_width=True)

# Loop principal
def main():
    # Tamanho da área de renderização do fogo
    width = 80
    height = 40

    # Cria a matriz do fogo com zeros
    fire = np.zeros((height, width), dtype=np.uint8)

    # Define a última linha da matriz como valor máximo de intensidade do fogo
    fire[-1, :] = 255

    # Loop principal
    while True:
        # Renderiza o fogo
        renderFire(fire)

        # Propagação do fogo
        for row in range(height - 1):
            for col in range(width):
                decay = np.random.randint(0, 3)
                spread = fire[row + 1, col] - decay
                spread = max(spread, 0)
                spread_idx = np.random.randint(0, 3)
                fire[row, max(col + spread_idx - 1, 0):min(col + spread_idx + 2, width)] = spread

        # Gera um novo valor aleatório para a última linha do fogo
        fire[-1, :] = np.random.randint(0, 256, size=width)
        
        # Adiciona um pequeno atraso para controlar a velocidade do fogo
        st.experimental_rerun()

# Executa o aplicativo
if __name__ == '__main__':
    main()
