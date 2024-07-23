



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


    db = Connection(host = 'localhost',port = '3306',user = 'root',password ='',database ='library')
    db.connect()
    def create_employee(self,db):
        super().create_user()
        self._job_position = input("Escriba su área en la empresa")
        self._salary =  float(input("Ingrese su salario"))
        self._employee_insert(db)


    def list_employee_data(self):
        for item in self.employees:
            print(item)

    def delete_employee(self):

    def employee_insert(self,db):
        query = ("INSERT INTO employee(id_employee, name_employee, last_nane_employee, email ,password , job_position ,salary ) VALUES(%s,%s,%s,%s,%s,%s,%s,)")
        VALUES = (self._id_employee, self._name_employee, self._last_nane_employee,self._email, self._password,self._job_position,self._salary)

