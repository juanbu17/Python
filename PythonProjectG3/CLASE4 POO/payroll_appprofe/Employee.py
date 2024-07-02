from User import User


class Employee(User):

    rol = None
    salary = None

    def __init__(self,employee_id, name_employee, last_name_employee, email, password, rol, salary):
        super().__init__(employee_id, name_employee, last_name_employee, email, password)
        self._rol = rol
        self._salary = salary

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def employee_id(self, rol):
        self._rol = rol

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    #employees =[]

    def create_user(self, employees):
        #employee = []
        super().create_user(employees)
        self._rol = input("Rol: ")
        #employee.append(self._rol)
        self._salary = input("Salario: ")
        #employee.append(self._salary)

        self.employees.append([self._employee_id, self._name_employee, self._last_name_employee, self._email, self._password, self._rol, self._salary])

        #User.employees.append(employee)

    def list_employee_data(self, employees):
        for item in employees:
            print(item)