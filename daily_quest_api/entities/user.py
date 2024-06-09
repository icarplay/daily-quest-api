from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class User(BaseModel):

    id: Optional[str]
    name: str
    email: str
    hashed_password: str
    is_active: bool

    
    def to_mongo(self, contains_id=False):
        cls_dict = {
            'name' : self.name,
            'email' : self.email,
            'hashed_password' : self.hashed_password,
            'is_active' : self.is_active
        }

        if contains_id:
            cls_dict['_id'] = ObjectId(self.id)
        
        return cls_dict
    
    def to_json(self, contains_id=False):
        cls_dict = {
            'name' : self.name,
            'email' : self.email,
            'hashed_password' : self.hashed_password,
            'is_active' : self.is_active
        }

        if contains_id:
            cls_dict['id'] = self.id
        
        return cls_dict
    
class UserResponse(User):

    def __init__(self, **pydict):
        if '_id' in pydict:
            pydict['id'] = str(pydict['_id'])
        super(UserResponse, self).__init__(**pydict)