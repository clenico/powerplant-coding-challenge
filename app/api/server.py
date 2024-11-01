from fastapi import APIRouter, FastAPI, HTTPException, status

import uvicorn
from app.controller.load_planner import LoadPlannerGreedy
from app.utils.parser import ApiProductionPlanPayloadParser
from app.utils.merit_manager import MeritSortManager

class ApiServer():
    def __init__(self):
        self.server = FastAPI()
        router = self.build_router()
        self.server.include_router(router)
        self.server

    def run(self, host:str = "0.0.0.0",
                  port: int = 8888):
        uvicorn.run(self.server, port=port, host=host)

    def build_router(self):
        router = APIRouter()

        @router.post("/productionplan")
        def plan_production(payload: dict):
            # TODO should encapsulate this logic
            parser = ApiProductionPlanPayloadParser()
            merit_sorter = MeritSortManager()
            planner = LoadPlannerGreedy()
            pp_data = parser.parse(payload)
            sorted_pairs_pp = merit_sorter.sort_by_lower_cost_per_MWh(pp_data)
            sorted_powerplants = [e[1] for e in sorted_pairs_pp]
            load_production_plan = planner.plan(pp_data.load, sorted_powerplants)
            if len(load_production_plan) == 0:
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    detail="No satisfying load plan could be found")
            serialized_lpp = [e.model_dump() for e in load_production_plan]
            return serialized_lpp

        return router
