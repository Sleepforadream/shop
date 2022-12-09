from flask import request, redirect, url_for, render_template
from flask_login import login_user
from werkzeug.security import check_password_hash

from app import db, Authorization, app


@app.route('/login', methods=['POST', 'GET'])
def login2():
    if request.method == "POST":
        email = request.form['floatingInput']
        password = request.form['floatingPassword']
        remember = request.form.get('rememberme')

        if remember is not None:
            remember = True
        else:
            remember = False

        users = Authorization.query.order_by(Authorization.date.desc()).all()

        for user in users:
            if user.email == email:
                if check_password_hash(user.password, password):
                    user = db.session.query(Authorization).filter(Authorization.email == email).first()
                    login_user(user, remember=remember)
                    return redirect(url_for('admin_panel'))
                else:
                    return "Пароль введён не верно"
        return "Такой электронной почты не было зарегистрировано"
    return render_template("login.html")

print(login_user)

if __name__ == '__main__':
    login2()