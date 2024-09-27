from faker import Faker

# Inicializamos Faker
fake = Faker()

class Person:
    def __init__(self, dni, name, lastname):
        self.dni = dni
        self.name = name
        self.lastname = lastname
    
    def __str__(self):
        return f"Person(DNI: {self.dni}, Name: {self.name}, Lastname: {self.lastname})"

# Función para generar instancias de Person
def generate_people(count):
    people = []
    for _ in range(count):
        dni = fake.ssn()  # Genera un número de identificación
        name = fake.first_name()  # Genera un nombre
        lastname = fake.last_name()  # Genera un apellido
        person = Person(dni, name, lastname)
        people.append(person)
    return people

def get_people(people):
    for person in people:
        print(person)



num_people = int(input("Ingrese el número de personas que desea generar: "))
people = generate_people(num_people)
get_people(people)