from domain import Discount, Shipping, Fees


class EcommerceFacade:
    def __init__(self, discount: Discount, shipping: Shipping, fees: Fees) -> None:
        self._discount = discount or Discount()
        self._shipping = shipping or Shipping()
        self._fees = fees or Fees()

    def calculate(self, price: float) -> float:
        # The facade method that calculates the price
        price = self._discount.calculate(price)
        price = self._fees.calculate(price)
        price += self._shipping.calculate(price)
        return price
