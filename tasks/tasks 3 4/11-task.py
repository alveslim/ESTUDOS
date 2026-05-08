class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        discounted_price = self.price - discount_amount
        return discounted_price
    
    def __str__(self): # fzd referencia direto a classe 
        return f"Produto: {self.name} "
    

product1 = Product("Super Mario Bros", 59.99)
print(product1)
print(f"Preco de desconto: R${product1.discount(10):.2f}")  # Aplica um desconto de 10%