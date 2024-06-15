from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime

class Quest(BaseModel):

    id: Optional[str]
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    expires_at: datetime

    
    def to_mongo(self, contains_id=False):
        cls_dict = {
            'name' : self.name,
            'description' : self.description,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'expires_at': self.expires_at
        }

        if contains_id:
            cls_dict['_id'] = ObjectId(self.id)
        
        return cls_dict
    
    def to_json(self, contains_id=False):
        cls_dict = {
            'name' : self.name,
            'description' : self.description,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'expires_at': self.expires_at
        }

        if contains_id:
            cls_dict['id'] = self.id
        
        return cls_dict
    
class QuestResponse(Quest):

    def __init__(self, **pydict):
        if '_id' in pydict:
            pydict['id'] = str(pydict['_id'])
        super(QuestResponse, self).__init__(**pydict)