def list_attributes(cls):
    print(f'Class: {cls.__name__}')
    for key, attr in cls.__dict__.items():
        print(f'Attribute name: {key}')
        print(f'Attribute type: {type(attr)}')
    return cls

@list_attributes
class Customer:
    customer_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Customer.customer_count += 1
        
    def pretty_print(self):
        print(f'Customer name: {self.name}')
        print(f'Customer e-mail: {self.email}')
    

def main():
    customer = Customer('Coca Cola', 'coca@coca.com')

if __name__ == '__main__':
    main()
