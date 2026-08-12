import unittest
from math_utils import es_multiplo_de #aun no existe, queremos ver fallar, RED

class TestEsMultiplo(unittest.TestCase):
    def test_positivos(self):
        self.assertTrue(es_multiplo_de(8,8)) 
        self.assertFalse(es_multiplo_de(4,8)) 
        self.assertTrue(es_multiplo_de(8,2))

    def test_negativos(self):
        self.assertTrue(es_multiplo_de(-8,8)) 
        self.assertTrue(es_multiplo_de(8,-8)) 
        self.assertFalse(es_multiplo_de(5,2))
        self.assertTrue(es_multiplo_de(9,3)) 

    def test_ceros(self):
        self.assertFalse(es_multiplo_de(2,0)) # me saca error
        self.assertTrue(es_multiplo_de(0,2)) 

