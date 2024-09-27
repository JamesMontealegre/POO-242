from models.coche import Coche
from models.cliente import Cliente
from models.concesionario import Concesionario
from shared.utils import generar_coches, guardar_estado, cargar_estado

# Crear o cargar concesionario
nombre_concesionario = "Autos XYZ"
concesionario = cargar_estado() or Concesionario(nombre_concesionario)

# Generar 5 coches aleatorios y agregarlos al concesionario
nuevos_coches = generar_coches(5)
for coche in nuevos_coches:
    concesionario.agregar_coche(coche)

# Mostrar los coches disponibles
concesionario.mostrar_coches()

# Crear cliente
cliente1 = Cliente("Ana", "123456789")

# Vender un coche al cliente
concesionario.vender_coche(cliente1, concesionario._coches_disponibles[0])

# Mostrar el coche comprado por el cliente
print(cliente1)

# Guardar el estado del concesionario
guardar_estado(concesionario)
