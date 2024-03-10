from fastapi import  status, HTTPException
from schema.customer import Customer, CustomerCreate, customers

from logger import logger

class CustomerService:
    @staticmethod
    def check_existing_username(payload: CustomerCreate):
       new_username = payload.username
       existing_usernames = []
       for customer in customers:
         existing_usernames.append(customer.username)
         if new_username in existing_usernames:
            logger.warning("Username exists")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists"
               )
       return payload   


customer_service = CustomerService()