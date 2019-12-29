#!/usr/bin/env python
__author__ = "Guilherme P. Paiva"
__date__ = "15/11/2019"

lista = [['A','B','C'],['D','E','F'],['G','H','I'], ['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'], ['W','X','Y','Z'], [' ']]

saida = ''

def entrada_valida(entrada):
	if not isinstance(entrada, str):
		return False
	if len(entrada) > 255 or len(entrada) <= 0:
		return False
	return all(x.isalpha() or x.isspace() for x in str(entrada))

def get_indice(letra):
	if letra >= 'A' and letra <= 'C':
		return 0
	if letra >= 'D' and letra <= 'F':
		return 1
	if letra >= 'G' and letra <= 'I':
		return 2
	if letra >= 'J' and letra <= 'L':
		return 3
	if letra >= 'M' and letra <= 'O':
		return 4
	if letra >= 'P' and letra <= 'S':
		return 5
	if letra >= 'T' and letra <= 'V':
		return 6
	if letra >= 'W' and letra <= 'Z':
		return 7
	if letra == ' ':
		return 8


def converte(entrada, saida = saida):
	for i in range(len(entrada)):
		contador = 1
		indice = get_indice(entrada[i])
		contador = (lista[indice].index(entrada[i])) + 1
		if indice == 8:
			saida += '0'
			continue
		saida += contador*str(indice+2)

		if i < len(entrada)-1:
			if indice == get_indice(entrada[i+1]):
				saida += '_'
	return saida

def main():
	entrada = input('Digite o texto a ser convertido:\n')
	while not entrada_valida(entrada):
		entrada = input('Por favor digite uma entrada valida: \n')
	print('Seu texto convertido:',converte(entrada.upper()))

if __name__ == '__main__':
	main()
