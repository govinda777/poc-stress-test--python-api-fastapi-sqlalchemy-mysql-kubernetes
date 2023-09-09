# user_repository.py

from model.user_mapper import UserMapper
from exception.user_not_found_exception import UserNotFoundException
from infrastructure.database import Database

class UserRepository:
    def __init__(self, database: Database):
        self.database = database

    def add(self, user: UserCreateRequest):
        self.database.add(user)
        
    def update(self, user: UserUpdateRequest):
        self.database.update(user)
        
    def delete(self, user: UserMapper):
        self.database.delete(user)

    def get_by_id(self, user_id: int) -> UserMapper:
        user = self.database.query(UserMapper).filter_by(id=user_id).first()
        if not user:
            raise UserNotFoundException(user_id)
        return user
