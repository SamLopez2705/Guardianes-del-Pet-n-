from animal import Animal


class CocodriloDePantano(Animal):
    def __init__(self, nombre, edad, habitat, longitud):
        super().__init__(nombre, edad, habitat)
        self.longitud = longitud

    def nadar(self):
        return f"{self.nombre} nada silenciosamente por el humedal."

    def alimentarse(self):
        mensaje_padre = super().alimentarse()
        return f"{mensaje_padre} El cocodrilo consume peces y otros animales."

    def describir(self):
        return (f"{self.nombre} es un cocodrilo de pantano que vive en {self.habitat}. "
                f"Es carnívoro, consume peces y otros animales, y se desplaza nadando. "
                f"Su longitud registrada es de {self.longitud} m.")
