import unittest
from app.utils.parser import ApiProductionPlanPayloadParser
import json
from app.schemas import (
    ApiProductionPlanPayload,
    FuelsCost,
    PowerplantData,
    PowerplantType,
)

class TestApiParser(unittest.TestCase):
    def test_parse_example_3_raise_no_error(self):
        example_payload = None
        path_payload_example_3 = "powerplant-coding-challenge/tests/example_payloads/payload3.json"
        with open(path_payload_example_3, "r") as reader:
            example_payload = json.load(reader)
        parser = ApiProductionPlanPayloadParser()
        production_plan_payload = parser.parse(example_payload)
        print(production_plan_payload)
        self.assertTrue(True)

    def test_parse_powerplant_have_correct_values(self):
        dummy_pp_payload = {"name": "gasfiredbig1",
                            "type": "gasfired",
                            "efficiency": 0.53,
                            "pmin": 100,
                            "pmax": 460}
        parser = ApiProductionPlanPayloadParser()
        expected_value = PowerplantData(name="gasfiredbig1",
                                        type=PowerplantType.GASFIRED,
                                        efficiency=0.53,
                                        pmin=100,
                                        pmax=460)
        parsed_powerplant = parser.parse_powerplant(dummy_pp_payload)
        self.assertEqual(parsed_powerplant, expected_value)

    def test_parse_example_3_have_correct_values(self):
        #TODO
        pass


