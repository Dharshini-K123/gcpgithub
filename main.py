from fastapi import FastAPI

from models import Product

app=FastAPI()

products=[
    Product(id=1,name="phone",description="Smart Phone hight camera quality",price=1200,quantity=5) ,
    Product(id=2,name="Laptop",description="Smart Laptop hight Ram ",price=10200,quantity=2) 
]

@app.get("/")
def greet():
    return "welcome Dharshu!"


@app.get("/products")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id:int):
     
    return products[id]



