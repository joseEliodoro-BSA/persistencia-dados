nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

file_name = "input_data.txt"

with open(file_name, 'a') as obj_file:
    obj_file.write(f"\nNome: {nome}\n")
    obj_file.write(f"idade: {idade}")

with open(file_name, "r") as obj_file:
    for line in obj_file.readlines():
        print(line)