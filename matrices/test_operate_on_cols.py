from operate_on_cols import transform_matrix

def setup_function(fn):
    global mat
    mat = [[0,  1,  2,  3,  4,  5],
           [7,  8,  9,  10, 11, 12],
           [13, 14, 15, 16, 17, 18],
           [19, 20, 21, 22, 23, 24]]

    global mary
    mary = [[0, 1, 0],
            [3, 4, 5],
            [6, 7, 0]]

def test():
    transform_matrix(mat)
    transform_matrix(mary)

    assert mat == [[0,  0,  0,  0,  0,  0],
                   [0,  8,  9,  10, 11, 12],
                   [0, 14, 15, 16, 17, 18],
                   [0, 20, 21, 22, 23, 24]]

    assert mary == [[0, 0, 0],
                    [0, 4, 0],
                    [0, 0, 0]]


