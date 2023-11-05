import functools

from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)

from  werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db, c = get_db()

        error = None

        #Busca el id del username
        c.execute(
            "SELECT id FROM user WHERE username = %s", (username,)
        )
        

        if not username:
            error = "Username es requerido"
        if not password:
            error = "Password es requerido"
        elif c.fetchone() is not None:
            error = f"Usuario {username} se encuentra registrado."
        #Esta aca llega bien

        # if error is None:
        #     c.execute(
        #         'insert into user (username,password) values (%s, %s)',
        #         (username, generate_password_hash(password)),
        #     )
        #     db.commit()
        if error is None:
            print("TODO BIEN SUPREMO 1 ")
            c.execute(
                "INSERT INTO user (username, password) VALUES (%s, %s)",
                (username, generate_password_hash(password)),
            )
            print("TODO BIEN SUPREMO 2")
            db.commit()

            print("TODO BIEN SUPREMO 3")
            return redirect(url_for('auth.login'))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db, c = get_db()
        error = None

        c.execute(
            'select * from user where username = %s', (username)
        )

        user = c.fetchone()

        if user is None:
            error = 'Usuario y/o contraseña invalida.'
        elif not check_password_hash(user['password'], password):
            error = 'Usuario y/o contraseña invalida.'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')