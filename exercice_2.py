class Complex:
    def __init__(self,real,im):
        self.__real=real
        self.__im=im

    def __str__(self):
        return (str(self.__real) if self.__real!=0 else ('0' if self.__im==0 else ''))+('+' if self.__im>0 and self.__real!=0 else '')+(str(self.__im)+'i' if abs(self.__im)!=1 and self.__im!=0 else ('i' if self.__im==1 else ('-i' if self.__im==-1 else '')))

    def __add__(self,other):
        if isinstance(other,Complex):
            return Complex(self.__real+other.getReal(),self.__im+other.getIm())
        raise Exception('Opération invalide')

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__real-other.getReal(),self.__im-other.getIm())
        raise Exception('Opération invalide')

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__real*other.getReal()-self.__im*other.getIm(),self.__real*other.getIm()+self.__im*other.getReal())
        raise Exception('Opération invalide')

    def __truediv__(self, other):
        if isinstance(other, Complex):
            r=self*other.conjug()
            d=other.getReal()**2+other.getIm()**2
            return Complex(r.getReal()/d,r.getIm()/d)
        raise Exception('Opération invalide')

    def __abs__(self):
        return (self.__real**2+self.__im**2)**0.5

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.__real==other.getReal() and self.__im==other.getReal()
        raise Exception('Condition invalide')

    def __ne__(self, other):
        if isinstance(other, Complex):
            return not self==other
        raise Exception('Condition invalide')

    def getReal(self):
        return self.__real

    def getIm(self):
        return self.__im

    def conjug(self):
        return Complex(self.__real,-self.__im)

if __name__=='__main__':
    cplx1=Complex(1,1)
    cplx2=Complex(1,1)
    print(cplx1+cplx2)
    print(cplx1-cplx2)
    print(cplx1*cplx2)
    print(cplx1/cplx2)
    print(cplx1==cplx2)
    print(cplx1!=cplx2)