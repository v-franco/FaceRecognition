results = [
    [ # Original 128dim
        [ # L2
        'photos/TC3002B_Faces/A01365726/0.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01365726/1.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01365726/2.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01365726/3.jpg',
        '0.33',
        ],
        [ # Cosenos
        'photos/TC3002B_Faces/A01365726/0.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01365726/1.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01365726/2.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01365726/3.jpg',
        '0.33',
        ],
        [ # Manhattan
        'photos/TC3002B_Faces/A01365726/0.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01365726/1.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01365726/2.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01365726/3.jpg',
        '0.33',
        ] 
    ],
    [ # PCA 2dim
        [ # L2
        'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01366686/Selfie_2.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01366686/selfie_3.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01366686/selfie_4.jpg',
        '0.33',
        ],
        [ # Cosenos
        'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01366686/Selfie_2.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01366686/selfie_3.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01366686/selfie_4.jpg',
        '0.33',
        ],
        [ # Manhattan
        'photos/TC3002B_Faces/A01366686/selfie_1.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01366686/Selfie_2.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01366686/selfie_3.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01366686/selfie_4.jpg',
        '0.33',
        ]
        
    ],
    [ # SVD 2dim
        [ # L2
        'photos/TC3002B_Faces/A01369422/jordi_1.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01369422/jordi_2.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01369422/Jordi_3.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01369422/Jordi_4.jpg',
        '0.33',
        ],
        [ # Cosenos
        'photos/TC3002B_Faces/A01369422/jordi_1.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01369422/jordi_2.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01369422/Jordi_3.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01369422/Jordi_4.jpg',
        '0.33',
        ],
        [ # Manhattan
        'photos/TC3002B_Faces/A01369422/jordi_1.jpg',
        '0.00',
        'photos/TC3002B_Faces/A01369422/jordi_2.jpg',
        '0.11',
        'photos/TC3002B_Faces/A01369422/Jordi_3.jpg',
        '0.22',
        'photos/TC3002B_Faces/A01369422/Jordi_4.jpg',
        '0.33',
        ]
    ]
]

# change path names
for matrix in results:
    for i in range(0, len(matrix)):
        model = matrix[i]
        for j in range(0, len(model), 2):
            path = model[j]
            new_path = "/".join(path.split("/")[1:])
            new_path = "static/img/" + new_path 
            model[j] = new_path
            print(model[j])
            
