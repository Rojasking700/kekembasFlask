from app import app, db, mail, Message
from flask import render_template,request, flash, redirect, url_for
from app.forms import UserInfoForm, PostForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    
    context = {
        'title' : 'Kekembas Blog | HOME',
        'customer_name': 'brian',
        'customer_username': 'bstanton'
    }
        
    return  render_template('index.html', **context)

 
@app.route('/register', methods=['GET','POST'])
def register():
    title = 'Kekembas blog | REGISTER'
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        print(username,email, password)
        
        #create a new instance of User
        new_user = User(username,email,password)
        #add new instance of use
        db.session.add(new_user)
        #commit database
        db.session.commit()

        #SEND EMAIL TO NEW USER
        msg = Message(f"welcome, {username}", [email])
        msg.body = 'Thank you for siging up for the kekembas blog. I hope you enjoy our blog!'
        msg.html = '<p>Thank you so much for signing up for out blog!</p>'
        
        mail.send(msg)

        flash("You have succesfully signed up!", "success")
        return redirect(url_for('index'))

    return render_template('register.html', title=title,form=form)

@app.route('/createpost', methods=['GET','POST'])
@login_required
def createpost():
    title = " Kekembas blog | CREATE POST"
    post = PostForm()
    if request.method == "POST" and post.validate():
        post_title = post.title.data
        content = post.content.data
        print(post_title, content)
    return render_template('create_post.html', post=post, title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Kekembas blog | LOGIN'
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            flash("Incorrect Email/Password. Please try again", 'danger')
            return redirect(url_for('login'))
        
        login_user(user,remember=form.remember_me.data)
        flash("You have successfully logged in!", 'success')
        next_page = request.args.get('next')
        if next_page:

            return redirect(url_for(next_page.lstrip('/')))
        return redirect(url_for('index'))


    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("you have seccesfully logged out", 'primary')
    return redirect(url_for('index'))