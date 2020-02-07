from .db import db

# Create a class for all table that should be in the database


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    username = db.StringField(required=True, unique=True)
    fname = db.StringField(required=True)
    lname = db.StringField()
    password = db.StringField(required=True)
    pictures = db.ListField(db.ReferenceField(
        'Picture'), reverse_delete_rule=db.PULL)
    nb_followers = db.IntField()
    followers = db.ListField(db.StringField())
    nb_following = db.IntField()
    following = db.ListField(db.StringField())
    image_queue = db.ListField(db.ReferenceField(
        'Picture'), reverse_delete_rule=db.PULL)


class Comment(db.Document):
    user_id = db.StringField()
    message = db.StringField()
    added_picture = db.ReferenceField('Picture')


class Picture(db.Document):
    date = db.DateTimeField(required=True)
    owner = db.StringField()
    user = db.ReferenceField('User')
    link = db.URLField()
    nb_likes = db.IntField()
    nb_comments = db.IntField()
    comments = db.ListField(db.ReferenceField(
        'Comment', reverse_delete_rule=db.PULL))


Picture.register_delete_rule(Comment, 'added_picture', db.CASCADE)
User.register_delete_rule(Picture, 'user', db.CASCADE)
