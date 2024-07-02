
class User:


    employee_id = None
    name_employee = None
    last_name_employee = None
    email = None
    password = None


    def __init__(self,employee_id, name_employee, last_name_employee, email, password):
        self._employee_id = employee_id
        self._name_employee = name_employee
        self._last_name_employee = last_name_employee
        self._email = email
        self._password = password

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def name_employee(self):
        return self._name_employee

    @name_employee.setter
    def name_employee(self, name_employee):
        self._name_employee = name_employee

    @property
    def last_name_employee(self):
        return self._last_name_employee

    @last_name_employee.setter
    def last_name_employee(self, last_name_employee):
        self._last_name_employee = last_name_employee

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


    employees = []

    def create_user(self, employees):
        #employee = []
        self._employee_id = input("Id empleado")
        #employee.append(self._employee_id)
        self._name_employee = input("Nombre empleado")
        #employee.append(self._name_employee)
        self._last_name_employee = input("Apellido empleado")
        #employee.append(self._last_name_employee)
        self._email = input("Correo")
        #employee.append(self._email)
        self._password = input("Contraseña")
        #employee.append(self._password)
        #self._salary = input("Salario")
        #employee.append(self._salary)

        #employees.append(employee)

    def list_employee_data(self, employees):
        for item in employees:
            print(item)