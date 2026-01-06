from pydantic import BaseModel, Field, model_validator, computed_field


class Order(BaseModel):
    """
    A model representing an order with quantity, price per unit, and discount.
    It includes validation to ensure the discount does not exceed 50% and a computed
    This is an example of using model validators and computed fields in Pydantic.
    """
    quantity: int = Field(..., gt=0)
    price_per_unit: float = Field(..., gt=0)
    discount_percent: float = Field(0, ge=0, le=100)

    @model_validator(mode="after")
    def check_discount(self):
        if self.discount_percent > 50:
            raise ValueError("Discount cannot exceed 50% for any order")
        return self

    @computed_field
    @property
    def total_price(self) -> float:
        subtotal = self.quantity * self.price_per_unit
        discount = subtotal * (self.discount_percent / 100)
        return subtotal - discount


order = Order(quantity=10, price_per_unit=20.0, discount_percent=10)
print(order)
print("Total price:", order.total_price)

try:
    Order(quantity=10, price_per_unit=20.0, discount_percent=60)
except Exception as e:
    print("\nOrder error:")
    print(e)
