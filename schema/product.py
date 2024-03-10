from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    price: Decimal
    quantity_available: int

class ProductCreate(BaseModel):
    name: str
    price: Decimal
    quantity_available: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    quantity_available: Optional[int] = None

products = {
    1: Product(id=1, name="Milo", price=Decimal('50.00'), quantity_available=1),
    2: Product(id=2, name="Pepsi", price=Decimal('150.00'), quantity_available=15),
    3: Product(id=3, name="Coffee", price=Decimal('10.50'), quantity_available=5),
}