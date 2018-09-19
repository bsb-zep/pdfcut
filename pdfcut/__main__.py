from step_one import workflow_controller as step_one
from step_two import workflow_controller as step_two

print('\n')
print('pdfcut v3.1 - record and apply granular pdf page numbers')
print('--------------------------------------------------------\n')

print('Bitte Workflow auswählen:')
print('  1 - Erfassung von Seitenzahlen')
print('  2 - Granulare PDFs anhand erfasster Seitenzahlen erstellen\n')

stepChoice = input("Workflow: \n\n")

if str(stepChoice) == '1':
    step_one.go()
elif str(stepChoice) == '2':
    step_two.go()
else:
    print('Ungültige Auswahl.')