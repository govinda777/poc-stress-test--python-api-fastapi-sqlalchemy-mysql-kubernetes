# user_controller.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from user_service import UserService
from user import User

class UserController:
    router = APIRouter()

    def __init__(self, service: UserService):
        self.service = service  # Aqui você pode inicializar o serviço. Se estiver usando injeção de dependência, pode ajustar isso.

    @router.post("/users/", response_model=User)
    def create_user(self, user: User):
        return self.service.create_user(user)

    @router.get("/users/", response_model=List[User])
    def read_users(self, skip: int = 0, limit: int = 10):
        return self.service.get_users(skip=skip, limit=limit)

    @router.get("/users/{user_id}", response_model=User)
    def read_user(self, user_id: int):
        db_user = self.service.get_user(user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    @router.put("/users/{user_id}", response_model=User)
    def update_user(self, user_id: int, user: User):
        return self.service.update_user(user_id, user)

    @router.delete("/users/{user_id}", response_model=User)
    def delete_user(self, user_id: int):
        return self.service.delete_user(user_id)

# Para usar o roteador em seu aplicativo principal:
# user_controller_instance = UserController()
# app.include_router(UserController.router)
