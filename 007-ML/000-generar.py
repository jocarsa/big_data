import pandas as pd
import random
import faker

fake = faker.Faker()

data = []
for _ in range(100000):
    name = fake.first_name()
    surname = fake.last_name()
    balance = round(random.uniform(1000, 1000000), 2)  
    data.append([name, surname, balance])

df = pd.DataFrame(data, columns=["Nombre", "Apellidos", "Saldo"])

file_path = "usuarios_ficticios.xlsx"
df.to_excel(file_path, index=False)


