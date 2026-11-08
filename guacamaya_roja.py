from animal import Animal


class GuacamayaRoja(Animal):
    def __init__(self, nombre, edad, habitat, envergadura):
        super().__init__(nombre, edad, habitat)
        self.envergadura = envergadura

    def volar(self):
        return f"{self.nombre} vuela sobre el bosque del Petén."

    def alimentarse(self):
        mensaje_padre = super().alimentarse()
        return f"{mensaje_padre} La guacamaya roja consume semillas, frutos y nueces."

    def describir(self):
        return (f"{self.nombre} es una guacamaya roja que vive en {self.habitat}. "
                f"Consume semillas, frutos y nueces, y se desplaza volando sobre el bosque. "
                f"Su envergadura registrada es de {self.envergadura} m.")
