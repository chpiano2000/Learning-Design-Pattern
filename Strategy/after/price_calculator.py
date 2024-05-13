from promotion_strategy import DiscountStrategy


class PriceCalculator:
    def __init__(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> DiscountStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def get_price(self, original_price: float) -> float:
        return self._strategy.calculate_price(original_price)
