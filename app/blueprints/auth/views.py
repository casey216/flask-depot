from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect, url_for, flash, abort, Blueprint
from .forms import LoginForm, UserRegisterForm, CustomerRegisterForm, VendorRegisterForm, DriverRegisterForm
from app.extensions import db
from app.models import User, Person, Customer, Vendor, Driver

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password, form.password.data):
            flash('Invalid username or password', category='error')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        flash('Login Successful', category='success')
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Login', form=form)

@login_required
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/')


@login_required
@auth.route('/register/<role>', methods=['GET', 'POST'])
def register(role):
    roles = {
        'user': {'form': UserRegisterForm(), 'model': User},
        'customer': {'form': CustomerRegisterForm(), 'model': Customer},
        'vendor': {'form': VendorRegisterForm(), 'model': Vendor},
        'driver': {'form': DriverRegisterForm(), 'model': Driver}
    }

    role = roles.get(role)
    if not role:
        abort(404)
    
    form = role['form']
    model = role['model']

    if form.validate_on_submit():
        person = Person(
            firstname = form.firstname.data,
            lastname = form.lastname.data,
            email = form.email.data,
            phone = form.phone.data
        )
        db.session.add(person)
        db.session.flush()

        role = model(
            username = form.username.data,
            password = generate_password_hash(form.password.data),
            person_id = person.id
        )
        db.session.add(role)
        db.session.flush()
        db.session.commit()
    return render_template('auth/register.html', title='Register', form=form, role=role)

auth.route('/')
def auth_home():
    return "This is home"