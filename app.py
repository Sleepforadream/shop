import os
import re
import shutil

from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'youmail@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'youmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    heading = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    imgpath = db.Column(db.String(300), nullable=True)
    author = db.Column(db.String(300),  nullable=False)
    private = db.Column(db.String(100))

    def __repr__(self):
        return '<Article %r>' % self.id


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Authorization).get(user_id)


class Authorization(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), unique=True, nullable=False)
    info = db.Column(db.String(1000), nullable=True)
    imgpath = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)

    def get_id(self):
        return Authorization.id

    def get_name(self):
        return Authorization.name


@app.route('/')
@app.route('/home')
def index():
    articles = Article.query.order_by(Article.date.desc()).all()
    if len(articles) > 1:
        articles_list = list()
        for article in articles:
            articles_list.append(article)
        article1 = articles_list[len(articles_list) - 1]
        article2 = articles_list[len(articles_list) - 2]

        uniquedates = set()
        for article in articles:
            date = article.date.strftime("%Y %B")
            uniquedates.add(date)
        monthsyears = sorted(uniquedates)
        return render_template("index.html", articles=articles, article1=article1, article2=article2,
                               monthsyears=monthsyears)
    else:
        return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/shop2')
def shop2():
    return render_template("shop2.html")

@app.route('/userLoginWindow')
def user_login_window():
    return render_template("userLoginWindow.html")

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    users = Authorization.query.order_by(Authorization.date.desc()).all()
    error = ""
    if request.method == "POST":

        name = request.form['floatingName']
        email = request.form['floatingInput']
        password = request.form['floatingPassword']
        password_double = request.form['floatingPassword2']

        pattern_password = re.compile(r'^(?=.*[0-9])(?=.*[!@#$%^&*_()=+?:;"`~/|,<>.-])(?=.*[a-z])(?=.*[A-Z])'
                                      r'[0-9a-zA-Z!@#$%^&*_()=+?:;"`~/|,<>.-]{8,}$')

        if name == "" or email == "" or password == "":
            error = "Были заполнены не все обязательные поля"
            return render_template("signup.html", error=error)

        if len(name) > 30 or len(email) > 256:
            error = "Слишком большое колличство символов в строке"
            return render_template("signup.html", error=error)
        is_password = bool(pattern_password.match(password))
        if not is_password:
            error = "Слабый пароль. Пароль должен состоять по крайней мере из восьми символов, содержать символы в " \
                    "верхнем и нижнем регистрах и включать по крайней мере одну цифру"
            return render_template("signup.html", error=error)

        if password != password_double:
            error = "Пароли не совпадают"
            return render_template("signup.html", error=error)

        for user in users:
            if user.email == email:
                error = "Такая почта уже была зарегистрирована"
                return render_template("signup.html", error=error)
            if user.name == name:
                error = "Пользователь с этим именем уже существует"
                return render_template("signup.html", error=error)

        password = generate_password_hash(password)

        authorization = Authorization(name=name, email=email, password=password)

        db.session.add(authorization)
        try:
            db.session.commit()
        except:
            return "При добавлении пользователя произошла ошибка"
        else:
            return render_template("login_success.html")
    else:
        return render_template("signup.html", error=error)


@app.route('/login_success')
def login_success():
    return render_template("login_success.html")


@app.route('/123')
def log123():
    return render_template("123.html")


@app.route('/admin_panel')
@login_required
def admin_panel():
    users = Authorization.query.order_by(Authorization.date.desc()).all()
    return render_template("admin_panel.html", users=users)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = ""
    if current_user.is_authenticated:
        return redirect(url_for('admin_panel'))

    class UserList(Authorization):

        def __init__(self, id, date, email, password, name):
            self.id = id
            self.date = date
            self.email = email
            self.password = password
            self.name = name

        def get_id(self):
            return self.id

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
                    list_users = UserList(user.id, user.date, user.email, user.password, user.name)
                    # user = db.session.query(Authorization).filter(Authorization.email == email).first()
                    login_user(list_users, remember=remember)
                    return redirect(url_for('private_profile'))
                else:
                    error = "Пароль введён не верно"
                    return render_template("login.html", error=error)
        error = "Такой электронной почты не было зарегистрировано"
        return render_template("login.html", error=error)
    return render_template("login.html", error=error)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile/<name>')
def profile(name):
    articles = Article.query.order_by(Article.date.desc()).all()
    user = Authorization.query.filter(Authorization.name == name).first()
    return render_template("profile.html", user=user, articles=articles)


@app.route('/private_profile')
def private_profile():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("private_profile.html", articles=articles)


@app.route('/profile_settings/<name>', methods=['POST', 'GET'])
def profile_settings(name):
    Authorization.query.filter(Authorization.name == name).first()
    error = ""
    user = Authorization.query.get(current_user.id)
    if request.method == "POST":
        user.name = request.form['name']
        user.email = request.form['email']
        user.info = request.form['info']
        password = request.form['password']
        password2 = request.form['password2']

        if len(user.name) >= 100 or len(user.email) >= 10000:
            error = "Слишком большое колличство символов в строке"
            return render_template("profile_settings.html", error=error)
        if len(user.name) <= 0 or len(user.email) <= 0:
            error = "Заполните поля: Имя и Email"
            return render_template("profile_settings.html", error=error)
        if password != "" or password2 != "":
            if password != password2:
                error = "Пароли должны совпадать"
                return render_template("profile_settings.html", error=error)

        if password != "":
            pattern_password = re.compile(r'^(?=.*[0-9])(?=.*[!@#$%^&*_()=+?:;"`~/|,<>.-])(?=.*[a-z])(?=.*[A-Z])'
                                          r'[0-9a-zA-Z!@#$%^&*_()=+?:;"`~/|,<>.-]{8,}$')
            is_password = bool(pattern_password.match(password))
            if not is_password:
                error = "Слабый пароль. Пароль должен состоять по крайней мере из восьми символов, содержать символы в " \
                        "верхнем и нижнем регистрах и включать по крайней мере одну цифру"
                return render_template("profile_settings.html", error=error)

            password = generate_password_hash(password)
            user.password = password

        try:
            db.session.commit()
        except:
            return "При редактировании пользователя произошла ошибка"
        else:
            img = request.files['img']
            if img.filename != "":
                if not os.path.exists('static\\img\\users_photo\\' + str(user.id)):
                    os.mkdir('static\\img\\users_photo\\' + str(user.id))
                imgpath = 'static\\img\\users_photo\\' + str(user.id) + '\\' + img.filename
                img.save(imgpath)
                user.imgpath = imgpath
                db.session.commit()
                return redirect('/private_profile')

            return redirect('/private_profile')
    else:
        return render_template("profile_settings.html", error=error)


@app.route('/profile_settings/<name>/delete')
def user_delete(name):
    articles = Article.query.order_by(Article.date.desc()).all()
    user = Authorization.query.filter(Authorization.name == name).first()

    separatepath = str(user.imgpath).split("\\")
    separatepath.pop(len(separatepath) - 1)
    pathtopackgage = ""
    for path in separatepath:
        if separatepath.index(path) != len(separatepath) - 1:
            pathtopackgage = pathtopackgage + path + "//"
        else:
            pathtopackgage = pathtopackgage + path
    if user.imgpath is None:
        db.session.delete(user)
        db.session.commit()
    else:
        shutil.rmtree(pathtopackgage)
        db.session.delete(user)
        db.session.commit()
    logout_user()
    return redirect('/')


@app.route('/headings', methods=['POST', 'GET'])
def headings():
    articles = Article.query.order_by(Article.date.desc()).all()
    Law = list()
    Sport = list()
    Finance = list()
    Nature = list()
    Learning = list()
    Health = list()
    Science = list()
    Politic = list()
    Army = list()
    Photo = list()
    select = "Все категории"
    selectdate = ""
    for article in articles:
        if article.heading == 'Закон и порядок':
            Law.append(article)
        if article.heading == 'Спорт':
            Sport.append(article)
        if article.heading == 'Финансы':
            Finance.append(article)
        if article.heading == 'Природа':
            Nature.append(article)
        if article.heading == 'Обучение':
            Learning.append(article)
        if article.heading == 'Здоровье':
            Health.append(article)
        if article.heading == 'Наука и технологии':
            Science.append(article)
        if article.heading == 'Политика':
            Politic.append(article)
        if article.heading == 'Военное дело':
            Army.append(article)
        if article.heading == 'Фотографии':
            Photo.append(article)

    headingsarray = [Law, Sport, Finance, Nature, Learning, Health, Science, Politic, Army, Photo]
    categorynames = 'Закон и порядок', "Спорт", 'Финансы', 'Природа', 'Обучение', 'Здоровье', 'Наука и технологии', \
                    'Политика', 'Военное дело', 'Фотографии '
    dictory = dict()
    number = 0
    while number < 10:
        dictory[categorynames[number]] = headingsarray[number]
        number = number + 1
    if request.method == "POST":
        select = request.form['select']
        selectdate = request.form.get('selectdate')

    return render_template("headings.html", articles=articles, Law=Law, Sport=Sport, Finance=Finance,
                           Nature=Nature, Learning=Learning, Health=Health, Science=Science, Politic=Politic,
                           Army=Army, Photo=Photo, select=select, selectdate=selectdate, dictory=dictory)


@app.route('/headings_sport')
def headings_sport():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_sport.html", articles=articles)


@app.route('/headings_law')
def headings_law():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_law.html", articles=articles)


@app.route('/headings_finance')
def headings_finance():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_finance.html", articles=articles)


@app.route('/headings_nature')
def headings_nature():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_nature.html", articles=articles)


@app.route('/headings_learning')
def headings_learning():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_learning.html", articles=articles)


@app.route('/headings_health')
def headings_health():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_health.html", articles=articles)


@app.route('/headings_science')
def headings_science():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_science.html", articles=articles)


@app.route('/headings_politic')
def headings_politic():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_politic.html", articles=articles)


@app.route('/headings_army')
def headings_army():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_army.html", articles=articles)


@app.route('/headings_photography')
def headings_photography():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("headings_photography.html", articles=articles)


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)


@app.route('/posts/<int:id>/delete')
def post_delete(id):
    article = Article.query.get_or_404(id)

    separatepath = str(article.imgpath).split("\\")
    separatepath.pop(len(separatepath) - 1)
    pathtopackgage = ""
    for path in separatepath:
        if separatepath.index(path) != len(separatepath) - 1:
            pathtopackgage = pathtopackgage + path + "//"
        else:
            pathtopackgage = pathtopackgage + path
    if article.imgpath is None:
        db.session.delete(article)
        db.session.commit()
    else:
        shutil.rmtree(pathtopackgage)
        db.session.delete(article)
        db.session.commit()
    return redirect('/posts')


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        article.heading = request.form['heading']

        if len(article.title) >= 60 or len(article.intro) >= 200 or len(article.text) >= 10000:
            return "Слишком большое колличство символов в строке"

        img = request.files['img']

        if img.filename != "":
            if os.path.exists('static\\img\\articles\\' + str(article.id)):
                imgpath = 'static\\img\\articles\\' + str(article.id) + '\\' + img.filename
                img.save(imgpath)
                article.imgpath = imgpath
            else:
                os.mkdir('static\\img\\articles\\' + str(article.id))
                imgpath = 'static\\img\\articles\\' + str(article.id) + '\\' + img.filename
                img.save(imgpath)
                article.imgpath = imgpath
        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "При обновлении статьи произошла ошибка"
    else:

        return render_template("post_update.html", article=article)


@app.route('/create-article', methods=['POST', 'GET'])
@login_required
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        heading = request.form.get('heading')
        author = current_user.name
        private = request.form['checkbox']

        if title == "" or intro == "" or text == "":
            return "Были заполнены не все обязательные поля"
        if len(title) >= 60 or len(intro) >= 200 or len(text) >= 10000:
            return "Слишком большое колличство символов в строке"

        article = Article(title=title, intro=intro, text=text, heading=heading, author=author, private=private)

        db.session.add(article)
        try:
            db.session.commit()
        except:
            return "При добавлении статьи произошла ошибка"
        else:
            img = request.files['img']
            if img.filename != "":
                os.mkdir('static\\img\\articles\\' + str(article.id))
                imgpath = 'static\\img\\articles\\' + str(article.id) + '\\' + img.filename
                img.save(imgpath)

                article.imgpath = imgpath
                db.session.commit()

                return redirect('/posts')
            return redirect('/posts')
    else:
        return render_template("create-article.html")


if __name__ == "__main__":
    app.run(debug=True)
