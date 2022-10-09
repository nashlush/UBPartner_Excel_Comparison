from convertToMatrix import convertToStringMatrix
from compareTableArray import compareArrayValues

pathOfOldQRTSheets = '.\\old\\'
pathOfNewQRTSheets = '.\\new\\'
qrtNumber = 'Validated-S.01.01.14.xlsx'
arr1 = ['A5','D10']
arr2 = ['A5','D10']

table1 = convertToStringMatrix(arr1,qrtNumber, pathOfOldQRTSheets)
table2 = convertToStringMatrix(arr2, qrtNumber, pathOfNewQRTSheets)

diff = compareArrayValues(table1,table2)
print(diff)
