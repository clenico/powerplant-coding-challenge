from typing import Dict, List
from app.schemas import FuelsCost, PowerplantData, ProductionPlanningData
from app.utils.merit_manager import AbstractCostComputer, CostComputer

class LoadPlanCostCalculator():

    def __init__(self,
                 fuels_cost: FuelsCost,
                 cost_computer: AbstractCostComputer = CostComputer()):
        self._cost_computer = cost_computer
        self.fuels_cost = fuels_cost

    def calculate(self,
                  powerplants: List[PowerplantData],
                  load_plan: List[ProductionPlanningData]) -> float:
        dict_name_pp = {pp.name:pp for pp in powerplants}
        total_cost = 0
        for load_plan_per_pp in load_plan:
            # TODO cost per MWh should be computed once and result passed via param
            cost_per_MWh = self._cost_computer.compute(pp=dict_name_pp[load_plan_per_pp.name],
                                                       fuels_cost=self.fuels_cost)
            total_cost += load_plan_per_pp.p * cost_per_MWh
        return total_cost




