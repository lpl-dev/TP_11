class Matrix:
    def __init__(self,data):
        if type(data)==list:
            row_types=[type(row) for row in data]
            if row_types.count(list)==len(data):
                cols_per_row = [len(row) for row in data]
                if len(data[0])==sum(cols_per_row)/len(data):
                    self.data=data
                    self.shape=(len(data),len(data[0]))
                else:
                    raise Exception("La matrice n'est pas valide : toutes les colonnes doivent avoir la même taille")
            else:
                raise Exception("La matrice n'est pas valide : toutes les lignes doivent être des listes")
        else:
            raise Exception("La matrice n'est pas valide")

    def __str__(self):
        render='[\n'
        for row in self.data:
            render+='\t['+' '.join(map(str,row))+']\n'
        render+=']'
        return render

    def __len__(self):
        return self.shape[0]

    def __add__(self, other):
        if isinstance(other,Matrix):
            if self.shape==other.shape:
                return Matrix([[c1+c2 for c1,c2 in zip(r1,r2)] for r1,r2 in zip(self.data, other.data)])
            raise Exception('Opération invalide')
        raise Exception('Opération invalide')

    def __ladd__(self,other):
        return self+other

    def __neg__(self):
        m=[[-col for col in row] for row in self.data]
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
                            e+= self.data[i][j] * other.data[j][k]
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
                return Matrix([[c1<c2 for c1,c2 in zip(r1,r2)] for r1,r2 in zip(self.data, other.data)])
            raise Exception('Condition impossible')
        raise Exception('Condition impossible')

    def __gt__(self, other):
        return Matrix([[not c for c in r] for r in (self<other).data])

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def trace(self):
        if self.shape[0]==self.shape[1]:
            return sum([self.data[i][i] for i in range(self.shape[0])])
        raise Exception("Le calcul de la trace n'est pas possible si la matrice n'est pas carrée")

    def det(self):
        if self.shape[0]==self.shape[1]:
            return self.__det(self)
        raise Exception("Le calcul du déterminant n'est pas possible si la matrice n'est pas carrée")

    def __det(self,array):
        if array.shape==(1,1):
            return array.data[0][0]
        else:
            det=0
            for i in range(array.shape[0]):
                det+=(array.data[i][0] if i%2==0 else -array.data[i][0])*self.__det(Matrix([[c for cidx,c in enumerate(r) if cidx!=0] for ridx,r in enumerate(array.data) if ridx!=i]))
            return det


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
    m3=Matrix([
        [7,8,9,88],
        [5,8,7,-98],
        [-5,-6,3,55],
        [7,8,2,3]
    ])
    print(f'Le déterminant de la matrice :\n{m3} est {m3.det()}')