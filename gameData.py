materialValueDictionary ={
    'K': 1000,
    'Q': 90,
    'R': 50,
    'B': 30,
    'N': 30,
    'p': 10
    }

absoluteEarlyPositionalDictionary ={
    'K':[
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [-10,-10,-10,-10,-10,-10,-10,-10],
        [  1,  2, -3, -3, -3, -5,  2,  1],
        [  2,  5,  4,  0,  0,  0,  5,  2]
        ],

    'Q':[
        [ 1, 3, 3, 3, 3, 3, 3, 1],
        [ 1, 6, 4, 4, 4, 6, 6, 1],
        [ 1, 3, 4, 4, 4, 4, 3, 1],
        [ 2, 3, 4, 4, 4, 4, 3, 2],
        [ 0, 0, 4, 5, 5, 4, 3, 3],
        [ 0, 5, 5, 4, 4, 5, 5, 3],
        [ 1, 3, 5, 3, 3, 0, 0, 1],
        [ 0, 0, 0, 0, 0, 0, 0, 0]
        ],

    'R':[
        [ 0,  0,  0,  4,  4,  0,  0,  0],
        [ 0,  0,  0,  5,  5,  0,  0,  0],
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 0,  0,  0,  1,  1,  0,  0,  0],
        [ 0,  0,  0,  1,  1,  0,  0,  0],
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 0,  0,  0,  3,  3,  0,  0,  0],
        [ 0,  0,  0,  4,  4,  0,  0,  0]
        ],

    'B':[
        [ -1, 0,  0,   0,  0,  0,  0, -1],
        [ 0,  2,  0,   0,  0,  0,  2,  0],
        [ 0,  0,  1,   0,  0,  1,  0,  0],
        [ 0,  2,  0,   0,  0,  2,  0,  0],
        [ 0,  0,  4,   1,  1,  4,  0,  0],
        [ 2,  3,  2,   2,  2,  2,  3,  2],
        [ 2,  3,  0,   2,  2,  0,  3,  2],
        [ 1,  0,  0 ,  0,  0,  0,  0,  1]
        ],

    'N':[
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 2, 2, 0, 0, 0],
        [ 2, 2, 4, 2, 2, 4, 2, 2],
        [ 0, 2, 3, 2, 2, 3, 0, 0],
        [ 0, 0, 2, 2, 2, 2, 0, 0],
        [ 0, 1, 2, 2, 2, 2, 0, 0],
        [ 0, 1, 1, 1, 1, 1, 1, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0]
        ],

    'p':[
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [12, 11, 10, 10, 10, 10, 11, 12],
        [ 3,  3,  3,  4,  4,  3,  3,  3],
        [ 0,  0,  2,  3,  3,  3,  0,  0],
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 0,  0,  0, -1, -1,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
        ]    
}    

absoluteLatePositionalDictionary ={
    'K':[
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  1,  1,  1,  1,  0,  0],
        [  0,  0,  1,  1,  1,  1,  0,  0],
        [  0,  0,  1,  1,  1,  1,  0,  0],
        [  0,  0,  1,  1,  1,  1,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0]
        ],

    'Q':[
        [ 1, 3, 3, 3, 3, 3, 3, 1],
        [ 1, 6, 4, 4, 4, 6, 6, 1],
        [ 1, 3, 4, 4, 4, 4, 3, 1],
        [ 2, 3, 4, 4, 4, 4, 3, 2],
        [ 0, 0, 4, 5, 5, 4, 3, 3],
        [ 0, 5, 5, 4, 4, 5, 5, 3],
        [ 1, 3, 5, 3, 3, 0, 0, 1],
        [ 0, 0, 0, 0, 0, 0, 0, 0]
        ],

    'R':[
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 3,  3,  3,  3,  3,  3,  3,  3],
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 0,  0,  0,  1,  1,  0,  0,  0],
        [ 0,  0,  0,  1,  1,  0,  0,  0],
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 0,  0,  0,  3,  3,  0,  0,  0],
        [ 0,  0,  0,  4,  4,  0,  0,  0]
        ],

    'B':[
        [ -1, 0,  0,   0,  0,  0,  0, -1],
        [ 0,  2,  0,   0,  0,  0,  2,  0],
        [ 0,  0,  1,   0,  0,  1,  0,  0],
        [ 0,  2,  0,   0,  0,  2,  0,  0],
        [ 0,  0,  4,   1,  1,  4,  0,  0],
        [ 2,  3,  2,   2,  2,  2,  3,  2],
        [ 2,  3,  0,   2,  2,  0,  3,  2],
        [ 1,  0,  0 ,  0,  0,  0,  0,  1]
        ],

    'N':[
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 2, 2, 0, 0, 0],
        [ 2, 2, 4, 2, 2, 4, 2, 2],
        [ 0, 2, 3, 2, 2, 3, 0, 0],
        [ 0, 0, 2, 2, 2, 2, 0, 0],
        [ 0, 1, 2, 2, 2, 2, 0, 0],
        [ 0, 1, 1, 1, 1, 1, 1, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0]
        ],

    'p':[
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [12, 11, 10, 10, 10, 10, 11, 12],
        [ 3,  3,  3,  4,  4,  3,  3,  3],
        [ 0,  0,  2,  3,  3,  3,  0,  0],
        [ 0,  0,  0,  2,  2,  0,  0,  0],
        [ 2,  0,  0,  2,  2,  0,  0,  2],
        [ -1, 0,  0, -1, -1,  0,  0, -1],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
        ]    
}    