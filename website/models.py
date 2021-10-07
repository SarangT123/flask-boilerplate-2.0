from re import I
from website import db
from datetime import datetime

DEFUALT_PROFILE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq39FYyBUpx-nUtHV7LPN-H31ER5zzNMW6KycDj0jK9GUw_v-R9tMDiunchfmCZMDyev8&usqp=CAU"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_picture = db.Column(db.String(20), nullable=False,
                                default=DEFUALT_PROFILE)
    password = db.Column(db.String(60), nullable=False)
    creation_date = db.Column(
        db.DateTime(), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_picture},'{self.creation_date}')"
