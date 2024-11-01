from typing import List
from app.schemas import PowerplantData, ProductionPlanningData

class LoadPlannerGreedy():
    def __init__(self):
        pass

    def plan(self, load: float, powerplants: List[PowerplantData])\
        -> List[ProductionPlanningData]:
            total_load = load
            remaining_load = total_load
            production_plan = []
            for pp in powerplants:
                if remaining_load == 0:
                    production_plan.append(ProductionPlanningData(
                        name=pp.name,
                        p=0
                    ))
                elif pp.pmin < remaining_load < pp.pmax:
                    production_plan.append(ProductionPlanningData(
                        name=pp.name,
                        p=remaining_load
                    ))
                    remaining_load = 0
                elif pp.pmin > remaining_load:
                    continue
                elif remaining_load > pp.pmax:
                    production_plan.append(ProductionPlanningData(
                        name=pp.name,
                        p=pp.pmax
                    ))
                    remaining_load -= pp.pmax
            return production_plan