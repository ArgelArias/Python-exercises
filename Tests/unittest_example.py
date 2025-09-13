#Unittest

def multiplicar(x,y):
	return x * y

import unittest

class pruebas(unittest.TestCase):
	def test(self):
		self.assertEqual(multiplicar(4,4),16)
		self.assertEqual(multiplicar(4,4),14)
		self.assertEqual(multiplicar(4,2),10)
		self.assertEqual(multiplicar(5,2),10)

if __name__ == '__main__':
	unittest.main()