class poly():
    # Здесь: poly() имеет в себе одну переменную-словарь "coef", в которой хранятся
    #значения по шаблону { <степень>: <Q-объект>, ... }.
    # Пример: poly( {23: Q( 3, 4 ), 7: Q( -4 )} ) будет выглядеть как "3/4 * x^23 - 4 * x^7".
    def __init__( self, coeflist ):
        self.coef = {}
        if isinstance(coeflist, list):
            for i in range( len( coeflist ) ):
                if not isinstance(i, Q):
                    self.coef.update( { i: Q( coeflist[ i ] ) } ) #append( Q( i ) )
                else:
                    self.coef.update( { i: coeflist[ i ] } )
        elif isinstance(coeflist, dict):
            self.coef = coeflist

    def __str__(self):
        coef, out = self.coef, ""
        if len( self.coef ) == 0:
            out = "0"
        else:
            out = str( self.coef.items() )
            #for i in range( len( self.coef ) ):
                #out += str( self.coef[ i ] ) + ", "
            #out = str( self.coef )
            '''for i in range( len( self.coef ) ):
                fl = poz_z_d( coef[i].num )
                if fl == 0:
                    pass
                else:
                    if i != 0 and not coef[i].num.sign:
                        out += '+'
                    if i == self.deg-2:
                        out += str( coef[i] ) + 'x'
                    elif i == self.deg - 1:
                        out += str( coef[i] )
                    else:
                        out += str( coef[i] ) +'x^'+ str( self.deg - i - 1)'''
        
        return out

    # НОД многочлена.
    def GCF_PP_P(poly1,poly2):
        c=poly1%poly2
        while NZER_N_B(DEG_P_N(c)):
            poly1,poly2=poly2,c
            c=poly1%poly2
        return poly2

    # Производная. Жаль, нет такого оператора в Python, перегрузить не получится...
    def DER_P_P(poly):
        poly_derivative=None
        for i in range (DEG_P_N(poly)):
            poly_derivative += DEG_P_N(poly) * LED_P_Q(poly)
            poly.remove(0)
        return  poly_derivative

    
#p = poly( [ Q( 2 ), Q(3), Q(4) ] )
#print( p )
