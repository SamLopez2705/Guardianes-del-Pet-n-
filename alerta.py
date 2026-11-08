class Alerta:
    def __init__(self, codigo, prioridad, hora, descripcion):
        self.codigo = codigo
        self.prioridad = prioridad
        self.hora = hora  # Formato HH:MM de 24 horas
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.codigo} | {self.prioridad.upper():5} | {self.hora} | {self.descripcion}"
