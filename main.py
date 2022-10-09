from convertToMatrix import convertToStringMatrix

pathOfQRTSheets = '.\\'
qrtNumber = 'Validated-S.38.01.10.xlsx'
arr = ['A5','C7']

table1 = convertToStringMatrix(arr,qrtNumber, pathOfQRTSheets)
for row in table1:
    print(row)