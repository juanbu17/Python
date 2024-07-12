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
        self._nombre = input("Ingresa el nombre")
        self.usuarios.append(self._nombre)
        self._apellido = input("Ingresa el apellido")
        self.usuarios.append(self._apellido)


    def list(self):
        for item in self.usuarios:
            print(item)

