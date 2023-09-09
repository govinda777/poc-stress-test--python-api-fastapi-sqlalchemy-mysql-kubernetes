from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
