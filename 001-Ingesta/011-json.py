import json
file_path = "clientes.json"
with open(file_path, "r") as file:
    data = json.load(file)
print(data)
