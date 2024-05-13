from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_price(self, original_price: float) -> float:
        pass


## Concrete classes
class NoDiscount(DiscountStrategy):
    def calculate_price(self, original_price: float) -> float:
        return original_price


class PreOrderDiscount(DiscountStrategy):
    def calculate_price(self, original_price: float) -> float:
        return original_price * 0.9 if original_price <= 200 else original_price - 30


class BlackFridayDiscount(DiscountStrategy):
    def calculate_price(self, original_price: float) -> float:
        return original_price * 0.5
