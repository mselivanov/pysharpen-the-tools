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

def main():
    print_header("Mathematical functions example")
    mathematical_funcs()

if __name__ == '__main__':
    main()