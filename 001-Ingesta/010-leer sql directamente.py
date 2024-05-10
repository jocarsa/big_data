def read_sql_dump(sql_dump_file,tabla):
    table_name = tabla
    table_data = []
    with open(sql_dump_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    in_table_data = False
    for line in lines:
        if line.startswith("INSERT INTO `{}`".format(table_name)):
            in_table_data = True
            continue
        if in_table_data:
            values = line.strip().split("VALUES ")[-1]
            values_list = values.strip("();\n").split("),(")
            for row_values in values_list:
                table_data.append(row_values.strip("()").split(","))
    return table_data

sql_dump_file = "bigdata.sql"
clientes_data = read_sql_dump(sql_dump_file,"clientes")

# Print the data
for row in clientes_data:
    print(row)
