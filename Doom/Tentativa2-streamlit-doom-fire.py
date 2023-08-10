import streamlit as st
import numpy as np
import cv2

# Configurações da página
st.set_page_config(
    page_title="Doom Fire",
    layout="wide"
)

# Estilos CSS
st.markdown("""
    <style>
        body {
            width: 100vw;
            height: 100vh;
            margin: 0px;
            display: flex;
            justify-content: center;
            align-items: center;

            color: rgb(255, 255, 255);
            background-color: rgb(32, 32, 32);

            font-family: Arial;
            font-size: 16px;
        }
        canvas {
            margin: 8px;
        }
        button {
            width: 150px;
            height: 36px;
            padding: 0px 16px;
            margin: 8px;

            color: rgb(255, 255, 255);
            background-color: rgb(255, 87, 34);
            border: none;
            border-radius: 2px;
            outline: none;

            text-transform: uppercase;
            font-size: 14px;
            font-weight: bold;
            letter-spacing: 0.08rem;

            cursor: pointer;

            -webkit-user-select: none;
            -ms-user-select: none;
            -moz-user-select: none;
            -o-user-select: none;
            user-select: none;

            -webkit-transition: all 0.2s;
            -moz-transition: all 0.2s;
            -ms-transition: all 0.2s;
            -o-transition: all 0.2s;
            transition: all 0.2s;
        }
        button:active {
            -webkit-transform: scale(0.96);
            -moz-transform: scale(0.96);
            -ms-transform: scale(0.96);
            -o-transform: scale(0.96);
            transform: scale(0.96);
        }
    </style>
""", unsafe_allow_html=True)

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

    # Executa o aplicativo
if __name__ == '__main__':
    main()
