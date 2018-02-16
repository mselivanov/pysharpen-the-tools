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

def main():
    print("{prefix}{message}{postfix}".format(prefix = "-"*10, 
                                              message = "Mathematical functions example", 
                                              postfix = "-"*10))
    mathematical_funcs()

if __name__ == '__main__':
    main()