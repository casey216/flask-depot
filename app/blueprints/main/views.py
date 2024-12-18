from flask import render_template, Blueprint
from flask_login import login_required, current_user
main = Blueprint('main', __name__)

@login_required
@main.route("/")
def index():
    return f"This is {current_user}"