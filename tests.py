import unittest
from main import palidromo

class PalidromoTest(unittest.TestCase):

    def test_anna(self):
        palabra_prueba = palidromo('anna')
        self.assertEqual(palidromo('anna'),True)

    def test_cerveza(self):
        palabra_prueba = palidromo('cerveza')
        self.assertEqual(palidromo('cerveza'),False)

    def test_queso(self):
        palabra_prueba = palidromo('queso')
        self.assertEqual(palidromo('queso'),False) 
    
    def test_neuquen(self):
        palabra_prueba = palidromo('neuquen')
        self.assertEqual(palidromo('neuquen'),True)       


if __name__ == "__main__":
    unittest.main()