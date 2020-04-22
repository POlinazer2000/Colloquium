from N import *
from Z import *
from Q import *
from poly import *

#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#

def parse(str):
    tmp = str.replace(' ','')
    ops = ['/','//','*','+','-','%']
    tmp = tmp.split(ops)
    return tmp

def tryReverseOp(a, b, op):
    crutch = {type(N(0)): 1,
              type(Z(0)): 2,
              type(Q(0)): 3,
              type(poly(0)): 4
              }

    # print( type( a ), type( b ) )
    # print( type(N(0)), type(Z(0)), type(Q(0)), type(poly(0)) )
    # print( a, op, b, ": ", type( a ), type( b ) )
    # print( self, "__add__", other, ": ", type( self ), type( other ) )
    try:
        if crutch[type(a)] < crutch[type(b)]:
            return eval('type(b)(a)' + op + 'b')
        else:
            # print( str( a ) + op + str( eval( "type(a)(b)" ) ) )
            return eval("a" + op + 'type(a)(b)')
    except:
        print(a, op, b, ": ", type(a), type(b))
        raise RuntimeError

