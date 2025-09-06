from fastapi import Depends, FastAPI
from models import Product
from config import session, engine
from database_models import Base, Product as DBProduct
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS for React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# list of products with 4 products like phones, laptops, pens, tables
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(
        id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30
    ),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(
        id=4, name="Table", description="A wooden table", price=199.99, quantity=20
    ),
]


# Dependency to get DB session for each request
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# Database session
def init_db():
    db = session()

    count = db.query(DBProduct).count()

    if count == 0:
        for product in products:
            db.add(DBProduct(**product.model_dump()))
        db.commit()
        # print("Database initialized with sample products.")

    db.close()


# Initialize the database with sample products
init_db()


# Get all products
@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(DBProduct).all()
    return db_products


# Get product by ID
@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(DBProduct).filter(DBProduct.id == id).first()
    if product:
        return product
    return {"error": "Product not found"}


# Add a new product
@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db_product = DBProduct(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Upadte a product by ID
@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(DBProduct).filter(DBProduct.id == id).first()
    if db_product:
        for key, value in product.model_dump().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return {"message": "Product updated successfully", "product": db_product}
    return {"error": "Product not found"}


# Delete a product by ID
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(DBProduct).filter(DBProduct.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}
