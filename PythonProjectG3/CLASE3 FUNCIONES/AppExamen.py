# Crea una plicación que se pueda inicializar y permita navegar en menu [registrar, iniciar sesión, salir]l
# crear registro del usuario
# guardarlo en una lista
# imprimir los datos del usuario
# el usuario solo puede ver sus datos si inicia sesión
# Al iniciar sesión deberá tener un menú que le ponga a elegir entre datos o calcular el salario neto
# El cuál debe imprimir el nombre, apellido, cargo, salario bruto, descuento de salud, descuento de pension y salario neto
"""
Este código define una lista usuarios que almacenará los registros de los usuarios. 
La función registrar_usuario permite registrar un nuevo usuario y lo agrega a la lista.
La función iniciar_sesion permite iniciar sesión con un usuario existente y llama a la función menu_usuario que muestra un menú al usuario.
 La función menu_usuario permite al usuario ver sus datos o calcular su salario neto. 
 La función imprimir_datos_usuario imprime los datos del usuario 
 y la función calcular_salario_neto calcula y imprime el salario neto del usuario.
"""

# farmacia.py

usuarios = []

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cargo = input("Ingrese su cargo: ")
    salario_bruto = float(input("Ingrese su salario bruto: "))
    descuento_salud = float(input("Ingrese el descuento de salud: "))
    descuento_pension = float(input("Ingrese el descuento de pension: "))

    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "salario_bruto": salario_bruto,
        "descuento_salud": descuento_salud,
        "descuento_pension": descuento_pension
    }

    usuarios.append(usuario)
    print("Usuario registrado con éxito!")

def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    for usuario in usuarios:
        if usuario["nombre"] == nombre_usuario:
            print("Bienvenido!")
            menu_usuario(usuario)
            return
    print("Usuario no encontrado. Intente de nuevo.")

def menu_usuario(usuario):
    while True:
        print("Menú:")
        print("1. Ver datos")
        print("2. Calcular salario neto")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            imprimir_datos_usuario(usuario)
        elif opcion == "2":
            calcular_salario_neto(usuario)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def imprimir_datos_usuario(usuario):
    print("Datos del usuario:")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Apellido: {usuario['apellido']}")
    print(f"Cargo: {usuario['cargo']}")
    print(f"Salario bruto: {usuario['salario_bruto']}")
    print(f"Descuento de salud: {usuario['descuento_salud']}")
    print(f"Descuento de pension: {usuario['descuento_pension']}")

def calcular_salario_neto(usuario):
    salario_neto = usuario["salario_bruto"] - usuario["descuento_salud"] - usuario["descuento_pension"]
    print(f"Salario neto: {salario_neto}")

def main():
    while True:
        print("Menú:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()