"""
Module demonstrates property object
"""


def quantity(attribute_name):
    def fget(self):
        return getattr(self, "_" + attribute_name)

    def fset(self, value):
        message = f"{attribute_name} must be greater than zero"
        if value > 0:
            setattr(self, "_" + attribute_name, value)
        else:
            raise ValueError(message)

    return property(fget=fget, fset=fset)


class OrderItem:
    """
    Class demonstrates properties
    """

    weight = quantity("weight")
    price = quantity("price")

    def __init__(self, product, weight, price):
        self.weight = weight
        self.product = product
        self.price = price


def main():
    "Main function"
    item = OrderItem("Watermelon", 1.1, 4)
    print(item.weight)
    print(item.price)
    item1 = OrderItem("Watermelon", 1.1, -4)


if __name__ == "__main__":
    main()
