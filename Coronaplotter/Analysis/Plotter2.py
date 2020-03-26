import os
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import csv
import xarray as xr
LIZT = []

for filename in os.listdir("."):
    if filename.endswith(".csv"):
        LIZT.append(filename)

#Creating empty xarray

df = xr.DataArray(data=[numpy.transpose(numpy.empty([8,22]).astype(int))], dims = ["Giorno", "Regione","Dati"], coords = ({"Regione": ['Lombardia', 'Emilia Romagna', 'Veneto', 'Piemonte',
                                    'Marche', 'Toscana', 'Liguria', 'Lazio', 'Friuli V.G.',
                                     'Campania', 'Puglia', 'Bolzano', 'Sicilia', 'Trento',
                                     'Abruzzo', 'Umbria', 'Sardegna', 'Calabria',
                                     "Valle d'Aosta", 'Molise', 'Basilicata','TOTALE'],
                                    "Dati":['Ricoverati con sintomi', 'Terapia intensiva',
                                     'Isolamento domiciliare', 'Totale attualmente positivi',
                                     'DIMESSI GUARITI', 'DECEDUTI', 'CASI TOTALI', 'TAMPONI'],
                                    "Giorno":[0]}))
                                    

day = 2

# Reading data from csv files and adding it to the xarray

for file in LIZT:
    csvfile = open(file, "r")
    reader = csv.reader(csvfile, delimiter=",", quotechar = "|")
    data = list(reader)
    data= numpy.asarray(data)
    for i,b in numpy.ndindex(22,8):
        data[i,b+1]= ("0"+data[i,b+1])
    
    
    VALZ = xr.DataArray(data= [numpy.transpose(data[:,1:].astype(int))], dims = ["Giorno","Dati","Regione"], coords = ({"Regione": data[:,0],"Dati":['Ricoverati con sintomi', 'Terapia intensiva',
                                     'Isolamento domiciliare', 'Totale attualmente positivi',
                                     'DIMESSI GUARITI', 'DECEDUTI', 'CASI TOTALI', 'TAMPONI'],"Giorno":[day]}))
    
    df = xr.concat([df,VALZ], dim = "Giorno")
    day +=1

today = 23

#All of the above code simply loads up the data from the csv files in the folder into an xarray with three axes: Day, DATA and Region.

#It's easy enough to select by days but I'm mostly looking at the whole range of a specific piece of data in a specific region. That's what the Sel() func is for

"""
'Ricoverati con sintomi' : "Hospitalized with symptoms"
'Terapia intensiva' : "ICU"
'Isolamento domiciliare' : "Self-Isolation"
'Totale attualmente positivi' : "Total number of active cases"
'DIMESSI GUARITI' :"Cured"
'DECEDUTI' : "Deaths"
'CASI TOTALI' : "Total number of cases"
'TAMPONI' : "Tests"

You can unquote this dict and just use ITA["Tests"] or ITA["Deaths"] throughout.

ITA = {'Hospitalized with symptoms' : "Ricoverati con sintomi", 'ICU' : "Terapia intensiva",
'Self-Isolation' : "Isolamento domiciliare", 'Total number of active cases' : "Totale attualmente positivi",
'Cured' :"DIMESSI GUARITI",
'Deaths' : "DECEDUTI",
'Total number of cases' : "CASI TOTALI",
'Tests' : "TAMPONI"}

"""

def Sel(Regione,Dati):
    """returns the Region/Data slice from the xarray,as a numpy array"""
    return numpy.asarray(df.sel(Dati = Dati, Regione = Regione))[1:]

def Increaseoverndays(X,ndays):
    """The increase of whatever Data 1D numpy array over ndays. If X is the total number of deaths, the day-by-day increase is given by Increaseoverndays(X,1)"""
    M = numpy.empty((len(X)//ndays)-1)
    for i in range((len(X)//ndays)-1):
        M[i] = X[ndays*(i+1)]-X[ndays*i]
    return M

def PercIncreaseoverndays(X,ndays):
    """The percentage increase of whatever Data 1D numpy array over ndays. If X is the total number of deaths, the day-by-day percentage increase is given by PercIncreaseoverndays(X,1)"""
    M = numpy.empty((len(X)//ndays)-1)
    for i in range((len(X)//ndays)-1):
        M[i] = (X[ndays*(i+1)]-X[ndays*i])/X[ndays*i]
    return M*100

def average (X, ndays):
    """averages 1D numpy array X over ndays. I use it to smooth very unsmooth data ( e.g. tests are carried out daily but take varying amounts of time to return a result for example, so sometimes the day to day increase in cases is higher than the day to day increase in tests)"""
    M = numpy.empty(len(X)-ndays+1)
    
    for i in range(len(M)):
        for b in range(ndays):
            M[i] += X[i+b]
    M = M/ndays
    return M

#Some structures I find useful when showing people stuff

def ComparedatabyRegion(data,Regions,n):
    """Plots percentage daily increase of a certain piece of data in the last n days
    for each region in list Regions"""
    plt.figure(1)
    plt.title("Aumento percentuale di " + data)
    for reg in Regions:
        Y = PercIncreaseoverndays(Sel(reg,data),1)[-n:]
        X = range(today-len(Y)+1,today+1)
        hsv = plt.get_cmap('hsv')
        col = hsv(numpy.random.uniform())
        plt.plot(X, Y, label = (reg), color = col)
        #The next couple lines add a trendline fit
        """
        N = 2 #Polynomial fit degree
        plt.plot(numpy.unique(X), numpy.poly1d(numpy.polyfit(X, Y, N))(numpy.unique(X)), color = col)
        """
        plt.legend()
    
ComparedatabyRegion("Ricoverati con sintomi", ["Lombardia", "Veneto", "Emilia Romagna"],5)

def CompareDatainRegion(Datapieces,region,n):
    """Plots percentage daily increase of a certain piece of data in the last n 
    days for each region in list Regions"""
    plt.figure(2)
    plt.title(region)
    for data in Datapieces:
        Y = PercIncreaseoverndays(Sel(region,data),1)[-n:]
        X = range(today-len(Y)+1,today+1)
        hsv = plt.get_cmap('hsv')
        col = hsv(numpy.random.uniform())
        plt.plot(X, Y, label = (data), color = col)
        #The next couple lines add a trendline fit
        """
        N = 2 #Polynomial fit degree
        plt.plot(numpy.unique(X), numpy.poly1d(numpy.polyfit(X, Y, N))(numpy.unique(X)), color = col)
        """
        plt.legend()

CompareDatainRegion(["Ricoverati con sintomi","DECEDUTI"], "Lombardia",15)

#Just something I think may be important to look at.

def Positivetestsratio(Regions,n):
    """Plots percentage of positive tests in the last n days
    for each region in list Regions"""
    plt.figure(3)
    plt.title("Percentage of positive tests by region")
    for region in Regions:
        Y = (100*Increaseoverndays(Sel(region,"CASI TOTALI"),1)/Increaseoverndays(Sel(region,"TAMPONI"),1))[-n:]
        X = range(today-len(Y)+1,today+1)
        hsv = plt.get_cmap('hsv')
        col = hsv(numpy.random.uniform())
        plt.plot(X, Y, label = (region), color = col)
        #The next couple lines add a trendline fit
        """
        N = 2 #Polynomial fit degree
        plt.plot(numpy.unique(X), numpy.poly1d(numpy.polyfit(X, Y, N))(numpy.unique(X)), color = col)
        """
        plt.legend()

Positivetestsratio(["Lombardia", "Veneto"],10)