import sys

from Empleado import Empleado
from Vehiculo import Vehiculo

empleado = Empleado(None, None, None, None)
vehiculo = Vehiculo(None, None, None)

def empleo():
    registro = input("Desea ingresar sus datos de empleado? (Y/N):\n").upper()

    if registro == "Y":
        empleado.crea_empleado()
    elif registro == "N":
        print("Buen día")
        sys.exit()
    else:
        print("Ingrese una opción válida")
        sys.exit()

def enlistar():
    datos = input("Desea ver sus datos agregados anteriormente? (Y/N):\n").upper()

    if datos == "Y":
        empleado.list()
    elif datos == "N":
        pass
    else:
        print("Ingrese una opción válida")
        sys.exit()

def datos_vehiculo():
    taller = input("Desea ver sus datos del servicio? (Y/N):\n").upper()

    if taller == "Y":
        vehiculo.listar_datos_vehiculo()
    elif taller == "N":
        print("Buen día")
    else:
        print("Ingrese una opción válida")
        sys.exit()