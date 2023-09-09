
# user_not_found_exception.py

class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.message = f"User with ID {self.user_id} not found."
        super().__init__(self.message)
