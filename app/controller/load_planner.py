from typing import List
from app.schemas import PowerplantData, ProductionPlanPayload

class LoadPlannerGreedy():
    def __init__(self):
        pass

    def plan(self, load: float, powerplants: List[PowerplantData])\
        -> List[ProductionPlanPayload]:
            return []