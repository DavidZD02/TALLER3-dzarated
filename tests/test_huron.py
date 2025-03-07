import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron("David", 10, 2, "Colombia", 30)
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        huron = Huron("David", 10, 2, "Colombia", 30)
        self.assertEqual(huron.calcular_flete(), 300)   