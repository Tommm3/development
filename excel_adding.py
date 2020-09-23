import pandas as pd
from openpyxl import load_workbook

df = pd.DataFrame({'masa': ['E','F','G','H']})

writer = pd.ExcelWriter('silka.xlsx', engine='openpyxl')
writer.book = load_workbook('silka.xlsx')
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
reader = pd.read_excel(r'silka.xlsx')

df.to_excel(writer,index=False,startcol=len(reader.columns))
# writer.save()
writer.close()

# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1', index=False)
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
