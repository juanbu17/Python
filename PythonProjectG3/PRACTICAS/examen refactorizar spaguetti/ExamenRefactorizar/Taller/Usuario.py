

class Usuario:
    nombre = None
    apellido = None



    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido


    @property
    def nombre(self, nombre):
        self._nombre = nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def apellido(self, apellido):
        self._apellido = apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

#crear los  nuevos usuarios:
    usuarios = []
    def create_user(self):
        self._nombre = input("Ingresa el nombre")
        self.usuarios.append(self._nombre)
        self._apellido = input("Ingresa el apellido")
        self.usuarios.append(self._apellido)

 #listar los usuarios existentes:
    def list(self):
        for item in self.usuarios:
            print(item)


#registrar el usuario nuevo:

users = []
def registrar():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    if any(user["username"] == username for user in users):
        print("El usuario ya esta registrado!!!")
        return
    user = {"username": username, "password": password}
    users.append(user)
    print("Registro exitoso")



# loguear el usuario nuevo:
    def loguear():
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
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Salir")
            option = input("Seleccione una opción: ")

            if option == "1":
                registrar()
            elif option == "2":
                loguear()
            elif option == "3":
                print("Salió de la App!")
                break
            else:
                print("Opción inválida")

    if __name__ == "__main__":
        main()