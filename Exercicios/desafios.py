#dolar = 3.25
#cambio = float(input("adicione quantos reais quer cambiar: "))
#soma = cambio * dolar
#print("Quantos dolares terá: ", soma)  
#x = 1
#while x==1:
#    questao= int(input("Selecione o tipo de media: "))
#    p1 = 8.66
#    p2 = 5.35
#    p3 = 5
#    p4 = 1
#    if questao ==1:
#        media_ma = p1 + p2 + p3 + p4 / 4
#        print(" A media aritimetica é: ", media_ma)
#    elif questao ==2:
#        media_mg = (p1 * p2 * p3 * p4) ** (1/4)
#        print(" A media geometrica é: ", media_mg)
#    elif questao ==3:
#        media_mh = (p1/1 + p2/1 + p3/1 + p4/1) // 4
#        print(" A media harmonica é: ", media_mh)
a=1
while a==1:
    import time
    dolar= 3.25
    x=299.99
    y=23.87
    w=66.66
    z=1.42
    frete=12.34
    soma= x + y + w + z
    reais= soma * dolar
    iof= reais % 0.638
    questao= float(input("selecione o que deseja: \n1-Valor total: \n2-Preço em reais: \n3-Valor do IOF: \n"))
    total= x + y + w + z
    if questao ==1:
        print("O Valor total é: ", soma)
        time.sleep(10)
    elif questao==2:
        print(" Valor total em reais: ", reais, "Valor do IOF em reais: ", iof)
        time.sleep(10)
    elif questao==3:
        print("Valor total IOF: ", soma - (soma - iof))
        time.sleep(10)
    elif questao==0:
        break 
