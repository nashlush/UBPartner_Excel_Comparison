# import statements
import openpyxl

# function to convert the extracted table into a 2d array of string 
def convertToStringMatrix(coordinate, qrtNumber, pathOfQRTSheets):

    # extracting the row num and col num from the array of Coordinates
    min_row = int(coordinate[0][1:])
    min_col = (ord(coordinate[0][0])%ord('A')+1)
    max_row = int(coordinate[1][1:])
    max_col = (ord(coordinate[1][0])%ord('A')+1)

    exact_path = pathOfQRTSheets+qrtNumber
    wb = openpyxl.load_workbook(exact_path)
    # print(qrtNumber[10:20])
    ws = wb[qrtNumber[10:20]]
    
    rows = ws.iter_rows(min_row=min_row, max_row=max_row, min_col=min_col,max_col=max_col)
    # print(rows)

    array1 = []

    # logic for pushing the cells into the 2d array defined
    for row in rows:
        tempArr = []
        for col in row:
            tempArr.append(col.value)
        array1.append(tempArr)

    return array1
