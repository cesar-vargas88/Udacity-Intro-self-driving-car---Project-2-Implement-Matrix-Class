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
        m = matrix.Matrix([[1, 2],[3, 4]])
        
        self.assertTrue(m.trace() == 5)
    
    def test_inverse(self):
        m = matrix.Matrix([[1, 2],[3, 4]])
        
        self.assertTrue(m.inverse().g == [[-2.0, 1.0], [1.5, -0.5]])

    def test_T(self):
        m = matrix.Matrix([[1, 2],[3, 4]])
        
        self.assertTrue(m.T().g == [[1, 3], [2, 4]])
    
    def test_is_square(self):
        m = matrix.Matrix([[1, 2],[3, 4]])
        grid = [[1, 3], [2, 4]]

        self.assertTrue(m.is_square() == (len(grid) == len(grid[0])))
            

    #############################
    # Test Operator Overloading #
    #############################

    def test_getitem(self):
        m = matrix.Matrix([[1, 2],[3, 4]])
        
        self.assertTrue(m[0][0] == m.g[0][0])

    #def test_repr(self):
       
    def test_add(self):
        m1 = matrix.Matrix([[1, 2],[3, 4]])
        m2 = matrix.Matrix([[1, 2],[3, 4]])

        self.assertTrue((m1 + m2).g == [[2, 4],[6, 8]])
    
    def test_neg(self):
        m = matrix.Matrix([[1, 2],[3, 4]])
        
        self.assertTrue((-m).g == [[-1, -2],[-3, -4]])
    
    def test_sub(self):
        m1 = matrix.Matrix([[2, 4],[6, 8]])
        m2 = matrix.Matrix([[1, 2],[3, 4]])

        self.assertTrue((m1 - m2).g == [[1, 2],[3, 4]])
    
    def test_mul(self):
        m1 = matrix.Matrix([[1, 2],[3, 4]])
        m2 = matrix.Matrix([[1, 2],[3, 4]])

        self.assertTrue((m1 * m2).g == [[7.0, 10.0],[15.0, 22.0]])
    
    def test_rmul(self):
        m1 = matrix.Matrix([[1, 2],[3, 4]])
        m2 = matrix.Matrix([[1, 2],[3, 4]])

        self.assertTrue((m1 * m2).g == [[7.0, 10.0],[15.0, 22.0]])
    