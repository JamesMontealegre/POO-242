class Coche:
    def __init__(self, marca, modelo, año, precio):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._precio = precio

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_año(self):
        return self._año

    def get_precio(self):
        return self._precio

    def aplicar_descuento(self, porcentaje):
        descuento = self._precio * (porcentaje / 100)
        self._precio -= descuento
        print(f"Se ha aplicado un descuento del {porcentaje}%. Precio final: ${self._precio:.2f}")

    def __str__(self):
        return f"{self._marca} {self._modelo} ({self._año}) - ${self._precio:.2f}"
