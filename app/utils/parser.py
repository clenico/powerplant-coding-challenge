from app.schemas import (
    ApiProductionPlanPayload,
    FuelsCost,
    PowerplantData,
    PowerplantType,
)


class ApiProductionPlanPayloadParser:
    def __init__(self):
        pass

    def validate(self, payload):
        # TODO make validation of payload format
        pass

    def parse_powerplant(self, powerplant: dict) -> PowerplantData:
        # TODO add validate before parsing
        data = PowerplantData(
            name=powerplant["name"],
            type=PowerplantType(powerplant["type"]),
            efficiency=powerplant["efficiency"],
            pmax=powerplant["pmax"],
            pmin=powerplant["pmin"],
        )
        return data

    def parse(self, payload: dict) -> ApiProductionPlanPayload:
        self.validate(payload=payload)
        load: float = payload["load"]
        wind_coefficient = payload["fuels"]["wind(%)"]
        fuels_cost = FuelsCost(
            co2=payload["fuels"]["wind(%)"],
            kerosine=payload["fuels"]["kerosine(euro/MWh)"],
            gas=payload["fuels"]["co2(euro/ton)"],
        )
        powerplants = [self.parse_powerplant(e) for e in payload["powerplants"]]
        for powerplant in powerplants:
            if powerplant.type == PowerplantType.WINDTURBINE:
                powerplant.pmax *= wind_coefficient
        return ApiProductionPlanPayload(
            load=load, fuels_cost=fuels_cost, powerplants=powerplants
        )

        pass
