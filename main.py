#importing fask
from flask import Flask,render_template,request,redirect,url_for
from database import fetch_products,fetch_sales,insert_products,insert_sales,sales_per_product,profit_per_product,sales_per_day,profit_per_day,check_user, add_user
from flask_bcrypt import Bcrypt

#instantiating our application -initialize our app
app = Flask(__name__)
app.secret_key = "12345678"
bcrypt =Bcrypt (app)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/products')
def products():
    products=fetch_products()
 
    return render_template('products.html',products=products)


@app.route('/add_products',methods=["GET","POST"])
def add_products():
    product_name = request.form['p-name']
    buying_price = request.form['b-price']
    selling_price = request.form['s-price']
    stock_quantity =request.form['stock']
    new_product = (product_name,buying_price,selling_price,stock_quantity)
    insert_products (new_product)
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data= fetch_sales()
    products=fetch_products()
    return render_template('sales.html',sales=sales_data,products=products)


@app.route('/make_sales',methods=["GET","POST"])
def make_sales():
    product_id = request.form['pid']
    quantity = request.form['quantity']
    new_sales = (product_id,quantity)
    insert_sales(new_sales)
    return redirect(url_for('sales')) 

@app.route('/dashboard')
def dashboard():
    profit_product=profit_per_product()
    sales_product=sales_per_product()
    profit_day=profit_per_day()
    sales_day=sales_per_day()

    product_name=[i[0] for i in profit_product]
    p_product=[ float(i[1]) for i in profit_product]
    s_product=[ float(i[1]) for i in sales_product]

    date=[i[0] for i in profit_day]
    p_day=[ float(i[1]) for i in profit_day]
    s_day=[ float(i[1]) for i in sales_day]

    return render_template('dashboard.html',product_name=product_name,p_product=p_product,s_product=s_product,date=date,p_day=p_day,s_day=s_day)




@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method=='POST':
        fullname = request.form['full_name']
        email = request.form['email']
        contact =request.form['contact']
        password= request.form['password']
        hashed_password =bcrypt.generate_password_hash(password).decode()
        user = check_user(email)
        if user == None:
            new_user = (fullname, email,contact, hashed_password)
            
            add_user(new_user)
            return redirect(url_for('login'))
        else:
            print('already registered')
    return render_template('register.html')

            


    
    
@app.route('/login',methods=['GET','POST'])
def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = check_user(email)
            if not user:
                return redirect(url_for('register'))
            else:
                if bcrypt.check_password_hash(user[-1],password):
                    return redirect(url_for('dashboard'))
                else:
                    return redirect(url_for('login'))
        return render_template('login.html')


app.run(debug=True)
                    
                    
                
                
                    
                    
                    
        
        

    
    

        





    







    
app.run(debug=True)