from flask import Blueprint, flash, render_template, redirect, url_for, request
from application.models import User
from application.register.forms import *
from database.setup import Base, sessionmaker, engine, db_session
from flask_login import login_user, login_required

registeration_blueprint = Blueprint('register',
                              __name__,
                              template_folder='templates')

@registeration_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('register.welcome_user')
            return redirect(next)
    return render_template('login.html', form=form)


@registeration_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        gender_ = ''
        if form.gender.data == 'on':
            gender_ = 'male'
        else:
            gender_ = 'female'
        user = User(email=form.email.data,
                    firstname=form.first_name.data,
                    lastname=form.last_name.data,
                    address=form.address.data,
                    number=form.number.data,
                    gender=gender_,
                    password=form.password.data)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(user)
        session.commit()
        db_session.close()
        flash('You are successfully Registered......!')
        return redirect(url_for('register.login'))
    return render_template('index.html', form=form)

@registeration_blueprint.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')



