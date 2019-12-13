from dojo import *

def test_valid_input():	
	assert entrada_valida(1) == False
	assert entrada_valida('ABCDEF GHI') == True
	assert entrada_valida('') == False

def test_get_indice():
	assert get_indice('A') == 0
	assert get_indice(' ') == 8
	assert get_indice('J') == 3

def test_converte():
	assert converte('PUZZLES') == '7889999_9999555337777'
	assert converte('OI PESSOAL') == '66644407337777_77776662555'