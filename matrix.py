# Helper library with simple matrix functions

class Matrix:
    def __init__(self, values, dimensions):
        ''' values is a list of numbers, dimensions is a tuple of ints '''
        self.values = values
        self.dimensions = dimensions
        size = 1
        for i in dimensions:
            size *= i
        if size != len(values):
            raise ValueError("Dimensions don't match values")
        self.degree = len(dimensions)

    def __repr__(self):
        return 'Matrix(%s, %s)' % (self.values,self.dimensions)

    def __str__(self):
        return '%s , %s' % (self.values,self.dimensions)

    def __add__(self,other):
        if type(other) == Matrix:
            if(self.dimensions != other.dimensions):
                raise Exception("Matrices must have same dimensions")
            else:
                result = [i+j for i,j in zip(self.values,other.values)]
                return Matrix(result,self.dimensions)
        elif type(other) == int or type(other) == float:
            result = [i+other for i in self.values]
            return Matrix(result,self.dimensions)
        else:
            raise TypeError("Can only add Matrix or int or float")

    def __iadd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if type(other) == Matrix:
            if(self.dimensions != other.dimensions):
                raise Exception("Matrices must have same dimensions")
            else:
                result = [i-j for i,j in zip(self.values,other.values)]
                return Matrix(result,self.dimensions)
        elif type(other) == int or type(other) == float:
            result = [i-other for i in self.values]
            return Matrix(result,self.dimensions)
        else:
            raise TypeError("Can only subtract Matrix or int or float")
    
    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        ''' Element wise multiplication '''
        if type(other) == Matrix:
            if(self.dimensions != other.dimensions):
                raise Exception("Matrices must have same dimensions")
            else:
                result = [i*j for i,j in zip(self.values,other.values)]
                return Matrix(result,self.dimensions)
        elif type(other) == int or type(other) == float:
            result = [i*other for i in self.values]
            return Matrix(result,self.dimensions)
        else:
            raise TypeError("Can only multiply Matrix or int or float")
    
    def __imul__(self, other):
        return self * other

    def transpose(self):
        if self.degree == 2:
            x, y = self.dimensions
            values = [self.values[j*y+i] for i in range(y) for j in range(x)]
            return Matrix(values,(y,x))
        else:
            raise TypeError("Can only transpose 2D matrices for now")
    
    def matmul(self, other):
        '''Returns a Matrix of the result of matrix multiplication'''
        if self.degree == 2 and other.degree == 2:
            x, y = self.dimensions
            z, w = other.dimensions
            if y == z:
                values = [sum(self.values[i*y+j]*other.values[j*z+k] for j in range(y)) for i in range(x) for k in range(w)]
                return Matrix(values,(x,w))
            else:
                raise Exception("Matrices must have same dimensions")
        else:
            raise TypeError("Can only multiply 2D matrices for now")
        
    def __getitem__(self, index):
        return self.values[index*self.dimensions[0]:(index+1)*self.dimensions[0]]
    
    def flatten(self):
        return Matrix(self.values, (1,len(self.values)))

    def perform(self, func):
        self.values = [func(i) for i in self.values]

    def copy(self):
        return Matrix(self.values, self.dimensions)
    
    def at(self, coor):
        '''Gets element at the specified coordinate'''
        if(len(coor) != self.degree):
            raise Exception("Coordinate must be of same degree as matrix")
        else:
            pos = 0
            for i in range(self.degree-1):
                pos += coor[i]*self.dimensions[i]
            pos += coor[-1]
            return self.values[pos]
    def setat(self, coor, value):
        '''Sets element at the specified coordinate'''
        if(len(coor) != self.degree):
            raise Exception("Coordinate must be of same degree as matrix")
        else:
            pos = 0
            for i in range(self.degree-1):
                pos += coor[i]*self.dimensions[i]
            pos += coor[-1]
            self.values[pos] = value

    def range(dimensions,start=0,step=1,end=None):
        '''Returns a matrix of the given dimensions'''
        product = 1
        for i in dimensions:
            product *= i
        if not end:
            end = step*product + start
        if (end-start)//step != product:
            raise Exception("Invalid range")
        values = list(range(start,end,step))
        return Matrix(values,dimensions)
