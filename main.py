from animal import Animal
from alerta import Alerta
from sistema_guardianes import SistemaGuardianes
from jaguar import Jaguar
from tapir import Tapir
from guacamaya_roja import GuacamayaRoja
from cocodrilo_de_pantano import CocodriloDePantano


def main():
    sistema = SistemaGuardianes()
    # Conservamos los constructores de las entregas anteriores.
    jaguar = Jaguar("Balam", 6, "Selva tropical del Petén", 1500)
    tapir = Tapir("Tikal", 4, "Bosque húmedo", 240)
    guacamaya = GuacamayaRoja("Ixchel", 3, "Dosel del bosque", 1.1)
    cocodrilo = CocodriloDePantano("Itzá", 8, "Humedales y lagunas", 3.2)
    # Se asigna un código único a cada ejemplar.
    jaguar.codigo = "JAG-001"
    tapir.codigo = "TAP-002"
    guacamaya.codigo = "GUA-001"
    cocodrilo.codigo = "CDP-001"
    # Los agregamos intencionalmente en desorden.
    for animal in [tapir, jaguar, cocodrilo, guacamaya]:
        sistema.agregar_animal(animal)

    for alerta in [
        Alerta("AL-01", "media", "10:15", "Huella cerca del sendero"),
        Alerta("AL-02", "alta", "09:40", "Animal herido"),
        Alerta("AL-03", "media", "08:30", "Revisión de bebedero"),
        Alerta("AL-04", "alta", "07:20", "Incendio reportado"),
        Alerta("AL-05", "alta", "11:05", "Trampa encontrada"),
    ]:
        sistema.agregar_alerta(alerta)

    print("=== GUARDIANES DEL PETEN - ENTREGA 4 ===")
    print("\n1. ALERTAS ANTES DE ORDENAR")
    for alerta in sistema.alertas:
        print(alerta)
    sistema.ordenar_alertas()
    print("\n2. ALERTAS ORDENADAS POR PRIORIDAD Y HORA")
    for alerta in sistema.alertas:
        print(alerta)

    print("\n3. BUSQUEDA BINARIA DE ANIMALES")
    sistema.ordenar_animales_por_codigo()
    print("Códigos ordenados:", ", ".join(a.codigo for a in sistema.animales))
    for codigo in [sistema.animales[0].codigo, sistema.animales[-1].codigo, "NO-999"]:
        encontrado = sistema.buscar_animal(codigo)
        print(f"{codigo}: {encontrado.mostrar_info() if encontrado else 'No encontrado'}")

    print("\n4. POLIMORFISMO (ENTREGA 3)")
    for animal in sistema.animales:
        print(animal.describir())

    print("\n5. CLASE ABSTRACTA (ENTREGA 3)")
    try:
        Animal("Genérico", 1, "Petén")
    except TypeError as error:
        print("TypeError:", error)

    print("\n6. HERENCIA Y METODOS ANTERIORES (ENTREGAS 1 Y 2)")
    print(jaguar.mostrar_info())
    print(jaguar.alimentarse())
    print(jaguar.cazar())
    print(tapir.buscar_frutas())
    print(guacamaya.volar())
    print(cocodrilo.nadar())
    print("\nPruebas finalizadas correctamente.")
    input("\nPresione ENTER para cerrar...")


if __name__ == "__main__":
    main()
