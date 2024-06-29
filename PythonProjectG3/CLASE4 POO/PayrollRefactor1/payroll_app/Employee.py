class Employee:

    employee_id = None
    name_employee = None
    last_name_employee = None
    email = None
    password = None
    salary = None

    # comment
    # init es un metodo que va hacer la vez de constructor
    # - protegido
    #__ privado
    # decoradores: anotaciones que se usan en Java

    def _init_(self, employee_id, name_employee, last_name_employee, email, password, salary):
        self._employee_id = employee_id
        self._name_employee = name_employee
        self._last_name_employee = last_name_employee
        self._email = email
        self._password = password
        self._salary = salary

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employeed_id(self, employee_id):
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
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self):
        return self._password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self):
        return self._salary

    employees = []

    def create_user(self, employees):
        employee = []
        self._employee_id = input("Id Empleado: ")
        employee.append(self._employee_id)
        self._name_employee = input("Nombre Empleado: ")
        employee.append(self._name_employee)
        self._last_name_employee = input("Apellido Empleado: ")
        employee.append(self._last_name_employee)
        self._email = input("Email: ")
        employee.append(self._email)
        self._password = input("Contraseña: ")
        employee.append(self._password)
        self._salary = input("Salario: ")
        employee.append(self._salary)

        employees.append(employee)

    def list_employee_data(self, employees):
        for item in employees:
            print(item)