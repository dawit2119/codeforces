test_cases = int(input())
def rotate_2x2_matrix(matrix):
    """
    Rotates a 2x2 matrix by 90 degrees clockwise.
    """
    matrix[0][0], matrix[1][0], matrix[1][1], matrix[0][1] = \
        matrix[1][0], matrix[1][1], matrix[0][1], matrix[0][0]
    return matrix

def check(matrix):
    for i in range(2):
        if matrix[i][0] > matrix[i][1]:
            return "NO"
    for j in range(2):
        if matrix[0][j] > matrix[1][j]:
            return "NO"
    return "YES"
for i in range(test_cases):
    row1 = list(map(int,input().split()))
    row2 = list(map(int,input().split()))
    original_matrix = [[0]*2 for i in range(2)]
    original_matrix[0][0] = row1[0]
    original_matrix[0][1] = row1[1]
    original_matrix[1][0] = row2[0]
    original_matrix[1][1] = row2[1]
    matrix = []    
    matrix.append(row1)
    matrix.append(row2)
    output1 = check(matrix)
    if output1 == "YES":
        print("YES")
    else:
        while True:
            matrix = rotate_2x2_matrix(matrix)
            output2 = check(matrix)
            if output2 == "YES":
                print("YES")
                break
            elif matrix == original_matrix :
                print("NO")
                break
    
