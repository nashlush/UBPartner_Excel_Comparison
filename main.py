from convertToMatrix import convertToStringMatrix
from compareTableArray import compareArrayValues
from Append_QRT import appendQRTSheets

appendQRTSheets('.\\XBRL QRT','.\\Appended XBRL QRT')
appendQRTSheets(".\\Solution QRT",".\\Appended Solution QRT")

pathOfOldQRTSheets = '.\\old\\'
pathOfNewQRTSheets = '.\\new\\'
qrtNumber = 'S.02.02.xlsx'
arr1 = ['C6','J25']
arr2 = ['C6','J25']

table1 = convertToStringMatrix(arr1,qrtNumber, pathOfOldQRTSheets)
table2 = convertToStringMatrix(arr2, qrtNumber, pathOfNewQRTSheets)

diff = compareArrayValues(table1,table2)
if len(diff) == 0:
    print("The QRTs match perfectly")
else:
    print(diff)
