import requests
import random
from visual import vidas_visual_dict
import string

def palavras():
    master = "https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt"
    req = requests.get(master)
    req = req.text
    dic = req.split('\n')
    return dic

def escolha_palavras():
    palavra = random.choice(palavras())
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras())
    return palavra.upper()

def forca():
    palavra_s = escolha_palavras()
    palavra_letras = set(palavra_s)
    alfabeto = set(string.ascii_uppercase)
    letra_usada = set()

    vidas = 7

    while len(palavra_letras) > 0:

        print("Você usou a letra", " ".join(letra_usada))
        palavra_mostrada = [
            letra if letra in letra_usada else '-' for letra in palavra_s]
        print(vidas_visual_dict[vidas])
        print("Palavra: " + " ".join(palavra_mostrada))

        entrada = input("Escreva uma letra: ").upper()
        if entrada in alfabeto - letra_usada:
            letra_usada.add(entrada)
            if entrada in palavra_s:
                palavra_letras.remove(entrada)
            else:
                vidas = vidas - 1
                print("Letra não está na palavra.")
        elif entrada in letra_usada:
            print("Você já usou essa letra! Tente novamente.")
        else:
            print("Entrada inválida!")

        if vidas == 0:
            print(vidas_visual_dict[vidas])
        
        else:
            print('YAY! You guessed the word!!')

    print(f"Parabéns! A palavra era '{palavra_s}'.")

if __name__ == '__main__':
    forca()
