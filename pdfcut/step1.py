# import standard libraries
import csv
import os
import sys

# import local helper library
import step_one


# get csv targe file name
csvTargetPath = step_one.setCsvWritingTarget()

# loop through recording routine
stopsignal = str()
while stopsignal != "n":

    # initialize new loop
    stopsignal = str()
    print("")

    newfirstpage = step_one.receivepagenumber("Erste Seite des Abschnitts: ")
    newlastpage = step_one.receivepagenumber("Letzte Seite des Abschnitts:")
  
    # show alert if range is suspiciously long
    if newlastpage - newfirstpage > 80:
        step_one.warninglongarea()

    # request correction if invalid page range delimiters entered
    while newlastpage < newfirstpage:
        if newlastpage < newfirstpage:
            print("Fehler: Letzte Seite liegt vor erster Seite.")
            print("Neue Erfassung des aktuellen Abschnitts:")

        newfirstpage = step_one.receivepagenumber("Erste Seite des Abschnitts: ")
        newlastpage = step_one.receivepagenumber("Letzte Seite des Abschnitts: ")
    
    # write new from/to page numbers to target file
    csvfileDao = open(csvTargetPath, "a", newline='')
    newcsvwriter = csv.writer(csvfileDao, delimiter=",")
    pageareadata = [[newfirstpage, newlastpage]]
    newcsvwriter.writerows(pageareadata)
    csvfileDao.close()

    # ask about further proceeding
    print("OK: " + str(newfirstpage) + " bis " + str(newlastpage))
    stopsignal = str(input("Weiter?  Enter(Ja) / n(Nein) / l(letzten Abschnitt löschen) "))

    # remove last from/to page number line from target file
    if stopsignal == "l":
        correctfile = open(csvTargetPath, "r")
        lines = correctfile.readlines()
        correctfile.close()
        correctfile = open(csvTargetPath, "w")
        correctfile.writelines([item for item in lines[:-1]])
        correctfile.close()
        print("Zuletzt gespeicherter Abschnitt wurde gelöscht.")
        stopsignal = str(input("Weiter?  Enter(Ja) / n(Nein) "))
 
else:
    # leave recording loop
    print("Erfassung beendet.")
    print("Dateiname: " + csvTargetPath)
    csvfileDao.close()
