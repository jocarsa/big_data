#pip install pandas odfpy
import pandas as pd
file_path = "empresa.ods"
data = pd.read_excel(file_path, engine="odf", sheet_name="clientes")
print(data)
