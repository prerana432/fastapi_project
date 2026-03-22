from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class Product(BaseModel):
    name: str
    price: int

class Order(BaseModel):
    user_id: int
    product_id: int