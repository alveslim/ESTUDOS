import csv

name = input("type name of the language want you have study:\n")
category = input("type category of the language:\n")

with open("4-Manipulando_arquivos/4-courses.csv", "a", encoding="utf-8", newline='') as file:
    writer =  csv.writer(file, lineterminator='\n')
    writer.writerow([name, category])
    
