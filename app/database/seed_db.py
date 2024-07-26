from faker import Faker
from werkzeug.security import generate_password_hash
from app.database.users import Users
from app.extensions import db
from app.core import logger
import json, random


fake = Faker(locale="en_CA")
roles = ["admin", "user", "compliance"]

def generate_seed_data() -> list[dict[str]]:
    seed_users = []
    for _ in range(10):
        user_pwd = fake.password()
        seed_users.append(
            {
                "name": fake.name(),
                "email": fake.ascii_safe_email(),
                "phone_number": fake.phone_number(),
                "password": generate_password_hash(user_pwd),
                "password_text": user_pwd,
                "address": fake.address(),
                "role": random.choice(roles),
                "is_verified": False,
            }
        )
    
    return seed_users


def create_user_instances(users: dict[str]) -> list[Users]:
    demo_users = []
    for user in users:
        user.pop("password_text")
        demo_users.append(Users(**user))

    return demo_users


def run() -> None:
    if int(db.session.query(Users).count()) > 0:
        # print(">>> DB Not Empty")
        return None
     
    # print(">>> Generating seed data")
    data = generate_seed_data()

    # print(">>> saving seed data to file")
    with open("seed_user.json", "w") as file:
        json.dump(data, file, indent=4)
        
    cleaned_data = create_user_instances(data)

    # print(">>> Seeding database with generated data")
    db.session.add_all(cleaned_data)
    db.session.commit()
    # print(">>> DB seediing complete")