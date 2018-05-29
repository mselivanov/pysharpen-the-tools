"""
Module demonstrates decorator pattern.
Problem:
1. Add new features to existing objects.
2. Add them dynamically.
3. Do not use subclassing.
"""

from functools import wraps

def unmasked_decorator(function):
    """Unmasked decorator"""
    def decorator(*args, **kwargs):
        """Actual decorator function"""
        print("{0} was called".format(function.__name__))
        return function(*args, **kwargs)
    return decorator

def masked_decorator(function):
    """Masked decorator"""
    # Update wrapper function to look like wrapped function
    @wraps(function)
    def decorator(*args, **kwargs):
        """Actual decorator function"""
        print("{0} was called".format(function.__name__))
        return function(*args, **kwargs)
    return decorator
    
@unmasked_decorator    
def unwrapped_test_function(message, name = "George"):
    """
    Test function for unwrapped decorator
    """
    result = "{1} says: {0}".format(message, name)
    print(result)
    return result

@masked_decorator    
def wrapped_test_function(message, name = "George"):
    """Test function for wrapped decorator"""
    result = "{1} says: {0}".format(message, name)
    print(result)
    return result    
    
def main():
    s1 = unwrapped_test_function("Let's rock!", name = "Bill")
    print("Result: " + s1)
    print("Name: " + unwrapped_test_function.__name__)
    print("Doc: " + unwrapped_test_function.__doc__)
    
    s2 = wrapped_test_function("Better way to rock!", name = "Steve")
    print("Result: " + s1)
    print("Name: " + wrapped_test_function.__name__)
    print("Doc: " + wrapped_test_function.__doc__)
    
if __name__ == "__main__":
    main()