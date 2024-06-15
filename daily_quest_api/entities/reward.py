from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime

class Reward(BaseModel):

    id: Optional[str]
    name: str
    description: str
    icon: str
    requirements: dict


    def to_mongo(self, contains_id=False):
        cls_dict = {
            'name' : self.name,
            'description' : self.description,
            'icon' : self.icon,
            'requirements' : self.requirements
        }

        if contains_id:
            cls_dict['_id'] = ObjectId(self.id)
        
        return cls_dict
    
    def to_json(self, contains_id=False):
        cls_dict = {
            'name' : self.name,
            'description' : self.description,
            'icon' : self.icon,
            'requirements' : self.requirements
        }

        if contains_id:
            cls_dict['id'] = self.id
        
        return cls_dict
    
class RewardResponse(Reward):

    def __init__(self, **pydict):
        if '_id' in pydict:
            pydict['id'] = str(pydict['_id'])
        super(RewardResponse, self).__init__(**pydict)