import calendar                                                                           #importando modulo de calendario.

ano = int(input("Digite o Ano: "))                                                        #Solicitando o ano via input.   

if ano >= 1:                                                                              #Condição de definição do ano.
    calendario = calendar.calendar(ano)                                                   #Variavel de ano, a partir do modulo calendar
    print ("Esse é o Calendario do mês",ano)
    print ("--------------------------------------------------------------------------") 
    print (calendario); 
    print ("--------------------------------------------------------------------------")                      
