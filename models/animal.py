from abc import ABC, abstractmethod
from models.ianimal import IAnimal

class Animal(IAnimal, ABC):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0

    def comer(self, kilos: float):
        self._kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return self._kilos_comidos

    @abstractmethod
    def hacer_sonido(self):
        pass

    # Setter Nombre
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> str:
        if isinstance(nuevo_nombre, str) and nuevo_nombre != '':
            self._nombre = nuevo_nombre
        else:
            raise ValueError('Expected str')
    
    # Setter Peso
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, nuevo_peso:float) -> float:
        if isinstance(nuevo_peso, float) and nuevo_peso != '':
            self._peso = nuevo_peso
        else:
            raise ValueError('Expected float')

    # Setter Edad
    @property
    def edad(self):
        return self._edad
    
    @peso.setter
    def edad(self, nueva_edad:int) -> int:
        if isinstance(nueva_edad, int) and nueva_edad != '':
            self._peso = nueva_edad
        else:
            raise ValueError('Expected int')
        
