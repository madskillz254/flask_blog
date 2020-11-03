from flask import Flask ,render_template , url_for
app = Flask(__name__)

posts = [
    {
        'author': 'corey schafer',
        'title': 'blog post 1',
        'content':'first post content',
        'date_posted': 'april 20 ,2018'
    } ,
        {
        'author': 'jane doe',
        'title': 'blog post 2',
        'content':'second post content',
        'date_posted': 'april 21 ,2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html" , posts= posts)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)