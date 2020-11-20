import numbers
import numpy as np

class Matrix(object):

    # Constructor
    def __init__(self, grid):

        if not isinstance(grid, (list, np.ndarray)):
            raise ValueError("Non-valid Matrix, make sure to enter a valid list.")

        self.g = np.array(grid)
        self.h = len(grid)
        self.w = 1

        if isinstance(grid[0], list):
            self.w = len(grid[0])

        #if any(not isinstance(self.g[i][j], (int, float)) for j in range(0, self.w) for i in range(0, self.h)):
        #    raise ValueError("Non-valid Matrix, make sure to enter just int or float values.")

    ###############################
    # Primary matrix math methods #
    ###############################
 
    def determinant(self):
        """
        Calculates the determinant of a matrix.
        """
        if not self.is_square():
            raise ValueError("Cannot calculate determinant of non-square matrix.")
  
        return np.linalg.det(self.g)
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise ValueError("Cannot calculate the trace of a non-square matrix.")
        else:            
            return np.trace(self.g)

    def inverse(self):
        """
        Calculates the inverse of a Matrix.
        """
        if not self.is_square():
            raise ValueError("Non-square Matrix does not have an inverse.")
        if self.determinant() == 0:
            raise ValueError("Non-invertible Matrix, because the determinant is zero.")
        else:   
            return Matrix(np.linalg.inv(self.g))
        
    def T(self):  
        """
        Returns a transposed copy of this Matrix.
        """
        return Matrix(np.transpose(self.g))

    def is_square(self):
        return self.h == self.w

    ##############################
    # Begin Operator Overloading #
    ##############################
    
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be added if the dimensions are the same") 
        else:        
            return Matrix(self.g + other.g)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        return Matrix(self.g * -1)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be subtracted if the dimensions are the same") 
        else:        
            return Matrix(self.g - other.g)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        if self.w != other.h:
            raise ValueError("Matrices can only be multiplied if the both matrix are same height") 
        else:
            mul = [[1.0 for _ in range(other.w)] for __ in range(self.h)]
            for i in range(self.h):
                for j in range(other.w):
                    dot_product = 0
                    for k in range(other.h):
                        dot_product += self[i][k] * other[k][j]
                    mul[i][j] = dot_product            
                    
            return Matrix(mul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass

            return Matrix(self.g * other)
            

           
            
            