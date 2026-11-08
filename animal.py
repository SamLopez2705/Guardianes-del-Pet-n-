from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre, edad, habitat, codigo=None):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat

    def mostrar_info(self):
        return f"{self.nombre} - Edad: {self.edad} años - Hábitat: {self.habitat}"

    def alimentarse(self):
        return f"{self.nombre} se está alimentando."

    def desplazarse(self):
        return f"{self.nombre} se desplaza por su hábitat."

    @abstractmethod
    def describir(self):
        pass
