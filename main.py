import fastapi
from db.ingreso_db import IngresoInDB
from db.ingreso_db import save_ingresos, get_ingresos
from db.egreso_db import EgresoInDB, save_egresos, get_egresos
from models.ingreso import IngresoIn, IngresoOut
from models.egreso import EgresoIn, EgresoOut
from typing import List
import json

from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://desafio6-frontend.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.put("/user/ingresos/")
async def make_ingreso(ingreso: IngresoIn):
    ingreso_in_db = IngresoInDB(**ingreso.dict())
    ingreso_in_db = save_ingresos(ingreso_in_db)
    salida =  IngresoOut(**ingreso_in_db.dict())
    return salida


@api.get("/user/ingresos/{tipo_ingreso}")
async def get_ingresos_main(tipo_ingreso: str):
    ingreso_in_db = get_ingresos(tipo_ingreso)
    if ingreso_in_db == None:
        raise HTTPException(status_code=404,
                            detail= "El tipo ingreso no existe")
    ingreso_out = IngresoOut(**ingreso_in_db.dict())
    return ingreso_out

@api.put("/user/egresos/")
async def make_egreso(egreso: EgresoIn):
    egreso_in_db = EgresoInDB(**egreso.dict())
    egreso_in_db = save_egresos(egreso_in_db)
    salida = EgresoOut(**egreso_in_db.dict())
    return salida

@api.get("/user/egresos/{tipo_egreso}", response_model=List)
async def get_egresos_main(tipo_egreso: str):
    egreso_in_db = get_egresos(tipo_egreso)
    if egreso_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El tipo de egreso no existe")
    egreso_out = EgresoList(**EgresoOut(**egreso_in_db.dict()))

    return egreso_out
