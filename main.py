from N import *
from Z import *
from Q import *
from poly import *

#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#
import re
def parse(s):
    def forN(s):
        return 'N(' + s[0] + ')'

    def forx(s):
        return 'poly(1:' + s[0][:-1] + ')'

    def fordx(s):
        return 'poly({}:{})'.format(s[3], s[1])

    patforn = '(?:(?<!x\^)(?<!\d))\d+(?![xX0-9])'  # поиск всех не-коэффициентов х
    patforx = '(?<![x0-9])\d+x(?=[^\^0-9x])'  # для х без степени
    patfordx = '(?<![x0-9])(\d+)(x\^)(\d+)'  # для х со степенью

    s = re.sub(patforn, forN, s)
    s = re.sub(patforx, forx, s)
    s = re.sub(patfordx, fordx, s)
    return s

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

