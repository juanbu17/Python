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
        print("Vamos a agregarte a nuesta base de datos")
        self._nombre = input("Ingresa el nombre:\n")
        self.usuarios.append(self._nombre)
        self._apellido = input("Ingresa el apellido:\n")
        self.usuarios.append(self._apellido)


    def list(self):
        for item in self.usuarios:
            print(item)
        print("Has sido agregado con exito\n")

    # registrar el usuario nuevo:
    users = []
    def registrar(self):
        user = []
        username = input("Ingrese un nombre de usuario:\n")
        password = input("Ingrese una contraseña:\n")
        if any(user["username"] == username for user in self.users):
            print("El usuario ya esta registrado!!!\n")
            return
        self.users.append(username)
        self.users.append(password)
        self.users.append(user)
        print("Registro exitoso\n")
