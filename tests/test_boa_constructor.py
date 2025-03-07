import unittest
from models.boa_constructor import Boa_Constructor
from guarderia import Guarderia

class TestBoaConstructor(unittest.TestCase):
    def test_hacer_sonido(self):
        boa = Boa_Constructor("Pedro", 100, 10, "Colombia", 100, 0)
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        boa = Boa_Constructor("Pedro", 100, 10, "Colombia", 100, 0)
        self.assertEqual(boa.calcular_flete(), 10000)

    def test_comer_raton(self):
        boa = Boa_Constructor("Pedro", 100, 10, "Colombia", 100, 0)
        boa.comer_raton()
        self.assertEqual(boa.ratones_comidos, 1)
        boa.comer_raton()
        self.assertEqual(boa.ratones_comidos, 2)

    def test_comer_varios_ratones(self):
        boa = Boa_Constructor("Pedro", 100, 10, "Colombia", 100, 0)
        self.assertEqual(boa.comer_varios_ratones(10), "Ratones comidos: 10")
        self.assertEqual(boa.comer_varios_ratones(100), "error: Demasiados Ratones")
