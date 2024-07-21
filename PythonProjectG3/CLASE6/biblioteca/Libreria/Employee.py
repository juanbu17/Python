



class Employee():

    rol_position = None
    salary = None


    def __init__(self,rol_position, salary):
        self._rol_position = rol_position
        self._salary = salary



    @property
    def rol_position(self):
        return self._rol_position

    @rol_position.setter
    def salary(self, rol_position):
        self._rol_position = rol_position


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary


    employees = []

    def create_user(self):
        employee = []
        self._rol_position = input("Rol")
        employee.append(self._rol_position)
        self._salary = input("Salario")
        employee.append(self._salary)

        self.employees.append([self._rol_position,self._salary])


    def list_employee_data(self):
        for item in self.employees:
            print(item)

    def delete_employee(self):
        