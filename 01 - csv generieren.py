import csv
import winsound
import os
import sys
from tkinter import filedialog

print("Seitenzahlerfassung für CSV-Datei")
stopsignal = str()
newfirstpage = str()
newlastpage = str()

def warninglongarea():
    beeptone = int(1500)
    beeplength = int(900)
    winsound.Beep(beeptone, beeplength)
    print("Achtung: Langer Abschnitt!")

def correctinput(wrongvaluename, wrongvalue):
    print(str(wrongvaluename) + " war keine Zahl.")
    print("Eingabe war: " + str(wrongvalue))
    correctedvalue = input("Bitte korrigieren: ")
    return correctedvalue

def receivepage(datadescription):
    newpage = str()    
    while newpage == "":
        newpage = input(datadescription + ": ")
    while newpage.isdigit() == False:
        newpage = correctinput(datadescription, newpage)
    return int(newpage)

newcsvfilepath = filedialog.asksaveasfilename(title = "Ziel-Datei auswählen", filetypes = (('CSV-Dateien', '.csv'), ))
print("Arbeitsverzeichnis ist: " + str(newcsvfilepath))
csvfilename = newcsvfilepath
testfile = open(csvfilename, "w")
print(" Datei wurde geöffnet.")
testfile.close()

while stopsignal != "n":
    print("")
    newcsvfile = open(csvfilename, "a", newline='')    
    stopsignal = str()
    
    newfirstpage = receivepage("Von")
    newlastpage = receivepage("Bis")
  
    if newlastpage-newfirstpage > 80:
        warninglongarea()

    while newlastpage < newfirstpage:
        if newlastpage < newfirstpage:
            print("Fehler: Letzte Seite liegt vor erster Seite.")
            print("Neue Erfassung des aktuellen Abschnitts:")

        newfirstpage = receivepage("Abschnittsanfang: ")
        newlastpage = receivepage("Seitenende: ")
        
    newcsvwriter = csv.writer(newcsvfile, delimiter=",")
    pageareadata = [[newfirstpage, newlastpage]]
    newcsvwriter.writerows(pageareadata)
    newcsvfile.close()
    print("OK: " + str(newfirstpage) + " bis " + str(newlastpage))
    stopsignal = str(input("Weiter?  Enter(Ja) / n(Nein) / k(Korrektur) "))

    if stopsignal == "k":
        correctfile = open(csvfilename, "r")
        lines = correctfile.readlines()
        correctfile.close()
        correctfile = open(csvfilename, "w")
        correctfile.writelines([item for item in lines[:-1]])
        correctfile.close()
        print("Zuletzt gespeicherter Abschnitt wurde gelöscht.")
        stopsignal = str(input("Weiter?  Enter(Ja) / n(Nein) "))

    
else:
    print("Erfassung beendet.")
    newcsvfile.close()
