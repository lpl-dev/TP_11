class Duration:
    def __init__(self,h,m,s):
        self.__h=h
        self.__m=m
        self.__s=s

    def __str__(self):
        return f'{self.__h}h{self.__m}m{self.__s}s'

    def __add__(self, other):
        if isinstance(other, Duration):
            ts=(self.__s+other.__s)%60
            tm=((self.__m+other.__m)+(self.__s+other.__s)//60)%60
            th=self.__h+other.__h+((self.__m+other.__m)+(self.__s+other.__s)//60)//60
            return Duration(th,tm,ts)
        raise Exception('Opération invalide')

if __name__=='__main__':
    d1=Duration(13,15,50)
    d2=Duration(2,45,20)
    print(f'd1={d1}, d2={d2}')
    print(f'd1+d2={d1+d2}')