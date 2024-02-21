from models.user_model import UserModel
from schema.user_schema import User

class UserService():
    
    def __init__(self, db) -> None:
        self.db = db

    def create_user(self, user: User):
        new_user = UserModel(**user.model_dump())
        print(new_user)
        self.db.add(new_user)
        self.db.commit()
        return
    
    def get_user_by_email(self, email):
        result = self.db.query(UserModel).filter(UserModel.email == email).first()
        return result