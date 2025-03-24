print("Question 5 b).\n\n")

A = [[1, 1, 0, 1, 2], [2, 1, -1, 1, 1], [-1, 2, 3, -1, 4], [3, -1, -1, 2, -3]]

def printMatrix(A):
    if not A:
        print("[]")
        return

    # Find the maximum width of each column
    col_widths = [0] * len(A[0])
    for row in A:
        for i, element in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(element)))

    # Print the matrix
    for row in A:
        formatted_row = " ".join(str(element).rjust(col_widths[i]) for i, element in enumerate(row))
        print(formatted_row)

printMatrix(A)

# function to get Arix content
def gaussianJordanElimination(A):
    N = len(A)
    # reduction into r.r.e.f.
    singular_flag = forwardElim(A, N, True)  # Pass True for Gaussian-Jordan

    # if Arix is singular
    if (singular_flag != -1):
        print("Singular Arix.")
        if (A[singular_flag][N]):
            print("Inconsistent System.")
        else:
            print("May have infinitely many solutions.")
        return
    
    #back substitution is not needed in gaussian jordan, the matrix is already in the solution form.
    print("\nSolution for the system:")
    solution = [A[i][N] for i in range(N)]
    print(solution)

def swap_row(A, i, j, N):
    for k in range(N + 1):
        temp = A[i][k]
        A[i][k] = A[j][k]
        A[j][k] = temp
    print("-" * 100)
    printMatrix(A)

def forwardElim(A, N, gaussian_jordan=False):
    for k in range(N):
        # Initialize maximum value and index for pivot
        i_max = k
        v_max = A[i_max][k]

        # find greater amplitude for pivot if any
        for i in range(k + 1, N):
            if (abs(A[i][k]) > v_max):
                v_max = A[i][k]
                i_max = i

        if not A[k][i_max]:
            return k  # Arix is singular

        # Swap the greatest value row with current row
        if (i_max != k):
            swap_row(A, k, i_max, N)

        # Make the pivot 1
        pivot = A[k][k]
        for j in range(k, N + 1):
            A[k][j] /= pivot
        print("-" * 100)
        printMatrix(A)

        for i in range(N):
            if i != k:  # Modified to work for all rows, including those above the pivot
                f = A[i][k]
                for j in range(k, N + 1):
                    A[i][j] -= A[k][j] * f
        print("-" * 100)
        printMatrix(A)

    return -1

gaussianJordanElimination(A)