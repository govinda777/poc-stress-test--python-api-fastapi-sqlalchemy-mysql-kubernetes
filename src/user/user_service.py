# user_service.py

from model.request.user_create_request import UserCreateRequest
from model.request.user_delete_request import UserDeleteRequest
from model.request.user_update_request import UserUpdateRequest
from model.response.user_response import UserResponse
from model.user_mapper import UserMapper
from user_repository import UserRepository
from exception.user_not_found_exception import UserNotFoundException

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, request: UserCreateRequest) -> UserResponse:
        user = UserMapper(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            age=request.age
        )
        self.repository.add(user)
        return UserResponse(id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email, age=user.age)

    def update_user(self, request: UserUpdateRequest) -> UserResponse:
        user = self.repository.get_by_id(request.id)
        
        user.first_name = request.first_name
        user.last_name = request.last_name
        user.email = request.email
        user.age = request.age
        self.repository.update(user)
        
        return UserResponse(id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email, age=user.age)

    def delete_user(self, request: UserDeleteRequest):
        user = self.repository.get_by_id(request.id)
        self.repository.delete(user)

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.repository.get_by_id(user_id)
        return UserResponse(id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email, age=user.age)
