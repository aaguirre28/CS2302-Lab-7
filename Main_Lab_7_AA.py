"""
Alexis Aguirre
CS2302: Lab 7, Option A 
Due on: 12/13/18

"""
import unittest

def PrintMatrix(matrix):
    for i in range(len(matrix)):    # Print method to to visualize matrix and verify algorithm
        print(matrix[i])

def InitializeMatrix(length_1, length_2):   # Initializes matrix with all 0s
    matrix = []
    for i in range(length_1):       # Appends new list at every element in initial list for 2 dimensional array
        matrix.append([])
    for j in range(length_1):       # Fills empty matrix with 0s
        for k in range(length_2):
            matrix[j].append(0)
    return matrix

def EditDistance(string_1, string_2):
    adjacency_matrix = InitializeMatrix(len(string_2) + 1, len(string_1) + 1)   # First string on top of matrix is controlled by i/vertical iterator
    for i in range(len(adjacency_matrix)):      # iterates through all of matrix
        for j in range(len(adjacency_matrix[i])):
            if i is 0 and j is 0:   # skips comparison of blank spaces
                continue
            elif i is 0:    # If vertical string is empty, add 1 for every character you add to top string
                adjacency_matrix[i][j] = adjacency_matrix[i][j-1] + 1   # + 1 since blank space is not in actual string
            elif j is 0:    # Opposit of previous check
                adjacency_matrix[i][j] = adjacency_matrix[i-1][j] + 1
            elif string_1[j-1] == string_2[i-1]:        # If current chars are the same, copy min from adjacent left, left upper, and upper values
                adjacency_matrix[i][j] = min(adjacency_matrix[i-1][j-1], adjacency_matrix[i-1][j], adjacency_matrix[i][j-1])
            else:   # If current chars are not the same, copy min + 1 from adjacent left, left upper, and upper values
                adjacency_matrix[i][j] = min(adjacency_matrix[i-1][j-1], adjacency_matrix[i-1][j], adjacency_matrix[i][j-1]) + 1
                
    return adjacency_matrix

class TestMatrix(unittest.TestCase):    # Test cases
    def test_ed_matrix(self):
        self.assertEqual(EditDistance("abcde", "abzde"), [[ 0, 1, 2, 3, 4, 5],
                                                          [ 1, 0, 1, 2, 3, 4],
                                                          [ 2, 1, 0, 1, 2, 3],
                                                          [ 3, 2, 1, 1, 2, 3],
                                                          [ 4, 3, 2, 2, 1, 2],
                                                          [ 5, 4, 3, 3, 2, 1]])

        self.assertEqual(EditDistance("flaw", "lawn"), [[ 0, 1, 2, 3, 4],
                                                        [ 1, 1, 1, 2, 3],
                                                        [ 2, 2, 2, 1, 2],
                                                        [ 3, 3, 3, 2, 1],
                                                        [ 4, 4, 4, 3, 2]])

        self.assertEqual(EditDistance("miners", "money"), [[ 0, 1, 2, 3, 4, 5, 6],
                                                           [ 1, 0, 1, 2, 3, 4, 5],
                                                           [ 2, 1, 1, 2, 3, 4, 5],
                                                           [ 3, 2, 2, 1, 2, 3, 4],
                                                           [ 4, 3, 3, 2, 1, 2, 3],
                                                           [ 5, 4, 4, 3, 2, 2, 3]])

def main():
    unittest.main()
    
main()