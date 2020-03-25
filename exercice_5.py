class Matrix:
    def __init__(self,data):
        if type(data)==list:
            row_types=[type(row) for row in data]
            if row_types.count(list)==len(data):
                cols_per_row = [len(row) for row in data]
                if len(data[0])==sum(cols_per_row)/len(data):
                    self.__data=data
                    self.shape=(len(data),len(data[0]))
                else:
                    raise Exception("La matrice n'est pas valide : toutes les colonnes doivent avoir la même taille")
            else:
                raise Exception("La matrice n'est pas valide : toutes les lignes doivent être des listes")
        else:
            raise Exception("La matrice n'est pas valide")

    def __str__(self):
        render='[\n'
        for row in self.__data:
            render+='\t['+' '.join(map(str,row))+']\n'
        render+=']'
        return render

    def __len__(self):
        return self.shape[0]

    def __add__(self, other):
        if isinstance(other,Matrix):
            if self.shape==other.shape:
                return Matrix([[c1+c2 for c1,c2 in zip(r1,r2)] for r1,r2 in zip(self.__data,other.__data)])
            raise Exception('Opération invalide')
        raise Exception('Opération invalide')

    def __ladd__(self,other):
        return self+other

    def __neg__(self):
        m=[[-col for col in row] for row in self.__data]
        return Matrix(m)

    def __sub__(self,other):
        return self+(-other)

    def __lsub__(self,other):
        return self-other

    def __mul__(self,other):
        if isinstance(other, Matrix):
            if self.shape[1]==other.shape[0]:
                m=[]
                for i in range(self.shape[0]):
                    row=[]
                    for k in range(other.shape[1]):
                        e=0
                        for j in range(self.shape[1]):
                            e+=self.__data[i][j]*other.__data[j][k]
                        row.append(e)
                    m.append(row)
                return Matrix(m)
            raise Exception('Les tailles des matrices ne sont pas valides pour la multiplication')
        raise Exception('Opération invalide')

    def __lmul__(self,other):
        return self*other

    def __lt__(self,other):
        if isinstance(other,Matrix):
            if self.shape==other.shape:
                return Matrix([[c1<c2 for c1,c2 in zip(r1,r2)] for r1,r2 in zip(self.__data,other.__data)])
            raise Exception('Condition impossible')
        raise Exception('Condition impossible')

    def __gt__(self, other):
        return Matrix([[not c for c in r] for r in (self<other).__data])

    def transpose(self):
        return Matrix([[self.__data[j][i] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def trace(self):
        if self.shape[0]==self.shape[1]:
            return sum([self.__data[i][i] for i in range(self.shape[0])])
        raise Exception("Le calcul de la trace n'est pas possible si la matrice n'est pas carrée")

if __name__=='__main__':
    m1=Matrix([
        [1,2],
        [8,5]
    ])
    m2=Matrix([
        [8, 2],
        [-5,7]
    ])
    print(f'm1={m1}')
    print(f'm2={m2}')
    print(f'm1+m2={m1+m2}')
    m1+=m2
    print(f'm1+=m2={m1}')
    print(f'm1-m2={m1-m2}')
    m1-=m2
    print(f'm1-=m2{m1}')
    print(f'm1*m2={m1*m2}')
    m1*=m2
    print(f'm1*=m2={m1}')
    print(f'm1<m2={m1<m2}')
    print(f'm1>m2={m1>m2}')
