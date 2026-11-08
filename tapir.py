from animal import Animal


class Tapir(Animal):
    def __init__(self, nombre, edad, habitat, peso):
        super().__init__(nombre, edad, habitat)
        self.peso = peso

    def buscar_frutas(self):
        return f"{self.nombre} busca frutas y hojas entre la vegetación."

    def alimentarse(self):
        mensaje_padre = super().alimentarse()
        return f"{mensaje_padre} El tapir es herbívoro y consume frutos, hojas y brotes."

    def describir(self):
        return (f"{self.nombre} es un tapir que vive en {self.habitat}. "
                f"Es herbívoro, consume frutos, hojas y brotes, y camina entre la vegetación. "
                f"Su peso registrado es de {self.peso} kg.")
