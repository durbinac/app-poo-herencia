from model.deportivo import deportivo
from model.furgoneta import furgoneta
from model.minivan import minivan

objdeportivo = deportivo("Ferrari", "488", 2021, 330)
print(objdeportivo.descripcion())

objdeportivo = furgoneta("Sam", "200", 2024, 330)
print(objdeportivo.descripcion())

objdeportivo = minivan("Ferrari", "488", 2021, 330)
print(objdeportivo.descripcion())
