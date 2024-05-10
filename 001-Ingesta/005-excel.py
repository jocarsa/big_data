#pip install pandas openpyxl
import pandas as pd
file_path = "empresa.xlsx"
data = pd.read_excel(file_path, sheet_name="clientes")
print(data)
