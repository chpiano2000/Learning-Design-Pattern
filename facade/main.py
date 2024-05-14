from domain import Discount, Shipping, Fees
from facade import EcommerceFacade


def buy(price: float) -> float:
    # Initialize the domains instances
    discount = Discount()
    shipping = Shipping()
    fees = Fees()

    # Initialize the facade
    price_calculator = EcommerceFacade(discount, shipping, fees)

    # Calculate the price
    result = price_calculator.calculate(price)
    return result


if __name__ == "__main__":
    print("Price ->", buy(120000))
