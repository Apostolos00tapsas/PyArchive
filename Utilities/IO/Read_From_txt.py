"""
Script Read_From_txt.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements a function that reads data for a txt file.

Parameters:
    filename  (string): Path of the txt file. 
    rows         (int): The number of rows in the file.
    cols         (int): The number of collumns in the file.
    data_type (string): The data type of data inside txt file.

Returns:
    data: array of the first rows x cols data of type data_type.

Example:
    values = from_txt_to_matrix('iris.txt',rows,cols,'int')
"""

def from_txt_to_matrix(filename,rows,col,data_type='int'):
    k = []
    # Anoikse to arxeio pros epeksergasia
    with open(filename) as file:
        k = [[(digit) for digit in line.split(',')] for line in file]
    # Apoies time mporoun na ginoyn float h in kane thn alagi
    data = [[-1 for x in range(col)] for y in range(rows)]
    for i in range(0,rows):
        for j in range(0,col):
            if k[i][j] == '\n':
                pass
            else:
                try:
                    if data_type=='int':
                        data[i][j] = (int(k[i][j]))
                    else:
                        data[i][j] = (float(k[i][j]))
                except ValueError:
                    data[i][j] = k[i][j]
        
    return data

rows = 150
cols = 5

values = from_txt_to_matrix('iris.txt',rows,cols,'int')
            




