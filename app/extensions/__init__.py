from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'



@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(user_id)
