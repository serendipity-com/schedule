# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 16:22:32 2019

@author: Cristian David Araujo
"""


def print_Intro():
    #Esta funcion imprime el intro
    introFile = open("intro2.txt","r")
    
    for x in introFile:
        print(x,end="")
    print("")
    
    introFile.close()
    
def create_data():
    #crea datos de maestros y alumnoos con diccionarios
    teacher = dict()
    group = dict()
    
    
    data_teacher = open("Data/teachers.txt","r")  
    user = str
    for line_1 in data_teacher:
        if "#" in line_1[0]:
            user = str(line_1[1:line_1.find(";")])
            teacher[user] = [[],[],{}]
            teacher[user][0] = (line_1[line_1.find(";")+1:line_1.find("<")]).split(",")
            teacher[user][1] = (line_1[line_1.find("<")+1:line_1.find(">")]).split(",")
        
        elif "[" in line_1[0]:
            teacher[user][2]["lunes"] = (line_1[1:-1].split(":"))[0]
            teacher[user][2]["martes"] = (line_1[1:-1].split(":"))[1]
            teacher[user][2]["miercoles"] = (line_1[1:-1].split(":"))[2]
            teacher[user][2]["jueves"] = (line_1[1:-1].split(":"))[3]
            teacher[user][2]["viernes"] = (line_1[1:-1].split(":"))[4]
            
            for day in teacher[user][2]:
                teacher[user][2][day] = teacher[user][2][day].split(",")
                
                for hour in range(len(teacher[user][2][day])):
                    teacher[user][2][day][hour] = teacher[user][2][day][hour].split("-")
    data_teacher.close()


    data_group = open("Data/groups.txt","r")
    user = str
    for line_2 in data_group:
        if "#" in line_2[0]:
            user = str(line_2[1:line_2.find(";")])
            group[user] = {}
            group[user]["lunes"] = (line_2[line_2.find("<")+1:line_2.find(">")].split("/"))[0]
            group[user]["martes"] = (line_2[line_2.find("<")+1:line_2.find(">")].split("/"))[1]
            group[user]["miercoles"] = (line_2[line_2.find("<")+1:line_2.find(">")].split("/"))[2]
            group[user]["jueves"] = (line_2[line_2.find("<")+1:line_2.find(">")].split("/"))[3]
            group[user]["viernes"] = (line_2[line_2.find("<")+1:line_2.find(">")].split("/"))[4]
            
        for day2 in group[user]:
            group[user][day2] = group[user][day2].split(",")
            
            for hour2 in range(len(group[user][day2])):
                group[user][day2][hour2] = group[user][day2][hour2].split("-") 
    data_group.close()
    
    return group , teacher

def see_information_teachers(teacher):
    #Imprime informacion de maestros
    user = "CRISTIAN"#str(input("ingrese nombre de maestro: ")).upper()
    if user in teacher:
        groups = teacher[user][0]
        course = teacher[user][1]
        days = teacher[user][2]
        espace = int(9)
        
        for count in range(len(course)):
            if espace < len(course[count]):
                espace = len(course[count])
                if (espace % 2) != 0:
                    espace += 1
               
        print("___"*5+(espace*"_"*5)+"___"*5)
        print(("|  "+(espace*" ")+"  |"+("   "+(espace*" ")+"  |")*4))
        print("|  "+((espace//2-3)*" ")+"LUNES"+((espace//2-2)*" ")+"  |"+"   "+((espace//2-3)*" ")+"MARTES"+((espace//2-3)*" ")+"  |"+"   "+((espace//2-5)*" ")+"MIERCOLES"+((espace//2-4)*" ")+"  |"+"   "+((espace//2-3)*" ")+"JUEVES"+((espace//2-3)*" ")+"  |"+"   "+((espace//2-4)*" ")+"VIERNES"+((espace//2-3)*" ")+"  |")
        print(("|__"+(espace*"_")+"__|"+("___"+(espace*"_")+"__|")*4))
        
        for hour in range(len(days["lunes"])):
            for day in days:
                if (len(days[day][hour][0]) % 2) == 0:
                    print("|  "+((espace//2-(len(days[day][hour][0])//2)))*" "+days[day][hour][0]+((espace//2-(len(days[day][hour][0])//2))*" ")+"  ",end="")
                elif (len(days[day][hour][0])) == 0:
                    print("|  "+(espace+3)*" "+"  ",end="")
                if (len(days[day][hour][0]) % 2) != 0:
                    print("|  "+((espace//2-(len(days[day][hour][0])//2)+1))*" "+days[day][hour][0]+((espace//2-(len(days[day][hour][0])//2))*" ")+"  ",end="")
            print("\n"+len(days[day][hour][0])

    else:
        print("El maestro "+user+" no esta registrado")
group , teacher = create_data()
see_information_teachers(teacher)







