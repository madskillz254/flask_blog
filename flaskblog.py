from flask import Flask ,render_template , url_for
from forms import RegistrationForm , LoginForm

app = Flask(__name__)

# setting a secret key
app.config['SECRET_KEY'] = 'b100a81daa02be3375a2922dfff54c3b'

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


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html" , title='register' , form = form )



@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html" , title='login' , form = form )

if __name__ == '__main__':
    app.run(debug=True)