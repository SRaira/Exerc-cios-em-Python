#Questão 25 - Desenvolver um algoritmo que efetue a soma de todos os números ímares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.
controle = 1
acumulador = 0

while controle <= 500:
    #acompanhar o ciclo de cada contagem
    #print(f'Ele esta no ciclo {controle}')
    if (controle % 3) == 0 and (controle % 2) != 0:
        acumulador = acumulador + controle

    controle = controle + 1

print(acumulador)