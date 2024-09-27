class Concesionario:
    def __init__(self, nombre):
        self._nombre = nombre
        self._coches_disponibles = []

    def agregar_coche(self, coche):
        self._coches_disponibles.append(coche)
        print(f"Se ha agregado {coche} al inventario del concesionario.")

    def mostrar_coches(self):
        if not self._coches_disponibles:
            print("No hay coches disponibles en este momento.")
        else:
            print(f"Coches disponibles en {self._nombre}:")
            for coche in self._coches_disponibles:
                print(f"- {coche}")

    def vender_coche(self, cliente, coche):
        if coche in self._coches_disponibles:
            cliente.comprar_coche(coche)
            self._coches_disponibles.remove(coche)
            print(f"El coche {coche} ha sido vendido a {cliente._nombre}.")
        else:
            print(f"El coche {coche} no está disponible.")
