#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#  e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar
# , sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite quantos Km você percorreu com o carro: '))
dia = int(input('Agora digite quantos dias você ficou com o carro: '))
custo = (60*dia)+(0.15*km)
print('O custo de {}KM em {} dias é de R${}'.format(km, dia, custo))