import unittest
from math_utils import es_par #aun no existe, queremos ver fallar, RED

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))  # 4 deberia ser par

    def test_5_es_par(self):
        self.assertFalse(es_par(5))  # 5 no deberia ser par
    
    def test_negativo(self):
        self.assertTrue(es_par(-2))  # deberia funcionar igual
        self.assertFalse(es_par(-5))



if __name__ == "__main__":
    unittest.main()
