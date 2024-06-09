from daily_quest_api.entities import User
from pymongo.database import Database
from bson import ObjectId
from bson import decode, encode

class UserService:

    def get_by_id(self, _id: str, db: Database):
        results = db.users.find_one({ '_id': ObjectId(_id) })
        return results
    
    def create(self, name: str, email: str, password: str, db: Database):
        new_user = User(
            _id='',
            name=name,
            email=email,
            hashed_password=password + "notreallyhashed",
            is_active=True
        )

        obj = new_user.to_json(contains_id=False)

        inserted = db.users.insert_one(obj)

        new_user._id = inserted.inserted_id

        return new_user.to_json()