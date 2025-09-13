#Doctest

def sumar(x,y):
	"""
	Esta funcion resive 2 numero y regresa su suma

	>>> sumar(4,3)
	7

	>>> sumar(1,7)
	8

	>>> sumar(3,3)
	4

	"""
	return x + y

import doctest
doctest.testmod()