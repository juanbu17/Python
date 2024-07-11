

class Usuario:
    def __init__(self, nombre, marca, usuario, contrasena, precio):
        self.nombre = nombre
        self.marca = marca
        self.usuario = usuario
        self.contrasena = contrasena
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} {self.marca} {self.usuario}"