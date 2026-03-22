from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API working"}

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)

@app.post("/products")
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)

@app.put("/products/{product_id}")
def update_product(product_id: int, product: schemas.Product, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)

@app.post("/orders")
def create_order(order: schemas.Order, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@app.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    return crud.get_order(db, order_id)

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return crud.delete_order(db, order_id)

@app.get("/products/search/{name}")
def search_product(name: str, db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.name.contains(name)).all()

@app.get("/users/count")
def user_count(db: Session = Depends(get_db)):
    return {"total_users": db.query(models.User).count()}

@app.get("/orders/user/{user_id}")
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()

@app.get("/orders/count")
def order_count(db: Session = Depends(get_db)):
    return {"total_orders": db.query(models.Order).count()}