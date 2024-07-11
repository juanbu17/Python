# users.py

users = []

def register():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    if any(user["username"] == username for user in users):
        print("El usuario ya existe")
        return
    user = {"username": username, "password": password}
    users.append(user)
    print("El usuario "+username+" fue registrado con éxito")

def login():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Inicio de sesión exitoso")
            return
    print("\n\n Sus credenciales no son correctas")

def main():
    while True:
        print("\n\n")
        print("---------Menú principal:----------")
        print("Seleccione una opción para iniciar")
        print("1. Registrar")
        print("2. Iniciar sesión")
        print("3. Salir")
        option = input("Opción seleccionada: ")

        if option == "1":
            register()
        elif option == "2":
            login()
        elif option == "3":
            print("App Finaliza!")
            break
        else:
            print("Opción inválida")


main()