import json
import csv

with open("dados.txt", 'w', encoding='utf-8') as obj_file:
    obj_file.write("olá mundo")

with open("dados.json", "w", encoding='utf-8') as obj_file:
    json.dump({"message": "Olá mundo"}, obj_file)

with open("dados.csv", "w", encoding='utf-8') as obj_file:
    write = csv.writer(obj_file)
    write.writerow(["olá", "mundo"])
    write.writerow(["jose", "carlos"])
    write.writerow(["testa", "jogos"])

with open("dados.json", "r", encoding='utf-8') as obj_file:
    print(f"dados dentro do 'dados.json': {json.load(obj_file)}")

with open("dados.txt", "r", encoding='utf-8') as obj_file:
    print(f"dados dentro do 'dados.txt': {obj_file.read()}")

with open("dados.csv", encoding='utf-8', newline="") as obj_file:
    read = csv.reader(obj_file)
    for line in read:
        print(read)

