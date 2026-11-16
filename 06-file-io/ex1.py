with open("grades.csv") as file:
    for line in file:
        name, _, point = line.rstrip().split(",")
        if int(point) > 80 :
            print (f"{name}: {point}")