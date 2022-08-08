# def add(*args):
#     print(args[0])
#
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(1,3,5,8,10,444,6,3,44))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add = 3, multiply=5)

class Car:
    def __init__(self, **kw):
        # using dictionary.get() instead of dictionary[] will make sure there is no error
        # and will just return None
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline", seats=6)
print(my_car.seats)