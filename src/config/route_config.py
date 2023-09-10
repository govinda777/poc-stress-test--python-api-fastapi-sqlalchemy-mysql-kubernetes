# route_config.py

from fastapi import FastAPI
from .user.user_controller import UserController

class RouteConfig:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        user_controller = UserController()
        self.app.include_router(user_controller.router, prefix="/users", tags=["users"])
        # Adicione outros controllers conforme necessário
