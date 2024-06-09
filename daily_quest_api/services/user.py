from daily_quest_api.entities import User
from pymongo.database import Database
from bson import ObjectId
from bson import decode, encode

class UserService:

    def get_all(self, db: Database):
        results = db.users.find()
        return results

    def get_by_id(self, _id: str, db: Database):
        results = db.users.find_one({ '_id': ObjectId(_id) })
        return results
    
    def create(self, name: str, email: str, password: str, db: Database):
        new_user = User(
            id=str(ObjectId()),
            name=name,
            email=email,
            hashed_password=password + "notreallyhashed",
            is_active=True
        )

        obj = new_user.to_mongo(contains_id=True)

        inserted = db.users.insert_one(obj)

        obj['_id'] = str(inserted.inserted_id)

        return obj