

class Usuario:
    nombre = None
    apellido = None

    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self, nombre):
        self._nombre = nombre

    @type.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def apellido(self, apellido):
        self._apellido = apellido

    @type.setter
    def apellido(self, apellido):
        self._apellido = apellido


#registrar el usuario nuevo:
    users = []

    def register():
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        if any(user["username"] == username for user in users):
            print("El usuario ya existe")
            return
        user = {"username": username, "password": password}
        users.append(user)
        print("Usuario registrado con éxito")



# loguear el usuario nuevo:
    def login():
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Inicio de sesión exitoso")
                return
        print("Credenciales incorrectas")


    def main():
        while True:
            print("\n\n\n")
            print("---------Menú principal:----------")
            print("Seleccione una opción para iniciar")
            print("1. Registrar")
            print("2. Iniciar sesión")
            print("3. Salir")
            option = input("Seleccione una opción: ")

            if option == "1":
                register()
            elif option == "2":
                login()
            elif option == "3":
                print("Adiós!")
                break
            else:
                print("Opción inválida")

    if __name__ == "__main__":
        main()