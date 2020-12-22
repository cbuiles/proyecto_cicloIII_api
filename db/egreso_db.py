from pydantic.types import ConstrainedStr
from models import egreso
from pydantic import BaseModel
from typing import Dict
from datetime import date

class EgresoInDB(BaseModel):
    tipo: str
    valor: int
    fecha: date= date.today()

tipos_validos = ['arriendo', 'transporte', 'inversion']


database_arriendo = []
database_transporte = []
database_servicios = []
database_ocio = []



def save_egresos(egreso_in_db: EgresoInDB):
    if egreso_in_db.tipo == "arriendo":
      database_arriendo.append(egreso_in_db)  
    elif egreso_in_db.tipo == "transporte":
      database_transporte.append((egreso_in_db))
    elif egreso_in_db.tipo == "servicios":
      database_servicios.append((egreso_in_db))
    elif egreso_in_db.tipo == "ocio":
      database_ocio.append((egreso_in_db))


def get_egresos(tipo: str):
    if tipo == "arriendo":
        return database_arriendo
    elif tipo == "transporte":
        return database_transporte
    elif tipo == "servicios":
        return database_servicios
    elif tipo == "ocio":
        return database_ocio
    else:
        return None




print(database_arriendo)