# concatenates all excel files in one worksheet
import os
import openpyxl
import pandas as pd
import glob

def appendQRTSheets(QRT_dir,Final_dir):
    os.chdir(QRT_dir)
    location = '.\\*.xlsx'
    excel_files = glob.glob(location)
    print(excel_files)
    for excel_file in excel_files:
        temp = str(excel_file)
        start = end = filename = ""
        if "XBRL QRT" in QRT_dir:
            start = temp.find("xbrl_")
            end = temp.find(".xlsx")
            filename = temp[start+5:end]
            print(filename)
        else:
            start = temp.find("-")
            end = temp.rindex(".")
            filename = temp[start+1:end]
            print(filename)

        final_df = pd.DataFrame()
        temp_df = pd.DataFrame()

        wb = openpyxl.load_workbook(temp)
        for ws in wb.worksheets:
            print(ws.title)
            if(filename in ws.title):
                sheet = ws.title
                temp_file = pd.ExcelFile(temp)
                temp_df = pd.read_excel(temp_file,sheet_name=sheet)
                final_df = pd.concat([final_df,temp_df], ignore_index=True)
        os.chdir('..\\'+Final_dir)
        print("Current directory : ",os.getcwd())
        final_df.to_excel(filename+'.xlsx', index=False, sheet_name=filename)
        os.chdir('..\\'+QRT_dir)

        

#appendQRTSheets('.\\XBRL QRT','.\\Appended XBRL QRT')
#appendQRTSheets(".\\Solution QRT",".\\Appended Solution QRT")

