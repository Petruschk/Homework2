class Cars:
    wheels: 4
    lights: 2
    engine: 1
    def __init__(self, color, brand, year):
        self.color = color
        self.brand = brand
        self.years = year

#colors

print ("1-red, 2-orange, 3-black")

x1 = Cars("BMW",1 ,2019)
x2 = Cars("Audi",3 ,2020)
x3 = Cars("Mercedes",2 ,2021)

print(x1.color)
print(x1.brand)
print(x1.years)

print(x2.color)
print(x2.brand)
print(x2.years)

print(x3.color)
print(x3.brand)
print(x3.years)