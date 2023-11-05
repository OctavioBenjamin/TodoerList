import os
from flask import Flask

def get_info():
    print("Host:")
    print(os.environ.get('FLASK_DATABASE_HOST'))
    print("User:")
    print(os.environ.get('FLASK_DATABASE_USER'))
    print("Passwd:")
    print(os.environ.get('FLASK_DATABASE_PASSWORD'))
    print("DB:")
    print(os.environ.get('FLASK_DATABASE'))


def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
        SECRET_KEY="mikey",
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    import db

    db.init_app(app)

    import auth
    app.register_blueprint(auth.bp)

    #Se debe configurar cada vez que se apage el pc?
    print("Host: " + str(os.environ.get('FLASK_DATABASE_HOST')))
    print("User: " + str(os.environ.get('FLASK_DATABASE_USER')))
    print("Passwd: " + str(os.environ.get('FLASK_DATABASE_PASSWORD')))
    print("DB: " + str(os.environ.get('FLASK_DATABASE')))


    @app.route('/hola')
    def hola():
        return "Hola mundo"
    
    return app
