from datetime import datetime

from ._helpers import noteAction,checkNotebook
from ..files import loadNotes,saveNotes,modDateFormat

@noteAction
class Create:
    def __init__(self,settings,notes=None):
        self.settings=settings
        notebook=self.getNotebook()
        title=self.getTitle()
        if notes is None:notes=loadNotes()
        self.createNote(notes,title,notebook)

    def getNotebook(self):
        nb=checkNotebook(self.settings)
        if nb is None:
            nb='default'
        return nb

    def getTitle(self):
        title=' '.join(self.settings)
        while not title.strip():
            title=input('Insert note title: ')
        return title

    def createNote(self,notes,title,notebook):
        note=self.createNoteDict(title,notebook)
        notes.append(note)
        saveNotes(notes)
        print('Created note %s'%len(notes))

    def createNoteDict(self,title,notebook):
        return {
            'title':title,
            'content':'',
            'modDate':datetime.now().strftime(modDateFormat),
            'notebook':notebook
        }
