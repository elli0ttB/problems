def transform_matrix(A):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set 0.
    """
    rows = len(A)
    cols = len(A[0])

    # an important pattern that I have not implemented here is the count-set;
    # have an array with index 1 if the value is postive or 0 if negative

    zero_rows = set()
    zero_cols = set()

    for i in range(rows):
        for j in range(cols):
            if A[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    for i in range(rows):
        if i in zero_rows:
            A[i] = [0] * cols
        else:
            for j in zero_cols:
                A[i][j] = 0
