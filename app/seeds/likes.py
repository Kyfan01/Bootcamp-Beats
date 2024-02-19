# from app.models import db, Like, environment, SCHEMA
# from sqlalchemy.sql import text

# def seed_likes():
#     likes = [
#         Like(user_id = 3 , track_id = 1),
#         Like(user_id = 3 , track_id = 2),
#         Like(user_id = 3 , track_id = 3),
#         Like(user_id = 3 , track_id = 4),
#         Like(user_id = 3 , track_id = 5),
#         Like(user_id = 3 , track_id = 6),
#         Like(user_id = 3 , track_id = 7),
#         Like(user_id = 3 , track_id = 8),
#         Like(user_id = 2 , track_id = 1),
#         Like(user_id = 1 , track_id = 1)
#     ]

#     db.session.add_all(likes)
#     db.session.commit()

# def undo_likes():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.likes RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM likes"))

#     db.session.commit()
