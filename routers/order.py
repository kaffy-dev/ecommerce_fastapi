from fastapi import APIRouter, Depends, status, HTTPException

from schema.order import Order, OrderCreate, orders
from services.order import order_service
from schema.product import products, Product

order_router = APIRouter()

# list all order
# create an order 

@order_router.get('/', status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {'message': 'success', 'data': response}

@order_router.post('/create', status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate = Depends(order_service.check_availability)):
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items

    # get current order id
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids
    )
    orders.append(new_order)

    return {'message': 'Order created successfully', 'data': new_order}


@order_router.put('/checkout/{order_id}', status_code=status.HTTP_200_OK)
def checkout_order(payload: Order = Depends(order_service.check_existing_order)):
    payload.status = 'completed'
    return {'message': 'Order successfully checked out', 'data': payload}


