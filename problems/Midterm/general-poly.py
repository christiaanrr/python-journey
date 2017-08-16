# Write a function called general_poly, that meets the specifications below.
# For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗10^3+2∗10^2+3∗10^1+4∗10^0

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def power(y):
        x = 0
        for num in L:
            x = y*x + num
        return x
    return power
