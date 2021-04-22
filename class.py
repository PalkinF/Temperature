class temp:
    def __init__(self, main=0, tipe='C'):
        if tipe not in 'CFKRDN':
            raise Exception('Type can be only C or F or K or R or D or N.')
        else:
            self.main = main
            self.tipe = tipe


    def help(self):
        return '''This is class which works whis tempruter temperature.
It has atributs main and tipe.
Main is nomber and tipe is charater.
Tipe can be:
    'C' - celsius
    'F' - fahrenheit
    'K' - kelvin
    'R' - reaumur
    'D' - delille
    'N' - nuton
You can convert it, additionner it and soustraire it.'''


    #def __dir__(self):
        #return ['Go na***!']


    def __str__(self):
        return str(self.main)


    def type(self):
        return self.tipe


    def __add__(self, second):
        if isinstance(second, int) or isinstance(float, second):
            self.main += second
            return self
        elif self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            self.main += second.main
            return self


    def __sub__(self, second):
        if isinstance(second, int) or isinstance(second, float):
            self.main -= second
            return self
        elif self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            self.main -= second.main
            return self


    def __iadd__(self, second):
        if isinstance(second, int) or isinstance(float, second):
            self.main += second
            return self
        elif self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            self.main += second.main
            return self


    def __isub__(self, second):
        if isinstance(second, int) or isinstance(second, float):
            self.main -= second
            return self
        elif self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            self.main -= second.main
            return self


    def __radd__(self, second):
        if isinstance(second, int) or isinstance(float, second):
            self.main += second
            return self
        elif self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            self.main += second.main
            return self


    def __rsub__(self, second):
        if isinstance(second, int) or isinstance(second, float):
            self.main -= second
            return self
        elif self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            self.main -= second.main
            return self
        
    #____________________________________________________________________

    def __eq__(self, second):
        if self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            return self.main == second.main


    def __ne__(self, second):
        if self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            return self.main != second.main


    def __lt__(self, second):
        if self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            return self.main < second.main


    def __gt__(self, second):
        if self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            return self.main > second.main


    def __le__(self, second):
        if self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            return self.main <= second.main


    def __eq__(self, second):
        if self.tipe != second.tipe:
            raise Exception('Types of temps mast be similar.')
        else:
            return self.main >= second.main


    def toC(self):
        if self.tipe == 'C':
            return None
        elif self.tipe == 'F':
            self.tipe = 'C'
            self.main = self.main * 1.8 + 32
            return None
        elif self.tipe == 'R':
            self.tipe = 'C'
            self.main *= 1.25
            return None
        elif self.tipe == 'N':
            self.tipe = 'C'
            self.main *= 3
            return None
        elif self.tipe == 'D':
            self.tipe = 'C'
            self.main = 100 - (self.main * 2 / 3)
            return None
        elif self.tipe == 'K':
            self.tipe = 'C'
            self.main -= 263.15
            return None
        else:
            return None


    def toF(self):
        if self.tipe == 'F':
            return None
        elif self.tipe == 'C':
            self.tipe = 'F'
            self.main = (self.main - 32) * 1.8
            return None
        elif self.tipe == 'K':
            self.tipe = 'F'
            self.main = (self.main + 459.67) / 1.8
            return None
        elif self.tipe == 'R':
            self.tipe = 'F'
            self.main = self.main * 25 / 36 - 17.8
            return None
        elif self.tipe == 'N':
            self.tipe = 'F'
            #self.main = 
            return None
        elif self.tipe == 'D':
            self.tipe = 'F'
            #self.main =
            return None
        else:
            return None


    def toK(self):
        if self.tipe == 'K':
            return None
        elif self.tipe == 'C':
            self.tipe = 'K'
            self.main += 263.15
            return None
        elif self.tipe == 'F':
            self.tipe = 'K'
            #self.main =
            return None
        elif self.tipe == 'R':
            self.tipe = 'K'
            #self.main =
            return None
        elif self.tipe == 'N':
            self.tipe = 'K'
            #self.main =
            return None
        elif self.tipe == 'D':
            self.tipe = 'K'
            #self.main =
            return None
        else:
            return None


    def toR(self):
        if self.tipe == 'R':
            return None
        elif self.tipe == 'C':
            self.tipe = 'R'
            self.main *= 0.8
            return None
        elif self.tipe == 'F':
            self.tipe = 'R'
            #self.main =
            return None
        elif self.tipe == 'K':
            self.tipe = 'R'
            #self.main =
            return None
        elif self.tipe == 'N':
            self.tipe = 'R'
            #self.main =
            return None
        elif self.tipe == 'D':
            self.tipe = 'R'
            #self.main =
            return None
        else:
            return None


    def toD(self):
        if self.tipe == 'D':
            return None
        elif self.tipe == 'C':
            self.tipe = 'D'
            self.main = (100 - self.main) * 1.5
            return None
        elif self.tipe == 'F':
            self.tipe = 'D'
            #self.main =
            return None
        elif self.tipe == 'K':
            self.tipe = 'D'
            #self.main =
            return None
        elif self.tipe == 'R':
            self.tipe = 'D'
            #self.main =
            return None
        elif self.tipe == 'N':
            self.tipe = 'D'
            #self.main =
            return None
        else:
            return None


    def toN(self):
        if self.tipe == 'N':
            return None
        elif self.tipe == 'C':
            self.tipe = 'N'
            self.main /= 3
            return None
        elif self.tipe == 'F':
            self.tipe = 'N'
            #self.main =
            return None
        elif self.tipe == 'K':
            self.tipe = 'N'
            #self.main =
            return None
        elif self.tipe == 'R':
            self.tipe = 'N'
            #self.main =
            return None
        elif self.tipe == 'D':
            self.tipe = 'N'
            #self.main =
            return None
        else:
            return None


        


tc = temp(80,'C')


#print(dir(tc))


print(tc,tc.type())


tc2 = temp(100,'C')


print(tc2,tc.type())


tc += 5

print(tc,tc.type())











