# this function will get the coordinates of all the tables from a specific excel sheet

# importing required libraries
import openpyxl

def getCoordinatesOfTable(pathOfQRTSheets, qrtNumber):
    exact_path = pathOfQRTSheets+qrtNumber
    wb = openpyxl.load_workbook(exact_path)
    ws = wb[qrtNumber]
