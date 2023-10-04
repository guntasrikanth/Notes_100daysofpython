def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

print(add( 3, 4, 5, 23 ))

def calculate(n, **kwargs):
    n += kwargs['add']
    n /= kwargs['div']
    print(n)

calculate(24, add=6, div=5)


class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.make = kwargs.get('make')

car = Car(make = 'Hyundai')
print(car.make)
