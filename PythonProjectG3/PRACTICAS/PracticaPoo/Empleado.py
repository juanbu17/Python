from Usuario import Usuario


class Empleado(Usuario):
    rol = None
    salario = None

    def __init__(self, rol, salario, nombre, apellido):
        super().__init__(nombre, apellido)
        self._rol = rol
        self._salario = salario

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    nomina = []
    def crea_empleado(self):
        super().create_user()
        self._rol = input("Ingrese su rol en la empresa:\n")
        self._salario = int(input("Ingrese su salario:\n"))

    def listar(self):
        for empleado in self.nomina:
            print("Empleado agregado correctamente\n")
            print(empleado)