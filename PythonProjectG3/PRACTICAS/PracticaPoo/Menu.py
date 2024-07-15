from Empleado import Empleado
from Funciones import empleo, enlistar
from Usuario import Usuario
from Vehiculo import Vehiculo


usuario = Usuario(None, None)

empleado = Empleado(None, None, None, None)

vehiculo = Vehiculo(None,None,None)

login = input("Desea iniciar sesión? (Y/N):\n").upper()
if login == "Y":
    usuario.registrar()
    empleo()
    enlistar()
    vehiculo.crea_vehiculo()
    vehiculo.listar_datos_vehiculo()
elif login == "N":
    print("Ten un buen día")
else:
    print("Ingrese una opción valida")