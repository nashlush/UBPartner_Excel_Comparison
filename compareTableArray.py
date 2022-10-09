# This function will compare both tables and return an array of differences.
def compareArrayValues(a, b):
    diff = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                diff.append((i,j,a[i][j],b[i][j]))
    return diff