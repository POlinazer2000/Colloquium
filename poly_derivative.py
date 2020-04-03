def DER_P_P(poly):
    poly_derivative=None
    for i in range (DEG_P_N(poly)):
        poly_derivative += DEG_P_N(poly) * LED_P_Q(poly)
        poly.remove(0)
    return  poly_derivative