class Circle:
    def __init__(self,radius):
        self.__radius=radius

    def __str__(self):
        return 'Cercle de rayon '+str(self.__radius)

    def __add__(self, other):
        if isinstance(other,Circle):
            return Circle(self.__radius+other.getRadius())
        raise Exception('Opération invalide')

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.__radius<other.getRadius()
        raise Exception('Comparaison invalide')

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.__radius>other.getRadius()
        raise Exception('Comparaison invalide')

    def getRadius(self):
        return self.__radius

if __name__=='__main__':
    c1=Circle(2)
    c2=Circle(3)
    c3=c1+c2
    c4=c1<c2
    c5=c2>c3
    print(c3)