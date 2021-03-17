from flask import current_app as app, render_template
from app.models import Post

@app.route('/')
@app.route('/index')
def index():
    
    context = {
        'title' : 'Kekembas Blog | HOME',
        'posts' : Post.query.order_by(Post.date_created).all()
    }
        
    return  render_template('index.html', **context)

 