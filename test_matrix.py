# Test for the matrix class
from matrix import Matrix
if __name__ == "__main__":
    # create a matrix of size 3x3 with 9 elements
    m1 = Matrix([1,2,3,4,5,6,7,8,9],(3,3))
    # create a matrix of size 3x3 with 9 elements
    m2 = Matrix([10,20,30,40,50,60,70,80,90],(3,3))
    # create a matrix of size 2x3 with 6 elements
    m3 = Matrix([1,2,3,4,5,6],(2,3))
    # create a matrix of size 3x3 with 9 elements for i-functions
    m4 = Matrix([1,2,3,4,5,6,7,8,9],(3,3))

    # Test for __str__
    if str(m1) != '[1, 2, 3, 4, 5, 6, 7, 8, 9] , (3, 3)':
        print("Error 1 in __str__ \nExpeted output: [1, 2, 3, 4, 5, 6, 7, 8, 9] , (3, 3) \nActual output: %s" % str(m1))
    
    # Test for __repr__
    if repr(m1) != 'Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], (3, 3))':
        print("Error 2 in __repr__ \nExpeted output: Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], (3, 3)) \nActual output: %s" % repr(m1))
    
    # Test for __add__
    if str(m1+m2) != '[11, 22, 33, 44, 55, 66, 77, 88, 99] , (3, 3)':
        print("Error 3 in __add__ \nExpeted output: [11, 22, 33, 44, 55, 66, 77, 88, 99] , (3, 3) \nActual output: %s" % str(m1+m2))
    
    # Test for __iadd__ using m4
    m4 += m1
    if str(m4) != '[2, 4, 6, 8, 10, 12, 14, 16, 18] , (3, 3)':
        print("Error 4 in __iadd__ \nExpeted output: [2, 4, 6, 8, 10, 12, 14, 16, 18] , (3, 3) \nActual output: %s" % str(m4))

    
    # Test for __iadd__ with int
    m4 += 1
    if str(m4) != '[3, 5, 7, 9, 11, 13, 15, 17, 19] , (3, 3)':
        print("Error 5 in __iadd__ \nExpeted output: [3, 5, 7, 9, 11, 13, 15, 17, 19] , (3, 3) \nActual output: %s" % str(m1))
    
    # Test for __add__ with int
    if str(m1+2) != '[3, 4, 5, 6, 7, 8, 9, 10, 11] , (3, 3)':
        print("Error 6 in __add__ \nExpeted output: [3, 4, 5, 6, 7, 8, 9, 10, 11] , (3, 3) \nActual output: %s" % str(m1+2))
    
    # Test for __sub__
    if str(m1-m2) != '[-9, -18, -27, -36, -45, -54, -63, -72, -81] , (3, 3)':
        print("Error 7 in __sub__ \nExpeted output: [-9, -18, -27, -36, -45, -54, -63, -72, -81] , (3, 3) \nActual output: %s" % str(m1-m2))

    # Test for __isub__ using m4
    m4 -= m1
    if str(m4) != '[2, 3, 4, 5, 6, 7, 8, 9, 10] , (3, 3)':
        print("Error 8 in __isub__ \nExpeted output: [2, 3, 4, 5, 6, 7, 8, 9, 10] , (3, 3) \nActual output: %s" % str(m4))
    
    # Test for __isub__ with int
    m4 -= 1
    if str(m4) != '[1, 2, 3, 4, 5, 6, 7, 8, 9] , (3, 3)':
        print("Error 9 in __isub__ \nExpeted output: [1, 2, 3, 4, 5, 6, 7, 8, 9] , (3, 3) \nActual output: %s" % str(m4))
    
    # Test for __sub__ with int
    if str(m2-m1) != '[9, 18, 27, 36, 45, 54, 63, 72, 81] , (3, 3)':
        print("Error 10 in __sub__ with int \nExpeted output: [9, 18, 27, 36, 45, 54, 63, 72, 81] , (3, 3) \nActual output: %s" % str(m2-m1))


    # Test for __mul__
    if str(m1*m2) != '[10, 40, 90, 160, 250, 360, 490, 640, 810] , (3, 3)':
        print("Error 11 in __mul__ \nExpeted output: [10, 40, 90, 160, 250, 360, 490, 640, 810] , (3, 3) \nActual output: %s" % str(m1*m2))

    # Test for __imul__ using m4
    m4 *= m1
    if str(m4) != '[1, 4, 9, 16, 25, 36, 49, 64, 81] , (3, 3)':
        print("Error 12 in __imul__ \nExpeted output: [1, 4, 9, 16, 25, 36, 49, 64, 81] , (3, 3) \nActual output: %s" % str(m4))
    
    # Test for __imul__ with int
    m4 *= 2
    if str(m4) != '[2, 8, 18, 32, 50, 72, 98, 128, 162] , (3, 3)':
        print("Error 13 in __imul__ \nExpeted output: [2, 8, 18, 32, 50, 72, 98, 128, 162] , (3, 3) \nActual output: %s" % str(m4))

    # Test for __mul__ with int
    if str(m1*2) != '[2, 4, 6, 8, 10, 12, 14, 16, 18] , (3, 3)':
        print("Error 14 in __mul__ \nExpeted output: [2, 4, 6, 8, 10, 12, 14, 16, 18] , (3, 3) \nActual output: %s" % str(m1*2))

    # Test for transpose
    if str(m1.transpose()) != '[1, 4, 7, 2, 5, 8, 3, 6, 9] , (3, 3)':
        print("Error 15 in transpose \nExpeted output: [1, 4, 7, 2, 5, 8, 3, 6, 9] , (3, 3) \nActual output: %s" % str(m1.transpose()))

    # Test for transpose for non square matrix
    if str(m3.transpose()) !=  '[1, 4, 2, 5, 3, 6] , (3, 2)':
        print("Error 16 in transpose \nExpeted output: [1, 4, 2, 5, 3, 6] , (3, 2) \nActual output: %s" % str(m3.transpose()))

    # Test for matrix multiplication
    if str(m1.matmul(m1)) != '[30, 36, 42, 66, 81, 96, 102, 126, 150] , (3, 3)':
        print("Error 17 in matrix multiplication \nExpeted output: [30, 36, 42, 66, 81, 96, 102, 126, 150] , (3, 3) \nActual output: %s" % str(m1.matmul(m1)))
    
    # Test for matrix multiplication for non square matrix
    if str(m3.matmul(m1)) != '[30, 36, 42, 66, 81, 96] , (2, 3)':
        print("Error 18 in matrix multiplication \nExpeted output: [30, 36, 42, 66, 81, 96] (2, 3) \nActual output: %s" % str(m3.matmul(m1)))

    # Test for getItem
    if str(m1[1]) != '[4, 5, 6]':
        print("Error 19 in getItem \nExpeted output: [4, 5, 6] \nActual output: %s" % str(m1[1]))

    # Test to get element at some index
    if m1[1][1] != 5:
        print("Error 20 in getItem \nExpeted output: 5 \nActual output: %s" % m1[1][1])
    
    # Test for flatten
    if str(m1.flatten()) != '[1, 2, 3, 4, 5, 6, 7, 8, 9] , (1, 9)':
        print("Error 21 in flatten \nExpeted output: [1, 4, 7, 2, 5, 8, 3, 6, 9] , (1, 9) \nActual output: %s" % str(m1.flatten()))

    # Test for flatten for non square matrix
    if str(m3.flatten()) != '[1, 2, 3, 4, 5, 6] , (1, 6)':
        print("Error 22 in flatten \nExpeted output: [1, 2, 3, 4, 5, 6] , (1, 6) \nActual output: %s" % str(m3.flatten()))

    # Test for perform function on matrix m4
    m4.perform(lambda x: x//2)
    if str(m4) != '[1, 4, 9, 16, 25, 36, 49, 64, 81] , (3, 3)':
        print("Error 23 in perform \nExpeted output: [1, 4, 9, 16, 25, 36, 49, 64, 81] , (3, 3) \nActual output: %s" % str(m4))

    # Test for the at function
    if m1.at((1, 1)) != 5:
        print("Error 24 in at \nExpeted output: 5 \nActual output: %s" % m1.at(1, 1))

    # Test for the set function on matrix m4
    m4.setat((1, 1), 10)
    if str(m4) != '[1, 4, 9, 16, 10, 36, 49, 64, 81] , (3, 3)':
        print("Error 25 in set \nExpeted output: [1, 4, 9, 16, 10, 36, 49, 64, 81] , (3, 3) \nActual output: %s" % str(m4))

    # Test for range function without range argument
    m5 = Matrix.range((3,3))
    if str(m5) != '[0, 1, 2, 3, 4, 5, 6, 7, 8] , (3, 3)':
        print("Error 26 in range \nExpeted output: [0, 1, 2, 3, 4, 5, 6, 7, 8] , (3, 3) \nActual output: %s" % str(m5))
    
    # Test for range function with all range argument
    m5 = Matrix.range((3,3),start=2,end=11,step=1 )
    if str(m5) != '[2, 3, 4, 5, 6, 7, 8, 9, 10] , (3, 3)':
        print("Error 27 in range \nExpeted output: [2, 3, 4, 5, 6, 7, 8, 9, 10] , (3, 3) \nActual output: %s" % str(m5))

    # Test for range function with step argument
    m5 = Matrix.range((3,3),step=2 )
    if str(m5) != '[0, 2, 4, 6, 8, 10, 12, 14, 16] , (3, 3)':
        print("Error 28 in range \nExpeted output: [0, 2, 4, 6, 8, 10, 12, 14, 16] , (3, 3) \nActual output: %s" % str(m5))

    # Test for range function with start argument
    m5 = Matrix.range((3,3),start=2 )
    if str(m5) != '[2, 3, 4, 5, 6, 7, 8, 9, 10] , (3, 3)':
        print("Error 29 in range \nExpeted output: [2, 3, 4, 5, 6, 7, 8, 9, 10] , (3, 3) \nActual output: %s" % str(m5))
    
    # Test for range function with start and step argument
    m5 = Matrix.range((3,3),start=2,step=2 )
    if str(m5) != '[2, 4, 6, 8, 10, 12, 14, 16, 18] , (3, 3)':
        print("Error 30 in range \nExpeted output: [2, 4, 6, 8, 10, 12, 14, 16, 18] , (3, 3) \nActual output: %s" % str(m5))


    # Speed test
    import time
    # Create a range matrix with size 100 x 100
    m6 = Matrix.range((100,100))
    start = time.time()
    # Perform the matrix multiplication
    m6.matmul(m6)
    end = time.time()
    print("Time taken for matrix multiplication: %s" % (end-start))

    
    # The tests below this are not implemented yet
    exit(0)