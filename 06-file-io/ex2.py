import csv


with open("grades1.csv", "w") as file:
    file.write(f"name,house,score\nHermione,Gryffindor,98\nHarry,Gryffindor,85\nDraco,Slytherin,92\nNeville,Gryffindor,74\n")

students = []
name = input("Name: ")
house = input("House: ")
score = input("Score: ")

with open("grades1.csv", "a", newline="") as file:
    writer = csv.writer(file) #можна прочитать как возьми функцию с модуля csv writer, 
                              #чтобы она сделала из сырого файлового обьекта, потока 
                              # более умную матрешку у которой уже будет метод для записи строк, списков
    writer.writerow([name, house, score])

with open("grades1.csv") as file:
    reader = csv.DictReader(file) #Возьми функцию DictReader из модуля csv, 
                                  #чтобы она сделала из сырого файлового объекта-потока 
                                  #более умную матрёшку, у которой уже будет встроена функция 
                                  # итерирования этого объекта и автоматическая выдача словарей, 
                                  # сформированных относительно первой строки (имён колонок)
    for row in reader: 
        students.append({"name": row["name"], "house": row["house"], "score": int(row["score"])})


for student in sorted(students, key=lambda s: s["score"], reverse=True):
    print(f"{student['name']} ({student['house']}): {student['score']}")