class Usuario:
    def _init_(self, nombre, apellido, usuario, contrasena,salario_bruto):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contrasena = contrasena
        self.salario_bruto = salario_bruto
    def _str_(self):
        return f"{self.nombre} {self.apellido}"