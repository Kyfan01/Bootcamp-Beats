from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


hun = User(
        name='Hun Choi', username='myunghun0721', email='hunchoi@aa.io', password='password',artist_name='Tetnim', date_of_birth=date(1998, 12, 4))
kevin = User(
        name='Kevin Fan', username='kyfn', email='kyfn@aa.io', password='password', artist_name='Kay-Z', date_of_birth=date(1997, 12, 4))
collin = User(
        name='Collin Ullmann', username='collinullmann', email='collinullmann@aa.io', password='password', artist_name='DJ-bytebeat', date_of_birth=date(1943, 12, 4))


# Adds a demo user, you can add other users here if you want
def seed_users():
    # hun = User(
    #     name='Hun Choi', username='myunghun0721', email='hunchoi@aa.io', password='password',artist_name='Tetnim', date_of_birth=date(1998, 12, 4))
    # kevin = User(
    #     name='Kevin Fan', username='kyfn', email='kyfn@aa.io', password='password', artist_name='Kay-Z', date_of_birth=date(1997, 12, 4))
    # collin = User(
    #     name='Collin Ullmann', username='collinullmann', email='collinullmann@aa.io', password='password', artist_name='DJ-bytebeat', date_of_birth=date(1943, 12, 4))
    demo = User(
        name='Demo User', username='demo', email='demo@aa.io', password='password', artist_name='DJ-Demo', date_of_birth=date(1000, 12, 4))

    db.session.add(hun)
    db.session.add(kevin)
    db.session.add(collin)
    db.session.add(demo)
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
