# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#

# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []
for row_number in range(rows):
    row = list(map(int, input(f"Enter row {row_number + 1}: ").split()))
    matrix.append(row)

def display_matrix(matrix):
    for row in matrix:
        for value in row:
          print(value, end=" ")
        print()

def transpose_matrix(matrix):
    transpose = []
  
    for column in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(matrix[row][column])
        transpose.append(new_row)

    return transpose


print("Original Matrix:")
display_matrix(matrix)

transpose = transpose_matrix(matrix)

print("Transpose Matrix:")
display_matrix(transpose)


def add_matrices(matrix1, matrix2):
  result = []

  for row in range(len(matrix1)):
    new_row = []

    for column in range(len(matrix1[0])):
        new_row.append(matrix1[row][column] + matrix2[row][column])

    result.append(new_row)


  return result


def multiply_matrices(matrix1,matrix2):
    result = []

    for row in range(len(matrix1)):
        new_row = []
    
        for column in range(len(matrix2[0])):
            total = 0 

            for k in range(len(matrix1[0])):
                total += matrix1[row][k] * matrix2[k][column]

          new_row.append(total)
      result.append(new_row)
    return result 