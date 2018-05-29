'''
@author: Maksim Selivanov
Module contains set of examples for using builtin's.
'''

def mathematical_funcs():
    neg_val = -1
    zero_val = 0
    pos_val = 1
    print(("abs({neg_val}) = {abs_neg_val} " +
        "abs({zero_val}) = {abs_zero_val} " + 
        "abs({pos_val}) = {abs_pos_val}").format(neg_val = neg_val, 
                                                abs_neg_val = abs(neg_val),
                                                zero_val = zero_val,
                                                abs_zero_val = abs(zero_val),
                                                pos_val = pos_val,
                                                abs_pos_val = abs(pos_val)))
    print("Modulo operator and floor division equation: x == (x//y)*y + (x%y)")
    divident, divisor = 5, 3
    print("{divident} % {divisor} == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divident % divisor))
    divident, divisor = 5, -3
    print("{divident} % {divisor} == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divident % divisor))
    divident, divisor = -5, 3
    print("{divident} % {divisor} == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divident % divisor))
    divident, divisor = -5, -3
    print("{divident} % {divisor} == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divident % divisor))
                                                            

    print("divmod, floor division and modulo equation: x == divmod(x, y) == (x//y, x%y)")
    divident, divisor = 5, 3
    quotient, reminder = divmod(divident, divisor)
    print("divmod({divident}, {divisor}) == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divmod(divident, divisor)))

    divident, divisor = 5, -3
    quotient, reminder = divmod(divident, divisor)
    print("divmod({divident}, {divisor}) == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divmod(divident, divisor)))
    divident, divisor = -5, 3
    quotient, reminder = divmod(divident, divisor)
    print("divmod({divident}, {divisor}) == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divmod(divident, divisor)))
    divident, divisor = -5, -3
    quotient, reminder = divmod(divident, divisor)
    print("divmod({divident}, {divisor}) == {result}".format(divident = divident, 
                                                            divisor = divisor, 
                                                            result = divmod(divident, divisor)))
                                                            
def print_header(message):
    print("{prefix}{message}{postfix}".format(prefix = "-"*10, 
                                              message = message, 
                                              postfix = "-"*10))

def logical_funcs():
    logical_constructs = [[], [None], {}, {None}, 0, 0.0, None, "", (), ("",), (None,)]
    for op in logical_constructs:
        print("bool({operand}) = {result}".format(operand = op, result = bool(op)))
    logical_constructs = [[], None, {}, 0, 0.0]
    print("any({iterable}) = {result}".format(iterable = logical_constructs, result = any(logical_constructs)))
    logical_constructs = [[], {None}, {}, 0, 0.0, None]
    print("any({iterable}) = {result}".format(iterable = logical_constructs, result = any(logical_constructs)))
    logical_constructs = [{None}, [None], 1, "None"]    
    print("all({iterable}) = {result}".format(iterable = logical_constructs, result = all(logical_constructs)))

def string_char_funcs():
    s = "Hello, world!"
    print("ascii({param}) = {result}".format(param = s, result = ascii(s)))
    print("repr({param}) = {result}".format(param = s, result = repr(s)))
    
    s = "This is 'Hello, world!' in Russian: 'Привет, мир!'"
    print("ascii({param}) = {result}".format(param = s, result = ascii(s)))
    print("repr({param}) = {result}".format(param = s, result = repr(s)))
    
    code_point1 = 97
    code_point2 = 8364
    code_point3 = 0x10FFFF
    print("chr({param}) = {result}".format(param = code_point1, result = chr(code_point1)))
    print("chr({param}) = {result}".format(param = code_point2, result = chr(code_point2)))
    print("chr({param}) = {result}".format(param = code_point3, result = chr(code_point3)))
    try:
        c1 = chr(code_point3+1)
    except ValueError as e:
        print("chr({param}) = 'Exception: {result}'".format(param = code_point3+1, result = e))
    
                                              
def main():
    print_header("Mathematical functions example")
    mathematical_funcs()
    print_header("Logical functions example")
    logical_funcs()
    print_header("String/char functions example")
    string_char_funcs()
    

if __name__ == '__main__':
    main()