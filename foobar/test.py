def matrix_equals(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix[i])):
	    if matrix1[i][j] != matrix2[i][j]:
	        return False
    return True

def _unit_test__matrix_equal():
    m1 = [range(3), range(3, 0, -1), [5, 2, 3]]
    m2 = [range(3), range(3, 0, -1), [5, 2, 3]]
    m3 = [range(3), range(3, 0, -1), [2, 2, 3]]

    if not matrix_equals(m1, m2):
        print("Matrix equals test failed - m1 and m2 should be equal")

    if not matrix_equals(m2, m1):
        print("Matrix equals test failed - m2 and m2 should be equal")

    if matrix_equals(m1, m2):
        print("Matrix equals test failed - m1 and m3 shoud NOT be equal")



def answer(entrances, exits, rooms):
    pass
