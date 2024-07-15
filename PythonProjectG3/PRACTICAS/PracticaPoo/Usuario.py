class Usuario:
    nombre = None
    apellido = None

    def __init__(self, nombre, apellido):

        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido


    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido


    usuarios = []
    def create_user(self):
        print("\n\nVamos a agregarte a nuesta base de datos")
        self._nombre = input("Ingresa el nombre: ")
        self.usuarios.append(self._nombre)
        self._apellido = input("Ingresa el apellido: ")
        self.usuarios.append(self._apellido)


    def list(self):
        for item in self.usuarios:
            print(item)

#print("Has sido agregado con exito")

# registrar el usuario nuevo:
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


