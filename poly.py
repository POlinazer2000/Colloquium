class poly:
    def __init__(self, coeflist):
        self.coef = []
        #self.deg =
        for i in coeflist:
            if not isinstance(i, Q):
                self.coef.append( Q( i ) )
            else:
                self.coef.append( i )  # Список коэффицентов, начиная со старшего.
            # self.coef = coeflist # Список коэффицентов, начиная со старшего.
        while not poz_z_d( self.coef[0].num ):
            self.coef.pop( 0 )
        self.deg = len( self.coef )

    def __str__(self):
        coef, out = self.coef, ""
        if self.deg == 0:
            out = "0"
        else:
            for i in range(self.deg):
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
                        out += str( coef[i] ) +'x^'+ str( self.deg - i - 1)


        return out