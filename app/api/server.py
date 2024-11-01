from fastapi import APIRouter, FastAPI
import uvicorn

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
            return []
        return router
