
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


    for product in products:
        print(products)


#fetching sales
def fetch_sales():
    cur.execute("select * from sales")

    sales= cur.fetchall()

    for sale in sales:
        print(sales)
 


#insert products
def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('mango',400,600,14)")
cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('mandazi',400,630,14)")
conn.commit()
# insert sales
def insert_sales():
    cur.execute("insert into sales(pid,quantity,created_at)values(4,5,'{now}')")


conn.commit()


fetch_sales()
fetch_products()



def fetch_data(table):
    cur.excute(f"select * from{table} ;")
    data = cur.fetchall()
    return data
    product = fetch_data('products')

#insert product - method1 takjes values as parameters
def insert_products(values):
    insert ="insert into product(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit()

    product_values= ("apple",120,150,200)
    insert_products(products_values1)
    products

