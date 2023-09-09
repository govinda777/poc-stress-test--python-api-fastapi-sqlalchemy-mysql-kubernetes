# main.py
from fastapi import FastAPI, Depends
from .config import Container
from .user.user_service import UserService

container = Container()
container.init_resources()
container.wire(modules=[sys.modules[__name__]])

app = FastAPI()