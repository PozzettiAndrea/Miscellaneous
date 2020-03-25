import numpy
import csv
import matplotlib.pyplot as plt


def valfrom(filename):
    csvfile = open(filename, "r")
    reader = csv.reader(csvfile, delimiter=",", quotechar = "|")
    data_list = list(reader)
    
    """creating a list with the sanitised data from the csv reader, with voltage higher than 1
    so that it only selects the data gathered after switchig the supply on"""
    
    DATA = []
    for i in range(len(data_list)-18):
       if data_list[i+18][0]!="nan" and data_list[i+18][0]!="inf" and data_list[i+18][1]!="inf":
           couple= [float(data_list[i+18][0]),float(data_list[i+18][1])]
           if float(couple[0])>1:
               DATA.append(couple)
               
    """turning that list into a numpy array, with one further iteration to select data
     from the top 30% of the voltage range"""
    
    MaxV = max(DATA)[0]
    listy = []

    for i in range(len(DATA)):
        if DATA[i][0]> (MaxV*0.8):
            listy.append(DATA[i])

    TRUDATA = numpy.asarray(listy)
    
    
    for i in range(len(TRUDATA)):
        TRUDATA[i,1] = (1000*TRUDATA[i,0]/TRUDATA[i,1])/(2*3.142*50)
    
   
    print(numpy.std(TRUDATA[:,1]), filename, MaxV)
    return(numpy.average(TRUDATA[:,1]))  
    
    
    
def graphfrom(filename):
    csvfile = open(filename, "r")
    reader = csv.reader(csvfile, delimiter=",", quotechar = "|")
    data_list = list(reader)
    
    """creating a list with the sanitised data from the csv reader, with voltage higher than 1
    so that it only selects the data gathered after switchig the supply on"""
    
    DATA = []
    for i in range(len(data_list)-18):
       if data_list[i+18][0]!="nan" and data_list[i+18][0]!="inf" and data_list[i+18][1]!="inf":
           couple= [float(data_list[i+18][0]),float(data_list[i+18][1])]
           if float(couple[0])>1:
               DATA.append(couple)
               
    """turning that list into a numpy array, with one further iteration to select data
     from the top 30% of the voltage range"""
    
    MaxV = max(DATA)[0]
    listy = []
    listy2 = []
    
    for i in range(len(DATA)):
        if DATA[i][0]> 1 and (1000*DATA[i][0]/DATA[i][1])/(2*3.142*50) < 200:
            listy2.append(DATA[i])
    
    summa = 0
    for i in range(len(listy2)):
        summa += (1000*listy2[i][0]/listy2[i][1])/(2*3.142*50)
    
    for i in range(len(listy2)):
        if DATA[i][0]> (MaxV*0.0) and (1000*DATA[i][0]/DATA[i][1])/(2*3.142*50) < 1.2*summa/(len(listy2)):
            listy.append(listy2[i])
    
    TRUDATA = numpy.asarray(listy)
    
    for i in range(len(TRUDATA)):
        TRUDATA[i,1] = (1000*TRUDATA[i,0]/TRUDATA[i,1])/(2*3.142*50)
    plt.ylim(80,100)
    plt.xlim(0,100)
    return(plt.scatter(TRUDATA[:,0],TRUDATA[:,1]))

def stringen(modes, gaps, leg, number):
    listo = []
    for i in modes:
        for b in gaps:
            for g in leg:
                for l in number:
                    listo.append(i+str(b)+g+l+".csv")
    return listo

Arr = stringen(["T", "TB", "JM"], ["0.5","1.6", "2.4", "3.3", "4.2", "4.8", "6.1"] , ["M"], ["1"])
Arr2 = stringen(["MID"], ["1.6", "2.4", "3.3", "4.2"] , ["L","M","R"], ["1", "2"])
Arr3 = stringen(["DM"], ["1.6", "2.4", "3.3"] , ["L","M","R"], ["1", "2"])

Total = Arr + Arr2 + Arr3

for i in Total:
    graphfrom(i)