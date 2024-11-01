import unittest
from app.controller.load_planner import LoadPlannerGreedy
from app.utils.parser import ApiProductionPlanPayloadParser
from app.utils.merit_manager import MeritSortManager, CostComputer
import json
from app.schemas import (
    ApiProductionPlanPayload,
    FuelsCost,
    PowerplantData,
    PowerplantType,
)
from app.controller.load_planner import LoadPlannerGreedy
class TestLoadPlannerGreedy(unittest.TestCase):
    def setUp(self):
        self.planner = LoadPlannerGreedy()

    def tearDown(self):
        del self.planner

    def test_load_planner_example_3(self):
        parser = ApiProductionPlanPayloadParser()
        path_payload_example = "powerplant-coding-challenge/tests/example_payloads/payload3.json"
        with open(path_payload_example, "r") as reader:
            payload = json.load(reader)
        path_response_example = "powerplant-coding-challenge/tests/example_payloads/response3.json"
        expected_load_production_plan = None
        with open(path_response_example, "r") as reader:
            expected_load_production_plan = json.load(reader)
        api_production_payload = parser.parse(payload)
        total_load = api_production_payload.load
        sorted_pairs_pp = MeritSortManager().sort_by_lower_cost_per_MWh(api_production_payload)
        sorted_powerplants = [e[1] for e in sorted_pairs_pp]
        load_production_plan = self.planner.plan(total_load, sorted_powerplants)
        serialized_lpp = [e.model_dump() for e in load_production_plan]
        self.assertEqual(serialized_lpp, expected_load_production_plan)
