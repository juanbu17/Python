from Empleado import Empleado
from Usuario import Usuario
from Vehiculo import Vehiculo


usuario = Usuario(None, None)
#usuario.registrar()

empleado = Empleado(None, None, None, None)
empleado.crea_empleado()
empleado.list()

vehiculo = Vehiculo(None,None,None)
vehiculo.crea_vehiculo()
