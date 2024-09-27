class Cliente:
    def __init__(self, nombre, cedula):
        self._nombre = nombre
        self._cedula = cedula
        self._coche_comprado = None

    def comprar_coche(self, coche):
        self._coche_comprado = coche
        print(f"{self._nombre} ha comprado el coche {coche.get_marca()} {coche.get_modelo()}.")

    def __str__(self):
        if self._coche_comprado:
            return f"Cliente: {self._nombre}, Cédula: {self._cedula}, Coche comprado: {self._coche_comprado}"
        else:
            return f"Cliente: {self._nombre}, Cédula: {self._cedula}, Coche comprado: Ninguno"
