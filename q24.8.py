#Questão 24 - Elabore um algoritmo que, a partir de um dia, mês e ano fornecidos, valide se eles compõem uma data válida. Não deixe de considerar os meses com 30 ou 31 dias, e o tratamento de ano bissexto.
dia = int(input('Digite o seu dia escolhido: '))
mes = int(input('Digite o seu mes escolhido: '))
ano = int(input('Digite o seu ano escolhido: '))
bissexto = ''

#verificado se o ano é bissexto:
if (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) == 0:
    bissexto = True
elif (ano % 4) != 0:
    bissexto = False
elif (ano % 4) == 0 and (ano % 100) != 0:
    bissexto = True
elif (ano % 4) == 0 and (ano % 100) == 0 and (ano % 400) !=0:
    bissexto = False

#verificando datas válidas:
if mes == 1 and dia >=1 and dia <=31:
    print('{} de Janeiro'.format(dia))

elif mes == 2 and dia >= 1 and dia <= 28 and bissexto == False:
    print('{} de Fevereiro'.format(dia))
    print('Ano não é Bissexto')

elif mes == 2 and dia >= 1 and dia <= 29 and bissexto == True:
    print('{} de Fevereiro'.format(dia))
    print('Ano é Bissexto')

elif mes == 3 and dia >= 1 and dia <= 2:
    print('{} de Março'.format(dia))

elif mes == 4 and dia >= 1 and dia <= 28:
    print('{} de Abril'.format(dia))

elif mes == 5 and dia >= 1 and dia <= 31:
    print('{} de Maio'.format(dia))

elif mes == 6 and dia >= 1 and dia <= 30:
    print('{} de Junho'.format(dia))

elif mes == 7 and dia >= 1 and dia <= 31:
    print('{} de Julho'.format(dia))

elif mes == 8 and dia >= 1 and dia <= 31:
    print('{} de Agosto'.format(dia))

elif mes == 9 and dia >= 1 and dia <= 30:
    print('{} de Setembro'.format(dia))

elif mes == 10 and dia >= 1 and dia <= 31:
    print('{} de Outubro'.format(dia))

elif mes == 11 and dia >= 1 and dia <= 30:
    print('{} de Novembro'.format(dia))

elif mes == 12 and dia >= 1 and dia <= 31:
    print('{} de Dezembro'.format(dia))

else:
    print('Você digitou um mês invalido')