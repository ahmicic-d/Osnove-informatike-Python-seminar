import csv
import statistics
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np

with open("statistika2.csv", "r",encoding='utf-8') as f:
    next(f)
    podaci = list(csv.reader(f, delimiter=';'))

for i in podaci:
 print(i)

kategorije = []
for i in podaci:
    kategorije.append(i[0])
kategorije = kategorije[0:]


godina2014 = []
for i in podaci:
 if i[1].isdigit():
  godina2014.append(int(i[1]))
godina2014 = godina2014[0:]

godina2015 = []
for i in podaci:
 if i[2].isdigit():
  godina2015.append(int(i[2]))
godina2015 = godina2015[0:]

godina2016 = []
for i in podaci:
 if i[3].isdigit():
  godina2016.append(int(i[3]))
godina2016 = godina2016[0:]

godina2017 = []
for i in podaci:
 if i[4].isdigit():
  godina2017.append(int(i[4]))
godina2017 = godina2017[0:]

godina2018 = []
for i in podaci:
 if i[5].isdigit():
  godina2018.append(int(i[5]))
godina2018 = godina2018[0:]


godina2019 = []
for i in podaci:
 if i[6].isdigit():
  godina2019.append(int(i[6]))
godina2019 = godina2019[0:]





def suma(y):
    a = 0
    for i in y:
        a += i
    return a

def aritm(y):
    a = 0
    x = 0
    for i in y:
        a = float(i) + a
    x = round (a/len(y), 2)
    return x

# def mod(y):
#     return statistics.mode(y)
def mod(y):
    sortirana_lista = sorted(y)
    mode = min(sortirana_lista)
    max_count = sortirana_lista.count(mode)
    for i in sortirana_lista:
        if (sortirana_lista.count(i) >= max_count):
            mode = i
            max_count = sortirana_lista.count(i)
            print(mode)
        else:
             print("None")



def median(y):
    sortirana_lista = sorted(y)
    x = len(y)
    if x%2 != 0:
        median = sortirana_lista[(x//2)]
    else:
        median = (sortirana_lista[x//2] + sortirana_lista[(x//2)-1])/2
    return median


def devijacija(y):
    suma = 0
    for x in y:
        suma += ((x - sum(y)/len(y))**2)
    a = (suma/(len(y)-1))**0.5
    return round(a, 2)


def minimum(y):
    najmanji=int(y[0])
    najveci=int(y[0])
    for i in y:
        if int(i)<najmanji:
            najmanji=int(i)
    return najmanji

def maximum(y):
    najveci=int(y[0])
    najmanji=int(y[0])
    for i in y:
        if int(i)>najveci:
            najveci=int(i)
    return najveci


with open("ispis.txt", "w") as my_output_file:
    with open("statistika2.csv", "r") as my_input_file:
        [my_output_file.write("\t ".join(row) + '\n') for row in csv.reader(my_input_file)]

    my_output_file.writelines(["Suma jest: \t", str(suma(godina2014)),";\t", str(suma(godina2015)),";\t", str(suma(godina2016)),";\t", str(suma(godina2017)),";\t", str(suma(godina2018)),";\t", str(suma(godina2019))])
    my_output_file.writelines(["\nAritm. sredina je: \t", str(aritm(godina2014)),";\t", str(aritm(godina2015)),";\t", str(aritm(godina2016)),";\t", str(aritm(godina2017)),";\t", str(aritm(godina2018)),";\t", str(aritm(godina2019))])
    my_output_file.writelines(["\nMod jest: \t", str(mod(godina2014)),";\t", str(mod(godina2015)),";\t", str(mod(godina2016)),";\t", str(mod(godina2017)),";\t", str(mod(godina2018)),";\t", str(mod(godina2019))])
    my_output_file.writelines(["\nMedijan je: \t", str(median(godina2014)),";\t", str(median(godina2015)),";\t", str(median(godina2016)),";\t", str(median(godina2017)),";\t", str(median(godina2018)),";\t", str(median(godina2019))])
    my_output_file.writelines(["\nDevijacija je: \t", str(devijacija(godina2014)),";\t", str(devijacija(godina2015)),";\t", str(devijacija(godina2016)),";\t", str(devijacija(godina2017)),";\t", str(devijacija(godina2018)),";\t", str(devijacija(godina2019))])
    my_output_file.writelines(["\nMinimum je: \t", str(minimum(godina2014)),";\t", str(minimum(godina2015)),";\t", str(minimum(godina2016)),";\t", str(minimum(godina2017)),";\t", str(minimum(godina2018)),";\t", str(minimum(godina2019))])
    my_output_file.writelines(["\nMaximum je: \t", str(maximum(godina2014)),";\t", str(maximum(godina2015)),";\t", str(maximum(godina2016)),";\t", str(maximum(godina2017)),";\t", str(maximum(godina2018)),";\t", str(maximum(godina2019))])
    my_output_file.close()




#----------------------------------------------------------------------GRAFIKON----------------------------------------------------------------
# X - Vrijednosti
godine = ['2014. godina', '2015. godina', '2016. godina', '2017. godina', '2018. godina', '2019. godina']
x = np.arange(len(godine))
width = 0.2

# Y - Vrijednosti
Asredina_ = [aritm(godina2014), aritm(godina2015), aritm(godina2016), aritm(godina2017), aritm(godina2018), aritm(godina2019)]
Med_ = [median(godina2014), median(godina2015), median(godina2016), median(godina2017), median(godina2018), median(godina2019)]
Dev_ = [devijacija(godina2014), devijacija(godina2015), devijacija(godina2016), devijacija(godina2017), devijacija(godina2018), devijacija(godina2019)]
Min_ = [minimum(godina2014), minimum(godina2015), minimum(godina2016), minimum(godina2017), minimum(godina2018), minimum(godina2019)]
Max_ = [maximum(godina2014), maximum(godina2015), maximum(godina2016), maximum(godina2017), maximum(godina2018), maximum(godina2019)]

# Crtanje grafikona
stupci1 = plt.bar(x-width/0.67, Asredina_, width, label = 'A. sredina', color="Blue",  zorder=2)
stupci2 = plt.bar(x-width/2, Med_, width, label = 'Medijan', color="Red", zorder=2)
stupci3 = plt.bar(x+width/2, Dev_, width, label = 'Devijacija', color="Green", zorder=2)
stupci4 = plt.bar(x+width/0.67, Min_, width, label = 'Minimum', color="Purple", zorder=2)

plt.title('Usporedba rezultata od 2014. do 2019. godine')
plt.xticks(x, godine)
plt.xlabel('Godine')
plt.ylabel('Iznos')
plt.grid(linestyle="-", axis='y', alpha=0.6, zorder=1)
plt.legend()
plt.show()
plt.savefig('GRAF.png')