import csv
import os

def gravar():   
    with open("desafio_02.csv", "w") as obj_file:
        writer = csv.writer(obj_file)
        writer.writerow(["aluno","nota"])
        writer.writerow(["jose",3.7])
        writer.writerow(["thiago",9.2])
        writer.writerow(["alice",6.9])
        writer.writerow(["aline",10.9])
def ler():
    with open("desafio_02.csv", "r") as obj_file:
        read = csv.reader(obj_file)
        for i, line in enumerate(read):
            if(line and i>0):
                if(float(line[1]) > 7):
                    print(f"Aluno: {line[0]}\nNota: {line[1]}\n")
                
gravar()
ler()