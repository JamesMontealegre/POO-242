# class Persona

# __name: string
# __lastname: string
# __id: int
# __age: int
# __role: int

# 1: student
# 2: collaborator
# 3: security


def class_person(name, lastname, id, age, role):
    return {
        "name": name,
        "lastname": lastname,
        "id": id,
        "age": age,
        "role": role
    }

def show_objet(object_):
    print(object_)


def add_person():
    name = input("Por favor digite el nombre:\n")
    lastname = input("Por favor digite el apellido:\n")
    id = int(input("Por favor digite su ID:\n"))
    age = int(input("Por favor digite su edad:\n"))
    role = int(input("Por favor digite su rol:\n"))


# Agregar personas a una lista.
# Usar un bucle para agregar usuarios hasta el usuario decida no agregar mas
# Imprimir el contenido del listado
