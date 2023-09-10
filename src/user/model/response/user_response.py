from dataclasses import dataclass

@dataclass
class UserResponse:
    id: int
    first_name: str
    last_name: str
    email: str
    age: int
    created_at: str

