from fastapi import FastAPI
from .config import Container
from config.route_config import RouteConfig

class main:
    container = Container()
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])

    app = FastAPI()

    RouteConfig(app)
