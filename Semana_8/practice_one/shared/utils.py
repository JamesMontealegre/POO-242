import pickle
from faker import Faker
import random
from models.coche import Coche

fake = Faker()

def generar_coches(cantidad):
    coches = []
    for _ in range(cantidad):
        marca = fake.company()
        modelo = fake.word()
        año = random.randint(2000, 2023)
        precio = round(random.uniform(10000, 50000), 2)
        coches.append(Coche(marca, modelo, año, precio))
    return coches

def guardar_estado(concesionario, filename='estado_concesionario.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(concesionario, f)
    print("Estado del concesionario guardado con éxito.")

def cargar_estado(filename='estado_concesionario.pkl'):
    try:
        with open(filename, 'rb') as f:
            concesionario = pickle.load(f)
        print("Estado del concesionario cargado con éxito.")
        return concesionario
    except FileNotFoundError:
        print("No se encontró un archivo de estado previo.")
        return None
