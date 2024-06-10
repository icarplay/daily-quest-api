from daily_quest_api.entities import User
from pymongo.database import Database
from bson import ObjectId
from bson import decode, encode

class UserService:

    def get_all(self, db: Database):
        results = db.users.find()
        return {
            'message': 'Get all users with success',
            'data': results
        }

    def get_by_id(self, _id: str, db: Database):
        results = db.users.find_one({ '_id': ObjectId(_id) })
        return {
            'message': 'Get user by id with success',
            'data': results
        }

    def get_by_email(self, email: str, db: Database):
        results = db.users.find_one({ 'email': email })
        return results

    def create(self, name: str, email: str, password: str, db: Database):

        is_valid_fields = self._validate_fields(name, email, password)

        if (not is_valid_fields is None):
            return {
                'message': is_valid_fields,
                'data': {}
            }

        is_valid_email = self.get_by_email(email=email, db=db)

        if (not is_valid_email is None):
            return {
                'message': 'Invalid e-mail',
                'data': {}
            }

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

        return {
            'message': 'User created',
            'data': obj
        }
    
    def _validate_fields(self, name: str, email: str, password: str):

        if (len(name) <= 0):
            return 'Invalid name'
        
        if (len(password) <= 6):
            return 'Invalid password'
        
        if (not '@' in email and len(email) <= 5):
            return 'Invalid e-mail'
        
        return None