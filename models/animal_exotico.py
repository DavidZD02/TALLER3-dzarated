from models.animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def calcular_flete(self) -> float:
        return self.impuestos * self.peso
    