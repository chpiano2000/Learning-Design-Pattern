from price_calculator import PriceCalculator
from promotion_strategy import BlackFridayDiscount, PreOrderDiscount, NoDiscount


if __name__ == "__main__":
    print("The client has to pick a default promotion, which normally NoDiscount")
    calculator = PriceCalculator(NoDiscount())
    print("Default no discount -->", calculator.get_price(200))

    print("It's time for PreOrderDiscount")
    calculator.strategy = PreOrderDiscount()
    print("PreOrderDiscount -->", calculator.get_price(200))

    print("Oh no it's Black Friday!")
    calculator.strategy = BlackFridayDiscount()
    print("BlackFridayDiscount -->", calculator.get_price(200))
