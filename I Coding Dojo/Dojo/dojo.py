ns = [[' '],[''], ['a','b','c'], ['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

def valida_entrada(entrada):
	count = 0
	while(count < len(entrada)):
		if entrada[count].isalpha() or entrada[count].isspace():
			pass
		else:
			return False
		count += 1
	return True

def converter(entrada):
	for i in range(len(ns)):
		if entrada in ns[i]:
			pos = ns[i].index(entrada)+1
			return pos*str(i)

def concatenar(entrada):
	palavra=''
	for i in entrada:
		palavra += converter(i)

	return palavra