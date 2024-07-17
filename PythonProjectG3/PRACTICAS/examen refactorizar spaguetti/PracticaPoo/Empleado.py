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

    def create_employee(self):
        super().create_user()
        self._rol = input("Ingrese su rol enla empresa: ")
        self._salario = int(input("Ingrese su salario: "))
