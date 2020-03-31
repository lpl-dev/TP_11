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
                    raise Exception("Matrice invalide : colonnes de tailles différentes")
            else:
                raise Exception("Matrice invalide : liste uniquement pour les lignes")
        else:
            raise Exception("Matrice invalide : liste uniquement")

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
            raise Exception("Impossible d'effectuer l'opération : matrices de tailles différentes")
        raise Exception("Impossible d'effectuer l'opération : objets de types différents")

    def __radd__(self, other):
        return self+other

    def __neg__(self):
        return Matrix([[-col for col in row] for row in self.data])

    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self, other):
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
            raise Exception("Impossible d'effectuer l'opération : tailles de matrice invalides")
        elif type(other) in [int, float]:
            return Matrix([[other*c for c in r] for r in self.data])
        raise Exception("Impossible d'effectuer l'opération : terme multiplicateur invalide")

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        if type(other) in [int, float]:
            if other!=0:
                return 1/other * self
            raise Exception("Impossible d'effectuer l'opération : division par 0")
        raise Exception("Impossible d'effectuer l'opération : terme diviseur invalide")

    def __pow__(self,other):
        if type(other)==int:
            if self.shape[0]==self.shape[1]:
                if other==0:
                    return Matrix([[(1 if c==r else 0) for c in range(self.shape[0])] for r in range(self.shape[0])])
                elif other==1:
                    return self
                elif other==-1:
                    return self.inv()
                elif other>1:
                    array=self
                    for _ in range(other-1):
                        array*=self
                    return array
                raise Exception("Impossible d'effectuer l'opération : puissance invalide")
            raise Exception("Impossible d'effectuer l'opération : matrice non carrée")
        raise Exception("Impossible d'effectuer l'opération : puissance invalide")

    def __lt__(self,other):
        if isinstance(other,Matrix):
            if self.shape==other.shape:
                return Matrix([[c1<c2 for c1,c2 in zip(r1,r2)] for r1,r2 in zip(self.data, other.data)])
            raise Exception('Condition impossible : matrices de tailles différentes')
        raise Exception('Condition impossible : objets de types différents')

    def __gt__(self, other):
        return Matrix([[not c for c in r] for r in (self<other).data])

    def transpose(self):
        """
        Retourne la transposée d'une matrice
        :return: Matrix object
        """
        return Matrix([[self.data[j][i] for j in range(self.shape[1])] for i in range(self.shape[0])])

    @property
    def T(self):
        return self.transpose()

    def trace(self):
        """
        Retourne la trace d'une matrice carrée
        :return: int
        """
        if self.shape[0]==self.shape[1]:
            return sum([self.data[i][i] for i in range(self.shape[0])])
        raise Exception("Impossible de calculer la trace : matrice non carrée")

    def det(self):
        """
        Calcul le déterminant d'une matrice carrée
        :return: int
        """
        if self.shape[0] == self.shape[1]:
            return self.__det(self)
        raise Exception("Impossible de calculer le déterminant : matrice non carrée")

    def __det(self, array):
        if array.shape == (1, 1):
            return array.data[0][0]
        else:
            det = 0
            for i in range(array.shape[0]):
                det += (-1)**i * array.data[i][0] * self.__det(Matrix([[c for cidx, c in enumerate(r) if cidx != 0] for ridx, r in enumerate(array.data) if ridx != i]))
            return det

    def adj(self):
        """
        Retourne la comatrice d'une matrice carrée
        :return: Matrix object
        """
        if self.shape[0]==self.shape[1]:
            array=[]
            for i in range(self.shape[0]):
                row=[]
                for j in range(self.shape[1]):
                    row.append((-1)**(i+j) * Matrix([[c for cidx, c in enumerate(r) if cidx != j] for ridx, r in enumerate(self.data) if ridx != i]).det())
                array.append(row)
            return Matrix(array)
        raise Exception("Impossible de calculer la comatrice : matrice non carrée")

    def inv(self):
        """
        Retourne l'inverse d'une matrice carrée si possible
        :return: Matrix object
        """
        det=self.det()
        if det!=0:
            return 1/det * self.adj().T
        raise Exception("Impossible d'inverser la matrice : déterminant nul")

if __name__=='__main__':
    m1=Matrix([
        [1,2],
        [8,5]
    ])
    m2 = Matrix([
        [8, 2],
        [-5,7]
    ])
    print(f'm1={m1}\n\n'+'-'*10+'\n')
    print(f'm2={m2}\n\n'+'-'*10+'\n')
    print(f'm1+m2={m1+m2}\n\n'+'-'*10+'\n')
    print(f'm1-m2={m1-m2}\n\n'+'-'*10+'\n')
    print(f'm1*m2={m1*m2}\n\n'+'-'*10+'\n')
    print(f'm1<m2={m1<m2}\n\n'+'-'*10+'\n')
    print(f'm1>m2={m1>m2}\n\n'+'-'*10+'\n')
    print(f'L\'inverse de la matrice :\n{m1}\nest :\n{m1.inv()}\n\n'+'-'*10+'\n')
    m3 = Matrix([
        [7, 8, 9, 88],
        [5, 8, 7, -98],
        [-5, -6, 3, 55],
        [7, 8, 2, 3]
    ])
    print(f'Le déterminant de la matrice :\n{m3}\nest : {m3.det()}')