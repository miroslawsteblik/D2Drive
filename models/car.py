class Car:
    def __init__(self, model, year, price, color):
        self.model = model 
        self.year = year 
        self.price = price 
        self.color = color

    def __str__(self):
        return f'{self.model} {self.year} {self.price} {self.color}'
