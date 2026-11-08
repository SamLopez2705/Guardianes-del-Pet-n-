class SistemaGuardianes:
    def __init__(self):
        self.animales = []
        self.alertas = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def agregar_alerta(self, alerta):
        self.alertas.append(alerta)

    def ordenar_alertas(self):
        def nivel(alerta):
            if alerta.prioridad == "alta":
                return 1
            return 2

        # Selección: una sola permuta por pasada, ordenando por nivel y hora.
        for i in range(len(self.alertas) - 1):
            menor = i
            for j in range(i + 1, len(self.alertas)):
                actual = (nivel(self.alertas[j]), self.alertas[j].hora)
                candidato = (nivel(self.alertas[menor]), self.alertas[menor].hora)
                if actual < candidato:
                    menor = j
            if menor != i:
                self.alertas[i], self.alertas[menor] = self.alertas[menor], self.alertas[i]

    def ordenar_animales_por_codigo(self):
        # Selección por código, sin sort() ni sorted().
        for i in range(len(self.animales) - 1):
            menor = i
            for j in range(i + 1, len(self.animales)):
                if self.animales[j].codigo < self.animales[menor].codigo:
                    menor = j
            if menor != i:
                self.animales[i], self.animales[menor] = self.animales[menor], self.animales[i]

    def buscar_animal(self, codigo):
        self.ordenar_animales_por_codigo()
        inicio = 0
        fin = len(self.animales) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.animales[medio].codigo == codigo:
                return self.animales[medio]
            if self.animales[medio].codigo < codigo:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None
