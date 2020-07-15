from database.db import db

#criação do documento de banco de dados
class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    atores = db.ListField(db.StringField(), required=True)
    genero = db.ListField(db.StringField(), required=True)
    
