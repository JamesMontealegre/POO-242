# class Persona

# __name: string
# __lastname: string
# __id: string
# __age: int
# __role: string

# Desea continuar agregando personal a la base de datos
def addition():
    a = int(input('Por favor ingrese un número:\n'))
    b = int(input('Por favor ingrese otro número:\n'))
    # return "El resultado de la suma es: {}".format(a+b)
    return f"El resultado de la suma es: {a+b}"

while True:
    print(addition())
    response = input('¿Desea continar realizando sumas? s/n\n')
    if response != 's':
        break
    







