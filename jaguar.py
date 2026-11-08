from animal import Animal


class Jaguar(Animal):
    def __init__(self, nombre, edad, habitat, fuerza_mordida):
        super().__init__(nombre, edad, habitat)
        self.fuerza_mordida = fuerza_mordida

    def cazar(self):
        return f"{self.nombre} caza sigilosamente en la selva."

    def alimentarse(self):
        mensaje_padre = super().alimentarse()
        return f"{mensaje_padre} El jaguar es carnívoro y consume principalmente carne."

    def describir(self):
        return (f"{self.nombre} es un jaguar que vive en {self.habitat}. "
                f"Es carnívoro, caza sigilosamente y se desplaza por tierra. "
                f"Su fuerza de mordida registrada es de {self.fuerza_mordida} PSI.")
