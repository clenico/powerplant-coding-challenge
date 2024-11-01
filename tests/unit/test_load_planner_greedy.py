import unittest
import json
from app.controller.load_planner import LoadPlannerGreedy
from app.utils.parser import ApiProductionPlanPayloadParser
from app.utils.merit_manager import MeritSortManager, CostComputer
from tests.const import PATH_PAYLOAD_3, PATH_RESPONSE_3
from app.controller.load_planner import LoadPlannerGreedy

class TestLoadPlannerGreedy(unittest.TestCase):
    def setUp(self):
        self.planner = LoadPlannerGreedy()

    def tearDown(self):
        del self.planner

    def test_load_planner_example_3(self):
        parser = ApiProductionPlanPayloadParser()
        with open(PATH_PAYLOAD_3, "r") as reader:
            payload = json.load(reader)
        expected_load_production_plan = None
        with open(PATH_RESPONSE_3, "r") as reader:
            expected_load_production_plan = json.load(reader)
        api_production_payload = parser.parse(payload)
        total_load = api_production_payload.load
        sorted_pairs_pp = MeritSortManager().sort_by_lower_cost_per_MWh(api_production_payload)
        sorted_powerplants = [e[1] for e in sorted_pairs_pp]
        load_production_plan = self.planner.plan(total_load, sorted_powerplants)
        serialized_lpp = [e.model_dump() for e in load_production_plan]
        self.assertEqual(serialized_lpp, expected_load_production_plan)
