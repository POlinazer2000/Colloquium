from N import *
from Z import *
from Q import *
from poly import *

def tryReverseOp(a, b, op):
    crutch = {type(N(0))   :1,
              type(Z(0))   :2,
              type(Q(0))   :3,
              type(poly(0)):4
              }

    if crutch[type(a)] < crutch[type(b)]:
        eval(type(b)(a) + op + b)
    else:
        eval(a + op + type(a)(b))


#poly = polynom( [ N([0]), N([3]), N([0]), Z([-1]) ] )
#print( "f(x) =", poly )

print( tryReverseOp( N(1), N(2), '+' ) )


