from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def hello_world():
    
    context = {
        'title' : 'Kekembas Blog | HOME',
        'customer_name': 'brian',
        'customer_username': 'bstanton',
        'items':{
            1: 'icream',
            2: 'bread'
        },
        'followers' : [
            {
                'username' : 'sdavvit',
                'created_at' :'2021-02-28'
            },
            {
                'username' : 'jacrter',
                'created_at' :'2020-09-08'
            }
        ]
    }
    return  render_template('index.html', **context)

 
@app.route('/register')
def register():
    title = 'Kekembas blog | REGISTER'
    return render_template('register.html', title=title)