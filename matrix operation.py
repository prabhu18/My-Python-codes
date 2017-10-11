matrix= [[1, 0, 3, 2],
         [0, 5, 0, 1],
        [0, 5, 0, 1],
        [0, 5, 0, 1],
        [0, 5, 0, 1],
         [0, 0, 3, 5]]

rowsToDelete= [1,3,4]
columnsToDelete= [0, 2,3]


def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):

    count=0
    for i in rowsToDelete:
        if count==0:
            del matrix[i]
            count=count+1
        else:
            del matrix[i-count]

    for  row in matrix:
        count = 0
        for j in range(0,len(row)):
            if j in columnsToDelete:
                if count==0:
                    del row[j]
                    count=count+1
                else:
                    del row[j-count]
                    count=count+1


    print matrix


constructSubmatrix(matrix, rowsToDelete, columnsToDelete)