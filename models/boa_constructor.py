from models.animal_exotico import Animal_Exotico

class Boa_Constructor(Animal_Exotico):
    
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float
                 , ratones_comidos: int):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comidos = ratones_comidos

    @staticmethod
    def hacer_sonido() -> str:
        print("¡Tsss!")
        return "¡Tsss!"

    def comer_raton(self):
        try:
            if(self.ratones_comidos > 10):
                raise ValueError("La boa esta llena")
            self.ratones_comidos += 1
            return f"Exito"
        except ValueError as e:
            return f"error: {e}"
    
    def comer_varios_ratones(self, cantidad):
        try: 
            if(cantidad >= 20):
                raise ValueError("Demasiados Ratones")
            self.ratones_comidos += cantidad
            return f"Ratones comidos: {cantidad}"
        except ValueError as e:
            return f"error: {e}"