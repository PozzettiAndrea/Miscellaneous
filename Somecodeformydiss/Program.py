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
    for i in range(len(DATA)):
        if DATA[i][0]> (MaxV*0.2):
            listy.append(DATA[i])
    
    TRUDATA = numpy.asarray(listy)
    
    for i in range(len(TRUDATA)):
        TRUDATA[i,1] = (1000*TRUDATA[i,0]/TRUDATA[i,1])/(2*3.142*50)
    
    return(plt.scatter(TRUDATA[:,0],TRUDATA[:,1]))

graphfrom("T1.6L1.csv")
graphfrom("T1.6M1.csv")
graphfrom("T1.6R1.csv")

"""
GAPS = numpy.array([0.5, 1.64, 2.37, 3.19, 4.28, 4.86, 6.08])
GAPS2 = numpy.array([0.5, 1.64, 2.37, 3.19, 4.28])

VALSLTB = numpy.array([valfrom("TB0.5L1.csv"),valfrom("TB1.6L1.csv"),valfrom("TB2.4L1.csv"),valfrom("TB3.3L1.csv"),valfrom("TB4.2L1.csv"),valfrom("TB4.8L1.csv"),valfrom("TB6.1L1.csv")])
VALSMTB = numpy.array([valfrom("TB0.5M1.csv"),valfrom("TB1.6M1.csv"),valfrom("TB2.4M1.csv"),valfrom("TB3.3M1.csv"),valfrom("TB4.2M1.csv"),valfrom("TB4.8M1.csv"),valfrom("TB6.1M1.csv")])
VALSRTB = numpy.array([valfrom("TB0.5R1.csv"),valfrom("TB1.6R1.csv"),valfrom("TB2.4R1.csv"),valfrom("TB3.3R1.csv"),valfrom("TB4.2R1.csv"),valfrom("TB4.8R1.csv"),valfrom("TB6.1R1.csv")])
VALSLTB2 = numpy.array([valfrom("TB0.5L2.csv"),valfrom("TB1.6L2.csv"),valfrom("TB2.4L2.csv"),valfrom("TB3.3L2.csv"),valfrom("TB4.2L2.csv"),valfrom("TB4.8L2.csv"),valfrom("TB6.1L2.csv")])
VALSMTB2 = numpy.array([valfrom("TB0.5M2.csv"),valfrom("TB1.6M2.csv"),valfrom("TB2.4M2.csv"),valfrom("TB3.3M2.csv"),valfrom("TB4.2M2.csv"),valfrom("TB4.8M2.csv"),valfrom("TB6.1M2.csv")])
VALSRTB2 = numpy.array([valfrom("TB0.5R2.csv"),valfrom("TB1.6R2.csv"),valfrom("TB2.4R2.csv"),valfrom("TB3.3R2.csv"),valfrom("TB4.2R2.csv"),valfrom("TB4.8R2.csv"),valfrom("TB6.1R2.csv")])

VALSL = numpy.array([valfrom("T0.5L1.csv"),valfrom("T1.6L1.csv"),valfrom("T2.4L1.csv"),valfrom("T3.3L1.csv"),valfrom("T4.2L1.csv"),valfrom("T4.8L1.csv"),valfrom("T6.1L1.csv")])
VALSM = numpy.array([valfrom("T0.5M1.csv"),valfrom("T1.6M1.csv"),valfrom("T2.4M1.csv"),valfrom("T3.3M1.csv"),valfrom("T4.2M1.csv"),valfrom("T4.8M1.csv"),valfrom("T6.1M1.csv")])
VALSR = numpy.array([valfrom("T0.5R1.csv"),valfrom("T1.6R1.csv"),valfrom("T2.4R1.csv"),valfrom("T3.3R1.csv"),valfrom("T4.2R1.csv"),valfrom("T4.8R1.csv"),valfrom("T6.1R1.csv")])
VALSL2 = numpy.array([valfrom("T0.5L2.csv"),valfrom("T1.6L2.csv"),valfrom("T2.4L2.csv"),valfrom("T3.3L2.csv"),valfrom("T4.2L2.csv"),valfrom("T4.8L2.csv"),valfrom("T6.1L2.csv")])
VALSM2 = numpy.array([valfrom("T0.5M2.csv"),valfrom("T1.6M2.csv"),valfrom("T2.4M2.csv"),valfrom("T3.3M2.csv"),valfrom("T4.2M2.csv"),valfrom("T4.8M2.csv"),valfrom("T6.1M2.csv")])
VALSR2 = numpy.array([valfrom("T0.5R2.csv"),valfrom("T1.6R2.csv"),valfrom("T2.4R2.csv"),valfrom("T3.3R2.csv"),valfrom("T4.2R2.csv"),valfrom("T4.8R2.csv"),valfrom("T6.1R2.csv")])

VALSLMID = numpy.array([valfrom("MID0.5L1.csv"),valfrom("MID1.6L1.csv"),valfrom("MID2.4L1.csv"),valfrom("MID3.3L1.csv"),valfrom("MID4.2L1.csv")])
VALSMMID = numpy.array([valfrom("MID0.5M1.csv"),valfrom("MID1.6M1.csv"),valfrom("MID2.4M1.csv"),valfrom("MID3.3M1.csv"),valfrom("MID4.2M1.csv")])
VALSRMID = numpy.array([valfrom("MID0.5R1.csv"),valfrom("MID1.6R1.csv"),valfrom("MID2.4R1.csv"),valfrom("MID3.3R1.csv"),valfrom("MID4.2R1.csv")])
VALSLMID2 = numpy.array([valfrom("MID0.5L2.csv"),valfrom("MID1.6L2.csv"),valfrom("MID2.4L2.csv"),valfrom("MID3.3L2.csv"),valfrom("MID4.2L2.csv")])
VALSMMID2 = numpy.array([valfrom("MID0.5M2.csv"),valfrom("MID1.6M2.csv"),valfrom("MID2.4M2.csv"),valfrom("MID3.3M2.csv"),valfrom("MID4.2M2.csv")])
VALSRMID2 = numpy.array([valfrom("MID0.5R2.csv"),valfrom("MID1.6R2.csv"),valfrom("MID2.4R2.csv"),valfrom("MID3.3R2.csv"),valfrom("MID4.2R2.csv")])

VALSNOTHING = numpy.array([valfrom("MID0.5L2.csv")])
VALS6NOTHING = numpy.array([valfrom("MID0.5L2.csv")])

VALS6L = numpy.array([valfrom("MID0.5L2.csv")])
VALS6M = numpy.array([valfrom("MID0.5L2.csv")])
VALS6R = numpy.array([valfrom("MID0.5L2.csv")])

VALS6LTB = numpy.array([])
VALS6MTB = numpy.array([])
VALS6RTB = numpy.array([])

plt.plot(GAPS,VALSLTB)
plt.plot(GAPS,VALSMTB)
plt.plot(GAPS,VALSRTB)

plt.figure

plt.plot(GAPS,VALSL)
plt.plot(GAPS,VALSM)
plt.plot(GAPS,VALSR)

plt.figure

plt.plot(GAPS2,VALSLMID)
plt.plot(GAPS2,VALSMMID)
plt.plot(GAPS2,VALSRMID)
"""