import matrix
import unittest

class Test_Matrix(unittest.TestCase):
    
    ############################
    # Test matrix math methods #
    ############################
    
    def test_determinant(self):
        m = matrix.Matrix([[1, 2],[3, 4]])
        
        self.assertTrue(m.determinant() == -2)
    
    def test_trace(self):
        m = matrix.Matrix([[1, 2, 4, 5],[6, 7, 8, 9],[10,11,12, 13],[14,15,16,17]])
        
        self.assertTrue(m.trace() == 37)
    
    def test_inverse(self):
        m = matrix.Matrix([[1, 2],[3, 4]])
        
        self.assertTrue(m.inverse().g == [[-2.0, 1.0], [1.5, -0.5]])

    def test_T(self):
        m = matrix.Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
        
        self.assertTrue(m.T().g == [[1, 5], [2, 6], [3, 7], [4, 8]])
    
    def test_is_square(self):

        self.assertTrue(matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).is_square() == True)
        self.assertTrue(matrix.Matrix([[1, 2],[3, 4]]).is_square() == True)
        self.assertTrue(matrix.Matrix([[1, 2, 3], [4, 5, 6]]).is_square() == False)
        self.assertTrue(matrix.Matrix([[1],[3]]).is_square() == False)       

    #############################
    # Test Operator Overloading #
    #############################

    def test_getitem(self):
        m = matrix.Matrix([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
        
        self.assertTrue(m[0][0] == 1)
        self.assertTrue(m[0][1] == 2)
        self.assertTrue(m[0][2] == 3)
        self.assertTrue(m[1][0] == 4)
        self.assertTrue(m[1][1] == 5)
        self.assertTrue(m[1][2] == 6)
        self.assertTrue(m[2][0] == 7)
        self.assertTrue(m[2][1] == 8)
        self.assertTrue(m[2][2] == 9)

    #def test_repr(self):
       
    def test_add(self):
        m1 = matrix.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        m2 = matrix.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

        self.assertTrue((m1 + m2).g == [[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24]])
    
    def test_neg(self):
        m = matrix.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        
        self.assertTrue((-m).g == [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12]])
    
    def test_sub(self):
        m1 = matrix.Matrix([[ 2, 4, 6, 8], [10,12,14,16], [18,20,22,24]])
        m2 = matrix.Matrix([[ 1, 2, 3, 4], [ 5, 6, 7, 8], [ 9,10,11,12]])

        self.assertTrue((m1 - m2).g == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    def test_mul(self):
        m1 = matrix.Matrix([[ 1, 2, 3, 4], [ 5, 6, 7, 8]])
        m2 = matrix.Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])

        self.assertTrue((m1 * m2).g == [[50, 60], [114, 140]])
    
    def test_rmul(self):
        m = matrix.Matrix([[1, 2, 3, 4],[5, 6, 7, 8]])

        self.assertTrue((2 * m).g == [[2, 4, 6, 8], [10, 12, 14, 16]])