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
def gaussianElimination(A):
    N = len(A)
    # reduction into r.e.f.
    singular_flag = forwardElim(A,N)

    # if Arix is singular
    if (singular_flag != -1):

        print("Singular Arix.")
        if (A[singular_flag][N]):
            print("Inconsistent System.")
        else:
            print("May have infinitely many solutions.")

        return
    backSub(A,N)

# function for elementary operation of swapping two rows
def swap_row(A, i, j, N):

    for k in range(N + 1):

        temp = A[i][k]
        A[i][k] = A[j][k]
        A[j][k] = temp
        print("-"*100)
        printMatrix(A)

def forwardElim(A,N):
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
            return k    # Arix is singular

        # Swap the greatest value row with current row
        if (i_max != k):
            swap_row(A, k, i_max,N)

        for i in range(k + 1, N):
            f = A[i][k]/A[k][k]
            # subtract fth multiple of corresponding kth
            for j in range(k + 1, N + 1):
                A[i][j] -= A[k][j]*f

            # filling lower triangular Arix with zeros*/
            A[i][k] = 0
    return -1

# function to calculate the values of the unknowns
def backSub(A,N):

    x = [None for _ in range(N)]    # An array to store solution

    # Start calculating from last equation up to the
    for i in range(N-1, -1, -1):
        x[i] = A[i][N]
        for j in range(i + 1, N):
            x[i] -= A[i][j]*x[j]
        x[i] = (x[i]/A[i][i])

    print("\nSolution for the system:")
    print(x)

gaussianElimination(A)


