from util.Conexion import Conexion


class Person_Type:
    id_type = None
    type = None

    def __init__(self,id_type,type):
        self.id_type = id_type
        self._type  = type



    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self,id_type):
        self.id_type = id_type



    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, type):
        self.type = type

    db = Conexion(host='localhost', port=3306, user='root', password="", database='tienda_sura')
    db.connect()

    def create_type_person(self,db):
        self._type = input("Ingrese P_NAT, si es persona natural o P_JU si es persona juridica: ")
        query = "INSERT INTO costumer_type(costumer_type) VALUES(%S)"
        values = (self._type)
        db.execute.query(query,values)





