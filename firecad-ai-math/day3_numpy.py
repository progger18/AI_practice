import numpy as np

x = np.array([1, 2, 3])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

RGB_image = np.array(
    [
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],

        [
            [0, 0, 0],
            [0, 255, 0],
            [0, 0, 0]
        ]
    ]
)

batch_RGB_image = np.array([
    
        [
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        ,

            [
                [0, 255, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        ]
    ,


        [
            [
                [0, 160, 0],
                [0, 0, 0],
                [0, 180, 0]
            ],

            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        ]

])

# print(x.ndim)
# print(matrix.ndim)
# print(RGB_image.ndim)
# print(batch_RGB_image.ndim)

# print(x.dtype)

x = np.array([1.0, 2.0, 3.0])
# print(x.dtype)

# print(matrix[:, 1])

line = np.array([1,2,3,4,5,6])
# print(line.shape)
# print(line.reshape(2,3))

image = np.array([
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    [
        1, 2, 3, 4, 5, 6, 7, 8
    ]
])

# print(image)
# print(image.reshape(64))

# print(image)
# print(image.T)

# length, thickness, angle
walls = np.array([
    [10.0, 0.2, 0.0],
    [15.0, 0.3, 90.0],
    [7.5, 0.2, 90.0],
    [20.0, 0.4, 0.0]
])

# print(walls.shape)
# print(walls.shape[0])
# print(walls[:, 0])
# print(walls[:,1])
# print(walls[:, 0].max())
# print(walls[:, 0].mean())

print(walls.ndim)