from model.vehiculo import vehiculo

class minivan(vehiculo):
    def __init__(self,marca,modelo,anio,pasajeros):
        super().__init__(marca,modelo,anio)
        self.pasajeros = pasajeros
    
    def descripcion(self):
        return f"{super().descripcion()}, Nro de Pasajeros, {self.pasajeros}"