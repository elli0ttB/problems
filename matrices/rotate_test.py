from rotate_matrix_90_degrees import rotate_90

def test_4_rotations():
    """4 rotations should is idempotent operation"""
    A = [[0,1,2], [3,4,5], [6,7,8]]
    for i in range(4):
        rotate_90(A)
    assert A == [[0,1,2], [3,4,5], [6,7,8]]

def test_1_rotation():
    A = [[0,1,2],
         [3,4,5],
         [6,7,8]]
    rotate_90(A)
    assert A == [[6,3,0],
                 [7,4,1],
                 [8,5,2]]

    A =[ [ 0,1,2,3 ],
         [ 4,5,6,7 ],
         [ 8,9,10,11 ],
         [ 12,13,14,15 ] ]
    rotate_90(A)
    assert A ==[[ 12,8,4,0 ],
                [ 13,9,5,1 ],
                [ 14,10,6,2 ],
                [ 15,11,7,3 ]]
