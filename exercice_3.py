class Rational:
    def __init__(self,num,denum):
        self.__num=num
        self.__denum=denum

    def __str__(self):
        return str(self.__num)+'/'+str(self.__denum)

    def __add__(self, other):
        if isinstance(other,Rational):
            if self.__denum==other.__denum:
                return Rational(self.__num+other.__num,self.__denum)
            else:
                r=Rational(self.__num*other.__denum+self.__denum*other.__num,self.__denum*other.__denum)
                r.simplify()
                return r
        raise Exception('Opération invalide')

    def __neg__(self):
        return Rational(-self.__num,self.__denum)

    def __sub__(self, other):
        if isinstance(other, Rational):
            return self+(-other)
        raise Exception('Opération invalide')

    def __mul__(self,other):
        if isinstance(other, Rational):
            r=Rational(self.__num*other.__num,self.__denum*other.__denum)
            r.simplify()
            return r
        elif type(other) in [int,float]:
            return Rational(self.__num*other,self.__denum)
        raise Exception('Opération invalide')

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return self*other.reverse()
        elif type(other) in [int,float]:
            return Rational(self.__num,self.__denum*other)
        raise Exception('Opération invalide')

    def __pow__(self,other):
        if type(other) in [int,float]:
            r=Rational(self.__num**other,self.__denum**other)
            r.simplify()
            return r
        raise Exception('Opération invalide')

    def __eq__(self, other):
        if isinstance(other, Rational):
            self.simplify()
            other.simplify()
            return self.__num==other.__num and self.__denum==other.__denum
        elif type(other) in [int,float]:
            return self.__num/self.__denum==other
        raise Exception('Condition invalide')

    def __ne__(self, other):
        return not self==other

    def __pgcd(self,a,b):
        mx=max(a,b)
        mn=min(a,b)
        r=mx%mn
        while r!=0:
            mx=mn
            mn=r
            r=mx%mn
        return mn

    def __ppcm(self,a,b):
        return a*b/self.__pgcd(a,b)

    def simplify(self):
        pgcd=self.__pgcd(self.__num,self.__denum)
        self.__num/=pgcd
        self.__denum/=pgcd

    def reverse(self):
        return Rational(self.__denum,self.__num)

if __name__=='__main__':
    r1=Rational(3,2)
    r2=Rational(8,2)
    print(f'r1={r1}, r2={r2}')
    print(f'-r1={-r1}, -r2={-r2}')
    print(f'r1+r2 = {r1+r2}')
    print(f'r1-r2 = {r1-r2}')
    print(f'r1*r2 = {r1*r2}')
    print(f'r1/r2 = {r1/r2}')
    print(f'r1**2 : {r1**2}')
    print(f'r1==r2 : {r1==r2}')
    print(f'r1!=r2 : {r1!=r2}')
