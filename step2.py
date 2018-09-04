import csv
import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog

def applycsv(firstpage, lastpage, sourcepdf, destinationpdfprefix, outputTargetDir):
    output = PdfFileWriter()
    firstpage -= 1
    input = PdfFileReader(open(sourcepdf, "rb"))
    for i in range(firstpage, lastpage):
        output.addPage(input.getPage(i))
    outputTargetUri = outputTargetDir + '/' + destinationpdfprefix + str(applycounter) + ".pdf"
    print('  Ziel: ' + outputTargetUri)
    try:
        outputStream = io.FileIO(outputTargetUri, "wb")
        output.write(outputStream)
        outputStream.close()
    except:
        raise RuntimeError
    print('\n')

csvlist = list()

print('\n')
newcsvfilepath = filedialog.askopenfilename(title = "Quell-Datei für Seitenangaben auswählen", filetypes = (('CSV-Dateien', '.csv'), ))
csvfilename = newcsvfilepath
with open(csvfilename, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row != []:
            csvlist.append(row)
csvlistlength = len(csvlist)
print("- Es wurden " + str(csvlistlength) + " Datensätze ausgelesen")

print('\n')
outputTargetDir = filedialog.askdirectory(initialdir="/",title='Bitte Zielverzeichnis für erstellte PDFs wählen')
print('Speichere PDFs nach: ' +  str(outputTargetDir) )

print('\n')
csvOffset = input("- Artikel-Offset (Eingabetaste für kein): ")
if csvOffset == "":
    csvOffset = 0
    print("  Kein Artikel-Offset ausgewählt.")
else:
    print("  Es werden jeweils " + csvOffset + " Seiten vor und nach einem Artikelumbruch mit gespeichert.")

print('\n')
totalOffset = input("- Seitenverschiebung (Eingabetaste für kein): ")
if totalOffset == "":
    totalOffset = 0
    print("  Keine Seitenverschiebung ausgewählt.")
else:
    print("  Die  " + totalOffset + " ersten Seiten der Quell-PDF-Datei werden in der Zählung übersprungen.")

print('\n')
for i in range(csvlistlength):
    if int(csvlist[i][0]) > int(csvlist[i][1]):
        print("- Fehler im Seitenbereich: " + str(csvlist[i]))
print("- Prüfung der Seitenbereichsdaten beendet.")
print('\n')

singlepagepdf = 0
for i in range(csvlistlength):
    if int(csvlist[i][0]) == int(csvlist[i][1]):
        singlepagepdf = singlepagepdf + 1
print("- Prüfangaben für das Inhaltsverzeichnis:")
print("  Anzahl Elemente: " + str(csvlistlength))
print("  Einzelseiten-Elemente: " + str(singlepagepdf))

print('\n')
csvdecision = input("- PDF-Dateien generieren? (j/n)")

if csvdecision == str("j"):
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
    print('\n')
    partdestinationname = str(input("  Präfix der Zieldateien ohne Endung: ") + "-")
    csvdecision = input("- Fortfahren? (j/n)")
if csvdecision == "j":
    applycounter = 0
    for i in range(csvlistlength):
        print("  Verarbeite Seitenabschnitt " + str(1+i) + " von " + str(csvlistlength) + "...")
        applycounter += 1
        applycsv(int(csvlist[i][0]) - int(csvOffset) + int(totalOffset), int(csvlist[i][1]) + int(csvOffset) + int(totalOffset), completefilename, partdestinationname, outputTargetDir)
        print("  Verarbeitung abgeschlossen.")
    print('\n')
    print("PDF-Segmente abgelegt nach " + outputTargetDir + " mit dem Präfix " + partdestinationname + ".")
else:
    exit()
