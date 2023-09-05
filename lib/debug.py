
#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    # Create an SQLAlchemy engine and session
    engine = create_engine('sqlite:///seed_db.db')  # Replace with your database URL
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Seeding games...")

    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for i in range(50)
    ]

    session.bulk_save_objects(games)
    session.commit()

    print("Seed data added successfully.")
