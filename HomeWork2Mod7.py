file_name = "text.txt"
with open(file_name, mode="r", encoding="utf8") as file:
for line in file:
print(line, end="")

# оператор with автоматически закрывает файл. close не требуется
