from models.animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)

    @staticmethod
    def hacer_sonido() -> None:
        print("¡Eek Eek!")
        return "¡Eek Eek!"