import os

''' 
   Provjere postoji li datoteka ili neka putanja do datoteke 
'''
def isFilePathExists(filePath):
    return os.path.exists(filePath)

'''
    Metoda za čitanje iz datoteke navedene u "filePath" varijabli
    Koristi 'r' opciju za čitanje iz datoteke.
'''
def readFromFile(filePath):
    if not isFilePathExists(filePath):
       return f'Datoteka {filePath} ne postoji!'
    try:
        with open(filePath, 'r') as fileReader:
            return fileReader.read()
    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja čitanja iz {filePath} datoteke!'

'''
    Metoda za pisanje u datoteku navedenu u "filePath" varijabli
    Koristi 'w' opciju za pisanje u datoteku i 'a' opciju za dodavanje u datoteku.
    Sadržaj zapisa se nalazi u varijabli 'content'
'''
def writeToFile(filePath, attr, content):
    try:
        with open(filePath, attr) as fileWriter:
            fileWriter.write(content + '\n')
    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja pisanja u {filePath} datoteku!'

