

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

