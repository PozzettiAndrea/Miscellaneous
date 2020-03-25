import csv
import matplotlib.pyplot as plt
import os

nc = 0
LIST = []
LIST2 = []
for filename in os.listdir("."):
    if filename.endswith(".csv"):
        LIST.append(filename)

print(LIST2)

DICT = {'DM0.5L1.CSV':[50,100,220,260], 'DM0.5M1.CSV':[17,72,174,233], 'DM0.5R1.CSV':[15,27,130,173],
        'DM1.6L1.CSV':[20,34,90,130], 'DM1.6M1.CSV':[13,38,130,165], 'DM1.6R1.CSV':[60,95,160,210],
        'DM2.4L1.CSV':[15,40,140,160], 'DM2.4M1.CSV':[15,30,100,140], 'DM2.4R1.CSV':[13,37,117,138],
        'DM3.2L1.CSV':[25,60,160,200], 'DM3.2M1.CSV':[20,50,140,180], 'DM3.2R1.CSV':[25,50,100,125],
        'JM0.5L1.CSV':[20,60,160,190], 'JM0.5M1.CSV':[32,70,180,230], 'JM0.5R1.CSV':[13,37,84,113],
        'JM1.6L1.CSV':[25,56,125,147], 'JM1.6M1.CSV':[15,37,100,137], 'JM1.6R1.CSV':[15,36,80,102],
        'JM2.4L1.CSV':[13,30,80,110], 'JM2.4M1.CSV':[12,32,67,89], 'JM2.4R1.CSV':[15,38,107,127],
        'JM3.3L1.CSV':[11,22,65,96], 'JM3.3M1.CSV':[15,30,72,93], 'JM3.3R1.CSV':[10,30,85,117],
        'JM4.2L1.CSV':[8,31,83,98], 'JM4.2M1.CSV':[1,20,76,102], 'JM4.2R1.CSV':[10,27,83,105],
        'JM4.8L1.CSV':[12,32,78,10], 'JM4.8M1.CSV':[6,24,80,117], 'JM4.8R1.CSV':[9,23,80,100],
        'JM6.2L1.CSV':[27,43,80,99], 'JM6.2M1.CSV':[10,24,69,96], 'JM6.2R1.CSV':[24,74,140,185],
        'MID0.5L1.CSV':[17,43,100,130], 'MID0.5M1.CSV':[23,45,104,140], 'MID0.5R1.CSV':[6,30,69,99],
        'MID1.6L1.CSV':[15,49,105,129], 'MID1.6M1.CSV':[18,35,61,104], 'MID1.6R1.CSV':[10,40,90,120],
        'MID2.4L1.CSV':[16,39,71,91], 'MID2.4M1.CSV':[17,39,76,94], 'MID2.4R1.CSV':[11,28,91,136],
        'MID3.3L1.CSV':[15,30,77,102], 'MID3.3M1.CSV':[12,27,62,83], 'MID3.3R1.CSV':[8,27,86,118],
        'MID4.2L1.CSV':[14,45,113,141], 'MID4.2M1.CSV':[5,16,47,74], 'MID4.2R1.CSV':[16,71,130,174], 
        'T0.5L1.CSV':[17,54,136,181], 'T0.5M1.CSV':[14,78,149,203], 'T0.5R1.CSV':[28,116,251,310],
        'T1.6L1.CSV':[0,36,169,241], 'T1.6M1.CSV':[29,102,258,315], 'T1.6R1.CSV':[33,49,126,164],
        'T2.4L1.CSV':[30,60,120,160], 'T2.4M1.CSV':[30,60,120,160], 'T2.4R1.CSV':[50,70,160,180],
        'T3.3L1.CSV':[30,60,125,160], 'T3.3M1.CSV':[20,30,90,120], 'T3.3R1.CSV':[9,36,90,125],
        'T4.2L1.CSV':[12,37,87,125], 'T4.2M1.CSV':[18,44,96,123], 'T4.2R1.CSV':[14,47,100,126],
        'T4.8L1.CSV':[13,35,66,86], 'T4.8M1.CSV':[185,215,250,280], 'T4.8R1.CSV':[15,36,80,107],
        'T6.1L1.CSV':[7,27,73,98], 'T6.1M1.CSV':[17,39,75,103], 'T6.1R1.CSV':[28,46,86,113],
        'TB0.5L1.CSV':[28,66,160,200], 'TB0.5M1.CSV':[30,60,166,198], 'TB0.5R1.CSV':[50,100,200,240],
        'TB1.6L1.CSV':[25,75,200,250], 'TB1.6M1.CSV':[200,240,320,360], 'TB1.6R1.CSV':[26,57,140,160],
        'TB2.4L1.CSV':[2,4,5,7], 'TB2.4M1.CSV':[2,4,5,7], 'TB2.4R1.CSV':[2,5,6,10],
        'TB3.3L1.CSV':[22,90,202,250], 'TB3.3M1.CSV':[20,60,160,217], 'TB3.3R1.CSV':[25,55,130,160],
        'TB4.2L1.CSV':[25,60,200,240], 'TB4.2M1.CSV':[25,60,200,225], 'TB4.2R1.CSV':[50,80,160,200],
        'TB4.86L1.CSV':[25,50,130,150], 'TB4.86M1.CSV':[15,30,110,140], 'TB4.86R1.CSV':[25,50,110,130],
        'TB6.1L1.CSV':[25,50,110,140], 'TB6.1M1.CSV':[50,70,150,170], 'TB6.1R1.CSV': [50,100,165,190]} 



for file in LIST2:
    print(file)
    csvfile = open(file, "r")
    reader = csv.reader(csvfile, delimiter=",", quotechar = "|")
    data_list = list(reader)
    
    DATA = []
    for i in range(len(data_list)-18):
       if data_list[i][0]!="nan" and data_list[i][0]!="inf" and data_list[i][1]!="inf":
           try:
               couple= [float(data_list[i][0]),float(data_list[i][1])]
               if float(couple[0])>1:
                   DATA.append(couple)

           except ValueError:
               b=0
    
    DATAA=[]
    MaxV = max(DATA)[0]
    
    print(MaxV)