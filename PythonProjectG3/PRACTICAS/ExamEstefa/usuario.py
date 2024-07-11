
class Usuario:
    def __init__(self, nombre, apellido, usuario, contrasena, salario_bruto):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contrasena = contrasena
        self.salario_bruto = salario_bruto


    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.usuario})"

    def registrar_usuario(self):
        print("Ingrese su información:")
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        self.contrasena = contrasena
        self.salario_bruto = int(input("Salario bruto: "))

    def autenticar_usuario(self, usuario, contrasena):
        return self.usuario == usuario and self.contrasena == contrasena
