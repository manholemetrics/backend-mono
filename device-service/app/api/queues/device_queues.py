import app.api.services.handlers.device_handlers as device_handlers 
from app.api.main import celery

@celery.task
def create_order(name, quantity):
    return {"message": f"Hi {name}, Your order has completed!",
        "order_quantity": quantity}
