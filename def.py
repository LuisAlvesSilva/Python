
def soma():
    x= float(input("primeiro numero: "))
    y= float(input("segundo numero: "))
    soma= x + y
    return soma
    
continuar = 1

while continuar:
    if(continuar):
        soma()
    continuar=int(input("digite 0 se desejar encerrar ou qualquer outro numero para continuar: "))

