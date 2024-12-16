from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        return 0

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def calculate_discount(self, amount: float) -> float:
        return amount * self.percentage / 100

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount: float):
        self.discount = discount

    def calculate_discount(self, amount: float) -> float:
        return min(amount, self.discount)

class Order:
    def __init__(self, amount: float, discount_strategy: DiscountStrategy):
        self.amount = amount
        self.discount_strategy = discount_strategy

    def calculate_total(self) -> float:
        discount = self.discount_strategy.calculate_discount(self.amount)
        return self.amount - discount
