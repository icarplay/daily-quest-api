from daily_quest_api.entities import User

class UserService:

    def get_by_id(self, id, db):
        return db.query(User).filter(User.id == id).one()
    
    def create(self, name: str, email: str, password: str, db):
        new_user = User(
            name=name,
            email=email,
            hashed_password=password + "notreallyhashed",
            is_active=True
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user