def miMetodo(x):
    return (x+1)/x

import unittest

class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(miMetodo(20),1.05)
        self.assertEqual(miMetodo(10),1.1)
        self.assertEqual(miMetodo(1),2)

if __name__ == '__main__':
    unittest.main()
