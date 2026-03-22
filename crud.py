from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db, user_id):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db, user_id, user):
    db_user = get_user(db, user_id)
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db, user_id):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def create_product(db, product):
    db_product = models.Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db):
    return db.query(ProductModel).all()

def get_product(db, product_id):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def update_product(db, product_id, product):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not db_product:
        return {"error": "Product not found"}

    db_product.name = product.name
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)

    return db_product

def delete_product(db, product_id):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not db_product:
        return {"error": "Product not found"}

    db.delete(db_product)
    db.commit()

    return {"message": "Product deleted"}

def create_order(db, order):
    db_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db):
    return db.query(OrderModel).all()

def get_order(db, order_id):
    return db.query(OrderModel).filter(OrderModel.id == order_id).first()

def delete_order(db, order_id):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()

    if not db_order:
        return {"error": "Order not found"}

    db.delete(db_order)
    db.commit()

    return {"message": "Order deleted"}

def update_order(db, order_id, order):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()

    if not db_order:
        return {"error": "Order not found"}

    db_order.user_id = order.user_id
    db_order.product_id = order.product_id

    db.commit()
    db.refresh(db_order)

    return db_order