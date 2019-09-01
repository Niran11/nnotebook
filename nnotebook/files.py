from os import mkdir,mknod,chdir
from os.path import expanduser,exists
from datetime import datetime
from json import loads,dumps
from json.decoder import JSONDecodeError

modDateFormat='%H:%M:%S %d.%m.%Y'

def openNotes(permissions):
    try:
        notesFile=open('notes.json',permissions)
    except FileNotFoundError:
        mknod('notes.json')
        notesFile=open('notes.json',permissions)
    return notesFile

def changeDir():
    notesPath='%s/.nnotebook'%expanduser('~')
    if not exists(notesPath):mkdir(notesPath)
    chdir(notesPath)

def loadNotes():
    notesFile=openNotes('r')
    try:
        notes=loads(notesFile.read())
    except JSONDecodeError:
        notes=[]
    notesFile.close()
    return notes

def saveNotes(notes):
    notesFile=openNotes('w')
    notes.sort(key=lambda x:datetime.strptime(x['modDate'],modDateFormat),reverse=True)
    notesFile.write(dumps(notes))
    notesFile.close()
