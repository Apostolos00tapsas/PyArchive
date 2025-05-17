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


values = from_txt_to_matrix('iris.txt',150,5,'int')
            




