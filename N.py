class N:
    def __init__(self, digit):
        self.digits = []
        if isinstance(digit, (list, tuple)):
            try:
                digit = int("".join( map( str, digit ) )) #костыли, можно и не убирать
            except:
                raise RuntimeError("Digit cannot be presented as integer > 0.")
        if isinstance(digit, int):
            try:
                self.digits = [int(i) for i in str(digit)]
                self.deg = len( str( digit ) )
            except:
                raise RuntimeError("Digit cannot be presented as integer > 0.")

    def __str__(self):
        return str(''.join(map(str, self.digits)))
