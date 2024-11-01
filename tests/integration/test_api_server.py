import unittest
from app.api.server import ApiServer
from tests.const import PATH_PAYLOAD_3, PATH_RESPONSE_3
import json
from fastapi.testclient import TestClient

class TestAPIServer(unittest.TestCase):
    def setUp(self):
        app = ApiServer()
        # This is your fixture setup
        self.client = TestClient(app.server)

    def tearDown(self):
        del self.client

    def test_example_3_payload_response(self):
        payload = None
        with open(PATH_PAYLOAD_3, "r") as reader:
            payload = json.load(reader)
        expected_response: dict = None
        with open(PATH_RESPONSE_3, "r") as reader:
            expected_response = json.load(reader)
        response = self.client.post("/productionplan",
                                    json=payload)
        # TODO add message for assert
        self.assertEqual(response.json(), expected_response)