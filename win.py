import win32com.client
ex = win32com.client.Dispatch("Excel.Application")
ex.Visible =True
work = ex.Workbooks.Open(r'C:\Users\Admin\Documents\rr')
sheet = work.Sheets(1)
cel=sheet.cells(1,1).values="hello","World"
print(f"value in A1 sheet:{cel}")

