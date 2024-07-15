from Usuario import Usuario


class Vehiculo():
    tipo_vehiculo = None
    marca = None
    costo_servicio = None

    def __init__(self, tipo_vehiculo, marca, costo_servicio):
        #super().__init__(nombre, apellido)
        self._tipo_vehiculo = tipo_vehiculo
        self._marca = marca
        self._costo_servicio = costo_servicio

    @property
    def tipo_vehiculo(self):
        return self._tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self, tipo_vehiculo):
        self._tipo_vehiculo = tipo_vehiculo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


    @property
    def costo_servicio(self):
        return self._costo_servicio

    @costo_servicio.setter
    def costo_servicio(self,costo_servicio):
        self._costo_servicio = costo_servicio

    def crea_vehiculo(self):
        #super().create_user()
        self._tipo_vehiculo = input("Ingrese el tipo (carro, moto o camión: ")
        self._marca = input("Ingrese la marca: ")
        self._costo_servicio = input("Indique el costo del servicio: ")