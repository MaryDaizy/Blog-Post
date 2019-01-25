from flask import Flask, render_template, url_for 
app = Flask(__name__)

posts = [
    {
        'author': 'Daisy Nakitende',
        'title': 'Blog post 1',
        'content': 'First blog content',
        'post_date': 'January 15 2019'
    },
     {
        'author': 'Jane Maurius',
        'title': 'Blog post 2',
        'content': 'Second blog content',
        'post_date': 'January 18 2019'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    return "The Project Page"

if __name__ == '__main__':
    app.run(debug=True)





