import pandas as pd
from openpyxl import load_workbook

# new data
masa = ['E','F','G','H','G', "H"]
df = pd.DataFrame(masa)
writer = pd.ExcelWriter('silka.xlsx', engine='openpyxl')

# try to open an existing workbook
writer.book = load_workbook('silka.xlsx')

# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)

# read existing file
reader = pd.read_excel(r'silka.xlsx')

# write out the new sheet
df.to_excel(writer,index=False,startcol=len(reader.columns),startrow=18, header=False)
writer.close()
