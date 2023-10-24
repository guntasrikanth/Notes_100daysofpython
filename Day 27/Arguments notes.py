# Function Arguments with Default values , Default values for  optional  arguments

# def add(a=1, b=5, c=6):
#     return a+b+c
#
# print(add()) #not giving any new values for default arguments
# print(add(5,7)) #giving new values for default arguments by not specifying arguments name
# print(add(c=8)) #giving new values for default arguments by specifying arguments name

#####################################################################################

# *args-take any number of arguments
# (arguments)(any name can be used but * has to be used before the name), it is tuple type

# def add(*nums):
#     print(nums[2]) #any access any values just like tuple
#     sum = 0
#     for n in nums:
#         sum += n
#     return sum
#
# print(add( 3, 4, 5, 23 ))

#####################################################################################

# **kwargs - take any number key and value pair values like dict data type, it is of dict type

# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs['add']
#     n /= kwargs['div']
#     print(n)
#
#
# calculate(24, add=6, div=5)

#####################################################################################

# creating own class with kwargs
class Car:
    def __init__(self, **kwargs):
        # self.model = kwargs['model']  - it gives error if model has no value
        # self.make = kwargs['make']  - it gives error if make has no value
        self.model = kwargs.get('model')  # by using get method we don't get any error even if model doesn't have
        # value instead it give none value
        self.make = kwargs.get('make')


car = Car(make='Jeep')
print(car.make)
