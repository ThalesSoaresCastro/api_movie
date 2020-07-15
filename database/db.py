from flask_mongoengine import MongoEngine

#criando o objeto de database e recebendo o app 
#para inicializar o banco de dados
db = MongoEngine()
def initialize_db(app):
    db.init_app(app)