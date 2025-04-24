#importing fask
from flask import Flask,render_template

#instantiating our application -initialize our app

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return "our services"

@app.route('/profile')
def profile():
    return "my profile"

@app.route('/orders')
def orders():
    return "our orders"
 
app.run(debug=True)