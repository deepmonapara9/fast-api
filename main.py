from fastapi import FastAPI
from models import Product

app = FastAPI()

# list of products with 4 products like phones, laptops, pens, tables
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]


# Get all products
@app.get("/products")
def get_all_products():
    return products


# Get product by ID
@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


# Add a new product
@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product