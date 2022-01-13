# Test for the helper functions
from helper import *

if __name__ == "__main__":
    # create a matrix of size 2x2 with 4 elements
    m1 = Matrix([1,2,3,4],(2,2))

    # Test for the sigmoid function
    sigmoid(m1)
    # sigmoid of 1, 2, 3, 4: 0.7310585786300049, 0.8807970779778823, 0.9525741268224334, 0.9820137900379085
    if str(m1) != "[0.7310585786300049, 0.8807970779778823, 0.9525741268224334, 0.9820137900379085] , (2, 2)":
        print("Error 1 in sigmoid function \nExpected output: [0.7310585786300049, 0.8807970779778823, 0.9525741268224334, 0.9820137900379085] , (2, 2) \nActual output: " + str(m1))
    # Reset the matrix
    m1.values = [1,2,3,4]

    # Test for the sigmoid_prime function
    sigmoid_prime(m1)
    # sigmoid_prime of [1,2,3,4] = [0, -2, -6, -12]
    if str(m1) != '[0, -2, -6, -12] , (2, 2)':
        print("Error 2 in sigmoid_prime function \nExpected output: [0, -2, -6, -12] , (2, 2) \nActual output: " + str(m1))
    # Reset the matrix
    m1.values = [1,2,3,4]

    # Test for the relu function
    relu(m1)
    # relu of [1,2,3,4] = [1, 2, 3, 4]
    if str(m1) != '[1, 2, 3, 4] , (2, 2)':
        print("Error 3 in relu function \nExpected output: [1, 2, 3, 4] , (2, 2) \nActual output: " + str(m1))
    # Reset the matrix
    m1.values = [1,2,3,4]

    # Test for the relu_prime function
    relu_prime(m1)
    # relu_prime of [1,2,3,4] = [1, 1, 1, 1]
    if str(m1) != '[1, 1, 1, 1] , (2, 2)':
        print("Error 4 in relu_prime function \nExpected output: [1, 1, 1, 1] , (2, 2) \nActual output: " + str(m1))
    # Reset the matrix
    m1.values = [1,2,3,4]
