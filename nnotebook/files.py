from os import mkdir,mknod,chdir
from os.path import expanduser,exists
from datetime import datetime
from json import loads,dumps
from json.decoder import JSONDecodeError

def openNotes(perm):
    try:
        notesFile=open('main.json',perm)
    except FileNotFoundError:
        mknod('main.json')
        notesFile=open('main.json',perm)
    return notesFile

def changeDir():
    notesPath='%s/.notes'%expanduser('~')
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
    notes.sort(key=lambda x:datetime.strptime(x['modDate'],'%Y-%m-%d %H:%M:%S'))
    notesFile.write(dumps(notes))
    notesFile.close()
