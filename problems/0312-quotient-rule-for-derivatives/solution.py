import numpy as np
from numpy.polynomial import Polynomial as Poly

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g=Poly(g_coeffs[::-1])
    h=Poly(h_coeffs[::-1])
    g_der=g.deriv()
    h_der=h.deriv()
    
    return (g_der(x)*h(x)-g(x)*h_der(x))/h(x)**2
    
        
            
