from typing import List, Tuple

from app.schemas import (ApiProductionPlanPayload,
                         PowerplantType, FuelsCost,
                         PowerplantData)
from abc import ABC, abstractmethod

class AbstractCostComputer(ABC):
    @abstractmethod
    def compute(self, pp: PowerplantData) -> float:
        pass

class CostComputer(AbstractCostComputer):
    def compute(self, pp: PowerplantData, fuels_cost: FuelsCost):
        # TODO implement testing
        cost = None
        if pp.type == PowerplantType.GASFIRED :
            cost = fuels_cost.gas / pp.efficiency
        elif pp.type == PowerplantType.TURBOJET:
            cost = fuels_cost.kerosine / pp.efficiency
        elif pp.type == PowerplantType.WINDTURBINE:
            cost = 0
        else:
            raise NotImplementedError()
        return cost

class MeritSortManager():
    def __init__(self, cost_computer: AbstractCostComputer):
        self.cc = cost_computer

    def sort_by_lower_cost_per_MWh(self, payload: ApiProductionPlanPayload)\
        -> List[Tuple[float, PowerplantData]]:
        # TODO implement testing
        pairs_cost_pp: list = []
        for pp in payload.powerplants:
            pairs_cost_pp.append((self.cc.compute(pp), pp))
        sorted_pairs = sorted(pairs_cost_pp, key= lambda e: e[0])
        return sorted_pairs
