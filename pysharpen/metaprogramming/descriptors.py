"""
Module demonstrates property object
"""


class Quantity:

    _counter = 0

    def __init__(self):
        cls = self.__class__
        index = cls._counter
        self.storage_name =  f"{cls.__name__}#{index}"
        cls._counter += 1

    def __get__(self, instance, owner):
        if not instance:
            return self
        return getattr(instance, self.storage_name) 

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must be > 0")


class OrderItem:
    """
    Class demonstrates properties
    """

    weight = Quantity()
    price = Quantity()

    def __init__(self, product, weight, price):
        self.weight = weight
        self.product = product
        self.price = price


def main():
    "Main function"
    item = OrderItem("Watermelon", 1.1, 4)
    print(item.weight)
    print(item.price)


if __name__ == "__main__":
    main()
