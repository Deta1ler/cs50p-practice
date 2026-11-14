



with open("grades.csv") as file:
    lines = file.readlines()
    for line in lines:
        name, house, point = line.rstrip().split(",")
        if int(point) > 80 :
            print (f"{name}: {point}")