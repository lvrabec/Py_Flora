import os
import json

''' 
   Provjere postoji li datoteka ili neka putanja do datoteke 
'''
def isFilePathExists(filePath):
    return os.path.exists(filePath)

'''
    Metoda za otvaranje konekcije prema datoteci navedenoj u "filePath" varijabli
    Konekcija prema datoteci će biti otvorena za čitanje
'''
def ReadFromFile(filePath):
    try:
        with open(filePath, 'r') as file_reader:
            dict_json = json.load(file_reader)
            return dict_json
    except Exception as ex:
        print(f'Dogodila se pogreska {ex}')

'''
    Otvaranje konekcije prema datoteci navedenoj u "filePath" varijabli
    Konekcija prema datoteci će biti otvorena za pisanje ili dodavanje
'''
def WriteToFile(data, filePath, attr):
    try:
        with open(filePath, 'w') as file_writer:
            json.dump(data, file_writer, indent=4)
    except Exception as ex:
        print(f'Dogodila se pogreska {ex}')


