import csv
import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog

def applycsv(firstpage, lastpage, sourcepdf, destinationpdfprefix):
    output = PdfFileWriter()
    firstpage -= 1
    input = PdfFileReader(open(sourcepdf, "rb"))
    for i in range(firstpage, lastpage):
        output.addPage(input.getPage(i))
    outputStream = io.FileIO("H:/OJSziel/" + destinationpdfprefix + str(applycounter) + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()

csvlist = list()

print("")
newcsvfilepath = filedialog.askopenfilename(title = "Quell-Datei für Seitenangaben auswählen", filetypes = (('CSV-Dateien', '.csv'), ))
csvfilename = newcsvfilepath
with open(csvfilename, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row != []:
            csvlist.append(row)
csvlistlength = len(csvlist)
print("- Es wurden " + str(csvlistlength) + " Datensätze ausgelesen")

print("")
csvOffset = input("- Artikel-Offset (Eingabetaste für kein): ")
if csvOffset == "":
    csvOffset = 0
    print("  Kein Artikel-Offset ausgewählt.")
else:
    print("  Es werden jeweils " + csvOffset + " Seiten vor und nach einem Artikelumbruch mit gespeichert.")

print("")
totalOffset = input("- Seitenverschiebung (Eingabetaste für kein): ")
if totalOffset == "":
    totalOffset = 0
    print("  Keine Seitenverschiebung ausgewählt.")
else:
    print("  Die  " + totalOffset + " ersten Seiten der Quell-PDF-Datei werden in der Zählung übersprungen.")

print("")
for i in range(csvlistlength):
    if int(csvlist[i][0]) > int(csvlist[i][1]):
        print("- Fehler im Seitenbereich: " + str(csvlist[i]))
print("- Prüfung der Seitenbereichsdaten beendet.")
print("")

singlepagepdf = 0
for i in range(csvlistlength):
    if int(csvlist[i][0]) == int(csvlist[i][1]):
        singlepagepdf = singlepagepdf + 1
print("- Prüfangaben für das Inhaltsverzeichnis:")
print("  Anzahl Elemente: " + str(csvlistlength))
print("  Einzelseiten-Elemente: " + str(singlepagepdf))

print("")
csvdecision = input("- PDF-Dateien generieren? (j/n)")

if csvdecision == "j":
    while True:
        try:            
            partfilename = filedialog.askopenfilename(title = "Quell-Datei für PDF auswählen", filetypes = (('PDF-Dateien', '.pdf'), ))
            completefilename = str(partfilename)
            with open(completefilename, "rb") as testfile:
                testfileopen = PdfFileReader(testfile, "rb")
                print("  Datei enthält %d Seiten." % testfileopen.getNumPages())
            break
        except FileNotFoundError:
            print("  Quelldatei unter angegebenem Namen nicht gefunden.")
    print("")
    partdestinationname = str(input("  Präfix der Zieldateien ohne Endung: ") + "-")
    csvdecision = input("- Fortfahren? (j/n)")
if csvdecision == "j":
    applycounter = 0
    for i in range(csvlistlength):
        print("  Verarbeite Seitenabschnitt " + str(1+i) + " von " + str(csvlistlength) + "...")
        applycounter += 1
        applycsv(int(csvlist[i][0]) - int(csvOffset) + int(totalOffset), int(csvlist[i][1]) + int(csvOffset) + int(totalOffset), completefilename, partdestinationname)
        print("  Verarbeitung abgeschlossen.")
    print("")
    print("PDF-Segmente abgelegt nach H:/OJSziel/ mit dem Präfix " + partdestinationname + ".")
else:
    exit()
