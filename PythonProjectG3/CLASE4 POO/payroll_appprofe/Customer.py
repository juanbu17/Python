from payroll_appprofe.User import User


class Customer(User):
    type = None
    points = None

    #definir el metodo constructor:
    def __init__(self, employee_id, name_employee, last_name_employee, email, password, type, points):
        super().__init__(employee_id, name_employee, last_name_employee, email, password)
        self._type = type
        self._points = points

    #crear los getter y setter de los atributos nuevos(type y points:
        @property
        def type(self,type):
            self._type = type

        @type.setter
        def type(self,typé):
            self._type = type

        @property
        def points(self, points):
            self._points = points

        @type.setter
        def points(self, points):
            self._points = points


    #establecer una funcion para crear usuarios:
        def create_user(self):
            super().create_user()
            self._type = input("Indique el tipo de cliente: ")
            self._points = int(input("Puntos: "))


        self.costumers[self.employee_id]={"Nombre": self._name_employee, "Apellido": self._last_name_employee,"Correo":self._email,"Password":self._password, "Tipo":self._type,"Puntos":self._points}

        def list_costumers(self):
            for item in self.costumers.items():
                print(item)