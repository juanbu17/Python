
from Conexion import Conexion


db = Conexion(host = 'localhost', port = 3306 , user = 'root' , password= ""  , database= 'tienda_sura')
db.connect()