from pydantic import BaseModel
from datetime import date
from typing import List

class EgresoIn(BaseModel):
    tipo: str
    valor: int
    fecha: date

class EgresoOut(BaseModel):
    tipo: str
    valor: int
    fecha:date

