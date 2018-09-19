import winsound
from tkinter import filedialog


def warninglongarea():
    beeptone = int(1500)
    beeplength = int(900)
    winsound.Beep(beeptone, beeplength)
    print("Achtung: Langer Abschnitt!")

def setCsvWritingTarget():
    csvfilename = filedialog.asksaveasfilename(title = "Ziel-Datei auswählen", 
                                               filetypes = (('CSV-Dateien', '.csv'), ))
    try:
        testfile = open(csvfilename, "w")
        testfile.close()
        return csvfilename
    except:
        print('Die Ziel-Datei konnte nicht geöffnet werden.')

def correctinput(wrongvaluename, wrongvalue):
    print(str(wrongvaluename) + " war keine Zahl.")
    print("Eingabe war: " + str(wrongvalue))
    correctedvalue = input("Bitte korrigieren: ")
    return correctedvalue

def receivepagenumber(datadescription):
    newpage = str()    
    while newpage == "":
        newpage = input(datadescription + ": ")
    while newpage.isdigit() == False:
        newpage = correctinput(datadescription, newpage)
    return int(newpage)