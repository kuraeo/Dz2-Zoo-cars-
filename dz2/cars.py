import random
winner = random.randint(1, 2)

class Cars:
    all_cars = 0
    brand = "BMW"
    def __init__(self, model, color, maxspeed, years, kmdriven):
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.years = years
        self.kmdriven = kmdriven
        Cars.all_cars += 1
    def go(self):
        print(f"The {self.model} has gone")

    def finish1(self):
        if winner == 1:
            print(f"{self.model} won")
        else:
            print(f"{self.model} lost")
    def finish2(self):
        if winner == 2:
            print(f"{self.model} won")
        else:
            print(f"{self.model} lost")

car1 = Cars("BMW 4 Series", "White", 240, 9, 7257)
car2 = Cars("BMW X1", "White", 220, 14, 12024)

car1.finish1()
car2.finish2()

print(f"Results of {Cars.brand} cars competition. The amount of participants: {Cars.all_cars}")