
class Z():
    def __init__(self, digit):
        digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
        try:
            self.sign = False
            if (digit[0] == '-'):
                self.sign = True
                digit = digit[1:]
            self.digits = [int(i) for i in digit]
        except:
            raise RuntimeError("Digit cannot be presented as integer.")

    def __str__(self):
        out = self.sign and '-' or ""
        out += str(''.join( map( str, self.digits )))
        return out
