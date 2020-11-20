import numpy as np
import matrix
import unittest

class Test_Matrix(unittest.TestCase):
    
    ############################
    # Test matrix math methods #
    ############################
    
    def test_determinant(self):
        m = matrix.Matrix([[-1, 2, 3, 4],[5, -6,7, 8],[9, 10, -11, 12],[13,14,15,-16]])
        print("\n\n####################")
        print("# test_determinant #")
        print("####################")
        print("\nMatrix\n")
        print(m)    
        print("Determinant\n")
        print(m.determinant())  
        print("\n")     
        self.assertAlmostEqual(m.determinant(), -36416)

    def test_trace(self):
        m = matrix.Matrix([[-1, 2, 3, 4],[5, -6,7, 8],[9, 10, -11, 12],[13,14,15,-16]])
        print("\n\n####################")
        print("#    test_trace    #")
        print("####################")
        print("\nMatrix\n")
        print(m)    
        print("Trace\n")
        print(m.trace())   
        print("\n")          
        self.assertEqual(m.trace(), -34)

    def test_inverse(self):
        m = matrix.Matrix([[-1, 2, 3, 4],[5, -6,7, 8],[9, 10, -11, 12],[13,14,15,-16]])
        print("\n\n####################")
        print("#   test_inverse   #")
        print("####################")
        print("\nMatrix\n")
        print(m)    
        print("Inverse\n")
        print(np.round(m.inverse().g, 3))  
        print("\n")          

        self.assertTrue(np.array_equal(np.round(m.inverse().g, 3) , np.round(np.array([ [-297/2276, 137/2276, 73/2276, 49/2276],
                                                                                        [ 269/2276, -63/1138, 45/2276, 19/1138],
                                                                                        [ 217/2276,  57/2276,-61/2276, 37/2276],
                                                                                        [ 395/4552, 109/4552, 83/4552,-69/4552]]), 3)))
    
    def test_T(self):
        m = matrix.Matrix([[-1, 2, 3, 4],[5, -6,7, 8],[9, 10, -11, 12],[13,14,15,-16]])
        print("\n\n####################")
        print("#       test_T     #")
        print("####################")
        print("\nMatrix\n")
        print(m)    
        print("T\n")
        print(m.T().g)  
        print("\n")    

        self.assertTrue(np.array_equal(m.T().g , np.array([ [-1,  5,  9, 13],
                                                            [ 2, -6, 10, 14],
                                                            [ 3,  7,-11, 15],
                                                            [ 4,  8, 12,-16]])))

    def test_is_square(self):
        print("\n\n####################")
        print("#  test_is_square  #")
        print("####################")
        print("\nMatrix\n")
        m1 = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(m1.g)    
        print("\n") 
        print(m1.is_square())      
        self.assertTrue(m1.is_square() == True)
        print("\nMatrix\n")
        m2 = matrix.Matrix([[1, 2],[3, 4]])
        print(m2.g)    
        print("\n") 
        print(m2.is_square())      
        self.assertTrue(m2.is_square() == True)
        print("\nMatrix\n")
        m3 = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
        print(m3.g)    
        print("\n") 
        print(m3.is_square())      
        self.assertTrue(m3.is_square() == False)
        print("\nMatrix\n")
        m4 = matrix.Matrix([[1],[3]])
        print(m4.g)    
        print("\n") 
        print(m4.is_square())      
        self.assertTrue(m4.is_square() == False)       
    
    #############################
    # Test Operator Overloading #
    #############################

    def test_getitem(self):
        m = matrix.Matrix([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
        print("\n\n####################")
        print("#   test_getitem   #")
        print("####################")
        print("\nMatrix\n")
        print(m.g)    
        print("\n")         
        print("m[0][0] = " + str(m[0][0])) 
        self.assertTrue(m[0][0] == 1)
        print("m[0][1] = " + str(m[0][1])) 
        self.assertTrue(m[0][1] == 2)
        print("m[0][2] = " + str(m[0][2])) 
        self.assertTrue(m[0][2] == 3)
        print("m[1][0] = " + str(m[1][0])) 
        self.assertTrue(m[1][0] == 4)
        print("m[1][1] = " + str(m[1][1])) 
        self.assertTrue(m[1][1] == 5)
        print("m[1][2] = " + str(m[1][2])) 
        self.assertTrue(m[1][2] == 6)
        print("m[2][0] = " + str(m[2][0])) 
        self.assertTrue(m[2][0] == 7)
        print("m[2][1] = " + str(m[2][1])) 
        self.assertTrue(m[2][1] == 8)
        print("m[2][2] = " + str(m[2][2])) 
        self.assertTrue(m[2][2] == 9)
    
    def test_add(self):
        m1 = matrix.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        m2 = matrix.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        print("\n\n####################")
        print("#     test_add     #")
        print("####################")
        print("\nMatrix 1\n")
        print(m1.g)    
        print("\n")    
        print("\nMatrix 2\n")
        print(m2.g)    
        print("\n")    
        print("\nMatrix sum\n")
        print((m1 + m2).g)    
        print("\n")
        self.assertTrue(np.array_equal((m1 + m2).g , np.array([[2, 4, 6, 8], 
                                                               [10, 12, 14, 16], 
                                                               [18, 20, 22, 24]])))

    def test_neg(self):
        m = matrix.Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        print("\n\n####################")
        print("#     test_neg     #")
        print("####################")
        print("\nMatrix\n")
        print(m.g)    
        print("\n")    
        print("\nMatrix neg\n")
        print((-m).g)    
        print("\n")   

        self.assertTrue(np.array_equal((-m).g , np.array([[-1, -2, -3, -4], 
                                                           [-5, -6, -7, -8], 
                                                           [-9, -10, -11, -12]])))

    def test_sub(self):
        m1 = matrix.Matrix([[ 2, 4, 6, 8], [10,12,14,16], [18,20,22,24]])
        m2 = matrix.Matrix([[ 1, 2, 3, 4], [ 5, 6, 7, 8], [ 9,10,11,12]])
        print("\n\n####################")
        print("#     test_sub     #")
        print("####################")
        print("\nMatrix 1\n")
        print(m1.g)    
        print("\n")    
        print("\nMatrix 2\n")
        print(m2.g)    
        print("\n")    
        print("\nMatrix sub\n")
        print((m1 - m2).g)    
        print("\n")
        self.assertTrue(np.array_equal((m1 - m2).g , np.array([ [1, 2, 3, 4], 
                                                                [5, 6, 7, 8], 
                                                                [9, 10, 11, 12]])))

    def test_mul(self):
        m1 = matrix.Matrix([[ 1, 2, 3, 4], [ 5, 6, 7, 8]])
        m2 = matrix.Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
        print("\n\n####################")
        print("#     test_mul     #")
        print("####################")
        print("\nMatrix 1\n")
        print(m1.g)    
        print("\n")    
        print("\nMatrix 2\n")
        print(m2.g)    
        print("\n")    
        print("\nMatrix mul\n")
        print((m1 * m2).g)    
        print("\n")

        self.assertTrue(np.array_equal((m1 * m2).g , np.array([[50, 60], [114, 140]])))

    def test_rmul(self):
        m = matrix.Matrix([[1, 2, 3, 4],[5, 6, 7, 8]])
        print("\n\n####################")
        print("#     test_rmul    #")
        print("####################")
        print("\nMatrix\n")
        print(m.g)    
        print("\n")    
        print("\nMatrix rmul\n")
        print((2*m).g)    
        print("\n")    

        self.assertTrue(np.array_equal((2*m).g , np.array([[2, 4, 6, 8], [10, 12, 14, 16]])))
