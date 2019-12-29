from dojo import *

def test_valida_entrada():
	assert valida_entrada('OLA') == True
	assert valida_entrada('9') == False
	assert valida_entrada ('Hello World') == True

def test_converter():
	assert converter('m') == '6'
	assert converter('o') == '666'

def test_concatenar():
	assert concatenar('fala') == '33325552'
	assert concatenar('ab') == '2_22'