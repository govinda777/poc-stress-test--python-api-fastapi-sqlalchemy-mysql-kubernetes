# user_request.py
from dataclasses import dataclass

@dataclass
class UserUpdateRequest:
    first_name: str
    last_name: str
    age: int