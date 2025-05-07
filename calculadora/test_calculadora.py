import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def test_sumar_dos_mas_dos(self):
        cal = Calculadora()
        resultado = cal.sumar(2, 5)
        self.assertEqual(resultado, 7, "La suma de 2 + 2 debería ser 4")


if __name__ == '__main__':
    unittest.main()
