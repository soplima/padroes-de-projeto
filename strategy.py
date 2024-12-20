from abc import ABC, abstractmethod

# Classe base abstrata para estratégias de desconto
class DiscountStrategy(ABC):
    # Método abstrato que define a interface para cálculo do desconto
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass

# Estratégia de desconto que não aplica nenhum desconto
class NoDiscount(DiscountStrategy):
    # Retorna 0, pois não há desconto
    def calculate_discount(self, amount: float) -> float:
        return 0

# Estratégia de desconto baseada em uma porcentagem
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage  # Define a porcentagem do desconto

    # Calcula o desconto como uma porcentagem do valor total
    def calculate_discount(self, amount: float) -> float:
        return amount * self.percentage / 100

# Estratégia de desconto com valor fixo
class FixedDiscount(DiscountStrategy):
    def __init__(self, discount: float):
        self.discount = discount  # Define o valor fixo do desconto

    # Retorna o menor valor entre o desconto fixo e o valor total (não permitindo valores negativos)
    def calculate_discount(self, amount: float) -> float:
        return min(amount, self.discount)

# Classe que representa um pedido, aplicando uma estratégia de desconto
class Order:
    def __init__(self, amount: float, discount_strategy: DiscountStrategy):
        self.amount = amount  # Valor total do pedido
        self.discount_strategy = discount_strategy  # Estratégia de desconto utilizada

    # Calcula o total final após aplicar o desconto
    def calculate_total(self) -> float:
        discount = self.discount_strategy.calculate_discount(self.amount)  # Calcula o desconto
        return self.amount - discount  # Retorna o valor total com o desconto aplicado

# Exemplos de uso:
# Pedido sem desconto
order1 = Order(100, NoDiscount())
print(order1.calculate_total())  # Saída: 100

# Pedido com desconto percentual
order2 = Order(200, PercentageDiscount(10))  # 10% de desconto
print(order2.calculate_total())  # Saída: 180

# Pedido com desconto fixo
order3 = Order(50, FixedDiscount(20))  # Desconto fixo de 20
print(order3.calculate_total())  # Saída: 30
