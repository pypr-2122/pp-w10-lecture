# a = [2.0]
# print(a)
# print(type(a))

import numpy as np

class Polynomial():
    '''
    Defines a Polynomial class/type.
    '''
    
    # Dunder methods (double underscore)
    def __init__(self, coefficients):
        self.coef = np.array(coefficients)
        self.degree = len(coefficients) - 1
    

    def __str__(self):
        '''
        Define the string representation of a polynomial.
        '''
        display_output = ''
        for i in range(len(self.coef)):
            if self.coef[i] != 0:
                sign = '+' if self.coef[i] >=0 else '-'
                # sign = 'plus' if self.coef[i] >=0 else 'minus'
                # if self.coef[i] >= 0:
                #     sign = '+'
                # else:
                #     sign = '-'
                display_output += f'{sign} {np.abs(self.coef[i])}x^{self.degree - i} '
                # display_output += f'{sign} {np.abs(self.coef[i])} times x to the power of {self.degree - i}, '
        
        return display_output
    
    def derivative(self):
        '''
        Differentiates a polynomial.
        '''
        coeffs = []
        for i in range(self.degree):
            coeffs.append(self.coef[i] * (self.degree - i))
        
        return Polynomial(coeffs)
    
    # Exercises:
    # - Create an integral(self) method that returns a Polynomial,
    # the indefinite integral of self.
    # - Create an evaluate(self, x) method that evaluates a Polynomial
    # at a given point x. Used as poly.evaluate(2) for instance.
    # - Create a definite_integral(self, a, b) method to calculate the integral
    # of a polynomial between x=a and x=b. Use integral() and evaluate().
    # - Create the __add__(self, other) method which sums 2 polynomials and returns
    # the result as a third polynomial. Use as poly1 + poly2.
        

# Create a polynomial, 3x^3 + 2x -1
poly = Polynomial([3, 0, 2, -1])
print(poly)

deriv = poly.derivative()
print(deriv)
# print(type(poly))
# print(poly.coef)
# print(poly.degree)



# # Creating a list
# my_list = list([3, 4, 5])
# print(my_list)
# print(type(my_list))
# my_list.append(3)
# print(my_list)

# # Create a polynomial
# poly = Polynomial()
# print(poly)
# print(type(poly))

# import numpy as np

# arr = np.zeros([3, 5])
# print(arr.shape)