import copy
from fastapi import HTTPException, status

from schema.product import Product, products
from schema.order import Order, OrderCreate, orders

from logger import logger

class OrderService:

    @staticmethod
    def order_parser(orders: list[OrderCreate]):
        clone_order = copy.deepcopy(orders)

        for order in clone_order:
            order_items = order.items
            new_order = []
            for product_id in order_items:
                product = products.get(product_id)
                new_order.append(product)
            order.items = new_order
        return clone_order
    
    @staticmethod
    def check_availability(payload: OrderCreate):
        product_ids = payload.items
        for product_id in product_ids:
            product: Product = products.get(int(product_id))
            if product.quantity_available < 1:
                logger.warning("Product is no more available")
                raise HTTPException(status_code=400, detail='Product is unavailable')
            product.quantity_available -= 1
        return payload
    
    @staticmethod
    def check_existing_order(order_id: int):
     for order in orders:
        if order.id == order_id:
            return order
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order does not exist")
    
order_service = OrderService()