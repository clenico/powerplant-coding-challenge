from typing import List
from app.schemas import PowerplantData, ProductionPlanningData
from itertools import permutations
from abc import ABC, abstractmethod
from app.utils.plan_cost import LoadPlanCostCalculator

class AbstractLoadPlanner(ABC):

    @abstractmethod
    def plan(self, load: float, powerplants: List[PowerplantData])\
        -> List[ProductionPlanningData]:
        pass

class LoadPlannerGreedy(AbstractLoadPlanner):
    def __init__(self):
        pass

    def plan(self, load: float, powerplants: List[PowerplantData])\
        -> List[ProductionPlanningData]:
            # TODO load per powerplant should multiple of 0.1 MWh
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

class LoadPlannerBruteforce(AbstractLoadPlanner):
    def __init__(self, cost_evaluator: LoadPlanCostCalculator):
        self.cost_evaluator = cost_evaluator

    def gen_all_permutations_index(self, nb_elements):
        return permutations(range(nb_elements), nb_elements)

    def plan(self, load: float, powerplants: List[PowerplantData])\
        -> List[ProductionPlanningData]:
        best_plan = None
        best_cost = None
        for perm in self.gen_all_permutations_index(len(powerplants)):
            greedy_planner = LoadPlannerGreedy()
            permuted_powerplants = [powerplants[i] for i in perm]
            current_plan = greedy_planner.plan(load, permuted_powerplants)
            current_cost = self.cost_evaluator.calculate(powerplants=powerplants,
                                                         load_plan=current_plan)
            if best_plan is None or current_cost < best_cost:
                best_plan = current_plan
                best_cost = current_cost
        return best_plan

