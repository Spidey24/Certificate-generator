import csv

#Create empty list to store data 
name = []
sem = []
grade = []

#Open the csv file and use csv reader 
with open('test.csv','r') as file:
    name_pep = csv.reader(file)

#Adding values to our empty lists
    for row in name_pep:
        name.append(row[0])
        sem.append(row[1])
        grade.append(row[2])

#Check values if they are correct or not by printing them 
#print(name)
#print(sem)
#print(grade)       

#Writing a separate file for the necessary data items
achievers_name = name[1:]
name_txt = open('D:/Python_learning/3_Projects/Certificate-generator/ach_name.txt','w')
content = '\n'.join(achievers_name)
name_txt.writelines(content)
name_txt.close()
