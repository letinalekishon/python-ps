
import psycopg2
from datetime import datetime


#connect to datase
conn = psycopg2.connect(user="postgres",password="powers05",host="localhost",port="5432",database="myduka")


#execute db operations
cur = conn.cursor()

 #query
def fetch_products():
    cur.execute("select * from products;")

    products = cur. fetchall()


    return products


#fetching sales
def fetch_sales():
    cur.execute("select * from sales")

    sales= cur.fetchall()

    return sales
 



# insert sales
def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s ,%s,now())'
    cur.execute(query,values)
    conn.commit()


def fetch_data(table):
    cur.execute(f"select * from {table} ;")
    data = cur.fetchall()
    return data
product = fetch_data('products')

#insert product - method1 takjes values as parameters
def insert_products(values):
    insert ="insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)" 
    cur.execute(insert,values)
    conn.commit()

def profit_per_day():
    cur.execute("select sales.created_at,sum((products.selling_price -products.buying_price)*sales.quantity) as profit from products join sales on products.id = sales.pid group by (sales.created_at);")
    profit_per_day = cur.fetchall()
    return profit_per_day



def profit_per_product():
    cur.execute("select products.name,sum((products.selling_price -products.buying_price)*sales.quantity) as profit from products join sales on products.id = sales.pid group by (products.name);")
    profit_per_product = cur.fetchall()
    return profit_per_product


def sales_per_product():
    cur.execute("select products.name,sum(products.selling_price*sales.quantity) as totalsales from products join sales on products.id=sales.pid group by (products.name);")
    sales_per_product = cur.fetchall()
    return sales_per_product



def sales_per_day():
    cur.execute("select sales.created_at ,sum(products.selling_price*sales.quantity) as total_sales from sales join products on products.id=sales.pid group by (sales.created_at);")
    sales_per_day = cur.fetchall()
    return sales_per_day



def check_user(email):
    q= "select * from users where email = %s"
    cur.execute(q,(email,))
    user =cur.fetchone()
    return user

def add_user(user_details):
    q = "insert into users(fullname, email, contact, password)values (%s, %s, %s,%s)"
    cur.execute(q,user_details)
    conn.commit()







    



    
