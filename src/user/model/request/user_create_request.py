# user_request.py
from dataclasses import dataclass

@dataclass
class UserCreateRequest:
    first_name: str
    last_name: str
    email: str
    age: int