from pydantic import BaseModel
from typing import List
from enum import Enum

class PowerplantType(Enum):
    GASFIRED = "gasfired"
    TURBOJET = "turbojet"
    WINDTURBINE = "windturbine"


class FuelsPricePayload(BaseModel):
    gas: float
    kerosine: float
    co2: float
    wind: float


class PowerplantData(BaseModel):
    name: str
    type: PowerplantType
    efficiency: float
    pmax: float
    pmin: float

class ApiProductionPlanPayload(BaseModel):
    load: str
    fuels: FuelsPricePayload
    powerplants: List[PowerplantData]

class PowerplantLoadPayload(BaseModel):
    name: str
    p: float
