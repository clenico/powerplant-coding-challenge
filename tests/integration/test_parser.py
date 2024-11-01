import unittest
from app.api.server import ApiServer
import json
from fastapi.testclient import TestClient

class TestApiParser(unittest.TestCase):
    def setUp(self):
        app = ApiServer()
        # This is your fixture setup
        self.client = TestClient(app.server)

    def tearDown(self):
        del self.client

    def test_example_3_payload_response(self):
        payload = None
        path_payload_example = "powerplant-coding-challenge/tests/example_payloads/payload3.json"
        with open(path_payload_example, "r") as reader:
            payload = json.load(reader)
        expected_response: dict = None
        path_response_example = "powerplant-coding-challenge/tests/example_payloads/response3.json"
        with open(path_response_example, "r") as reader:
            expected_response = json.load(reader)
        response = self.client.post("/productionplan",
                                    json=payload)
        # TODO add message for assert
        self.assertEqual(response.json(), expected_response)