from pydantic import BaseModel
from typing import List
from enum import Enum


class PowerplantType(Enum):
    GASFIRED = "gasfired"
    TURBOJET = "turbojet"
    WINDTURBINE = "windturbine"


class FuelsCost(BaseModel):
    gas: float
    kerosine: float
    co2: float


class PowerplantData(BaseModel):
    name: str
    type: PowerplantType
    efficiency: float
    pmax: float
    pmin: float


class ApiProductionPlanPayload(BaseModel):
    load: float
    fuels_cost: FuelsCost
    powerplants: List[PowerplantData]


class PowerplantLoadPayload(BaseModel):
    name: str
    p: float
