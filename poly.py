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

    def __add__(self, other):
        if len(self.coef)<len(other.coef):
            self, other = other, self
        out=poly(str(self))
        do=len(other.coef)
        ds=len(self.coef)
        for i in range(do):
            out.coef[ds-do+i] += other.coef[i]
        while(out.coef[0]==0):
            out.coef.pop(0)
        return poly(str(out))


    def __sub__(self, other):
        if len(self.coef) < len(other.coef):
            self, other = other, self
        out = poly(str(self))
        do = len(other.coef)
        ds = len(self.coef)
        for i in range(do):
            out.coef[ds - do + i] -= other.coef[i]
        while (out.coef[0] == 0):
            out.coef.pop(0)
        return poly(str(out))


    def __mul__(self, other):
        if len(self.coef) < len(other.coef):
            self, other = other, self
        out=poly(str([0]*(len(self.coef)+len(other.coef)-2)))
        for i in range(len(self.coef)):
            for j in range(len(other.coef)):
                out.coef[i+j]+= self.coef[i] * other.coef[j]
        return poly(str(out))


    def __floordiv__(self, other):
        outq=poly(str([0]*(len(self.coef)-len(other.coef))))
        outr=poly(str(self.coef))
        i=0
        while outr >= other:
            outq.coef[i]=outr.coef[0]
            outr-=other*outq
            i+=1
        return poly(str(outq))


    def __mod__(self, other):
        outq=poly(str([0]*(len(self.coef)-len(other.coef))))
        outr=poly(str(self.coef))
        i=0
        while outr >= other:
            outq.coef[i]=outr.coef[0]
            outr-=other*outq
            i+=1
        return poly(str(outr))

    def factor_P(self):
        a=poly(str(self))
        g=abs(a.coef[0].num).GCF(abs(a.coef[0].num))
        l=a.coef[0].denum.LCM(a.coef[0].denum)
        for i in range(1, len(a.coef)):
            g=gcd.GCF(abs(a.coef[0].num))
            l=lcm.LCM(a.coef[i].denum)
        return Q(str(g), str(l))

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
