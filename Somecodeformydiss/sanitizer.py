import csv

import os

LIST = []
for filename in os.listdir("."):
    if filename.endswith(".CSV"):
        LIST.append(filename)

for filename in LIST:
    print(filename)
    csvfile = open(filename, "r")
    reader = csv.reader(csvfile, delimiter=",", quotechar = "|")
    data_list = list(reader)
    

    DATA = []
    for i in range(len(data_list)):
       if data_list[i][0]!="nan" and data_list[i][0]!=0 and data_list[i][0]!="inf":
           try:
               couple= [float(data_list[i][0]), float(data_list[i][1])]
               if float(couple[0])>1:
                   DATA.append(couple)
           except:
               print("exception")
    
    print(filename)       
    MaxV = max(DATA)[0]
    listy = []
    
    passed = 0
    for i in range(len(DATA)):
         if passed == 0:
             listy.append(DATA[i])
             if DATA[i][0] == MaxV:
                passed = 1
                listy.append(DATA[i])
            
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(listy)):
            writer.writerow(listy[i])