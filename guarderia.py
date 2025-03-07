import unittest
from models.boa_constructor import Boa_Constructor
import unittest
from models.huron import Huron

class Guarderia:

    def __init__(self):
        self.huron1 = Huron("David", 10, 2, "Colombia", 30)
        self.huron2 = Huron("Santiago", 20, 4, "Argentina", 60)
        self.boa1 = Boa_Constructor("Pedro", 100, 10, "Colombia", 100, 0)
        self.boa2 = Boa_Constructor("Pablo", 120, 30, "Peru", 30, 0)

    def alimentar_boa(self, boa1):
        boa1.comer_raton()




