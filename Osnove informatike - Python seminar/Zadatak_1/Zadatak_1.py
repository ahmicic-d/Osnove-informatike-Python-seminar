import re
import csv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

ulaz=open('seminar.txt','r',encoding='utf-8')
seminar = ulaz.read()

def words():
    #Broji koliko rijeci ima u .txt file-u
    rijeci = seminar.split()
    broj_rijeci = len(rijeci)
    print("Ukupan broj rijeci jest: ",broj_rijeci)

    #--------------------------------------------Ako moramo regularnim izrazom traziti sve rijeci-----------------------------
    # izraz = '[A-Za-z0-9čČćĆžŽšŠđĐ]+'
    # rijeci = re.findall(izraz, seminar)
    # broj_rijeci = len(rijeci)
    # print("Ukupan broj rijeci jest: ",broj_rijeci)
    #-------------------------------------------------------------------------------------------------------------------------

def spaces():
    #Broji koliko praznih znakova (razmaka) ima u .txt file-u
    izraz = '\ '
    razmak = re.findall(izraz, seminar)
    broj_razmaka = len(razmak)
    print("Ukupan broj praznih znakova (razmaka) jest: ", broj_razmaka)


def numbers():
    #Broji koliko ima brojeva svih vrsta (cijeli, decimalni, razlomci, itd.)
    izraz1 = '[0-9]+((\.|\/|\:)*([0-9]+))*'
    brojevi = re.findall(izraz1, seminar)
    broj_brojeva = len(brojevi)
    print("Ukupna količina brojeva svih vrsta jest: ", broj_brojeva)

def words_with_D():
    #Broji koliko rijeci ima koje počinju sa slovom D
    izraz2 = r'\b(D|d)[A-Za-zčČćĆžŽšŠđĐ]*'
    rijeci_D = re.findall(izraz2, seminar)
    broj_rijeci_D = len(rijeci_D)
    print("Broj rijeci koje počinju sa slovom D jest: ", broj_rijeci_D)

def words_with_A():
    #Broji koliko rijeci ima koje završavaju sa slovom A
    izraz3 = r'[A-Za-zčČćĆžŽšŠđĐ]*(A|a)\b'
    rijeci_A = re.findall(izraz3, seminar)
    broj_rijeci_A = len(rijeci_A)
    print("Broj rijeci koje završavaju sa slovom A jest: ", broj_rijeci_A)



#------------------------------------------------GRAFIKON- NE RADI----------------------------------------------------
slova1 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{1}\b'
slova2 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{2}\b'
slova3 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{3}\b'
slova4 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{4}\b'
slova5 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{5}\b'
slova6 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{6}\b'
slova7 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{7}\b'
slova8 = r'\b[A-Za-zčČćĆžŽšŠđĐ]{8}\b'

pojavljivanje_rijeci1 = int(len(re.findall(slova1, seminar)))
pojavljivanje_rijeci2 = int(len(re.findall(slova2, seminar)))
pojavljivanje_rijeci3 = int(len(re.findall(slova3, seminar)))
pojavljivanje_rijeci4 = int(len(re.findall(slova4, seminar)))
pojavljivanje_rijeci5 = int(len(re.findall(slova5, seminar)))
pojavljivanje_rijeci6 = int(len(re.findall(slova6, seminar)))
pojavljivanje_rijeci7 = int(len(re.findall(slova7, seminar)))
pojavljivanje_rijeci8 = int(len(re.findall(slova8, seminar)))


# plt.style.use('fivethirtyeight')
Slova = ['1 slovo', '2 slova', '3 slova', '4 slova', '5 slova', '6 slova', '7 slova', '8 slova']
pozicije = [1, 2, 3, 4, 5, 6, 7, 8]
x = np.arange(len(Slova))
frekvencija_slova = [pojavljivanje_rijeci1, pojavljivanje_rijeci2, pojavljivanje_rijeci3, pojavljivanje_rijeci4, pojavljivanje_rijeci5, pojavljivanje_rijeci6, pojavljivanje_rijeci7, pojavljivanje_rijeci8]





plt.hist(x, edgecolor='black', align='mid')
plt.title("Frekvencija pojavaljivanja slova")
plt.xlabel("Broj slova u riječi")
plt.ylabel("Broj pojavljivanja")

plt.xticks(pozicije, Slova)
plt.yticks(frekvencija_slova)
plt.show()
plt.savefig("graf.png")




#------------------------------------------POZIVI SVIH FUNKCIJA-----------------------------------------------

words()
spaces()
numbers()
words_with_D()
words_with_A()