print('\n')
print('pdfcut v3.1 - record and apply granular pdf page numbers')
print('--------------------------------------------------------\n')

print('Bitte Workflow auswählen:')
print('  1 - Erfassung von Seitenzahlen')
print('  2 - Granulare PDFs anhand erfasster Seitenzahlen erstellen\n')

stepChoice = input("Workflow: \n\n")

if str(stepChoice) == '1':
    __import__('step1')
elif str(stepChoice) == '2':
    __import__('step2')
else:
    print('Ungültige Auswahl.')