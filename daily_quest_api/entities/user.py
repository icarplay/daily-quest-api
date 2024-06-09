from pydantic import BaseModel
from typing import Optional

class User(BaseModel):

    _id: Optional[str]
    name: str
    email: str
    hashed_password: str
    is_active: bool

    
    def to_json(self, contains_id=False):
        cls_dict = {
            'name' : self.name,
            'email' : self.email,
            'hashed_password' : self.hashed_password,
            'is_active' : self.is_active
        }

        if contains_id:
            cls_dict['_id'] = self._id
        
        return cls_dict
    
class UserResponse(User):

    def __init__(self, **pydict):
        super(UserResponse, self).__init__(**pydict)