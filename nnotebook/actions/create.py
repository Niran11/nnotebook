from datetime import datetime

from ._helpers import noteAction
from ..files import loadNotes,saveNotes

@noteAction
class Create:
    def __init__(self,settings,notes=None):
        title=self.getTitle(settings)
        if notes is None:notes=loadNotes()
        self.createNote(notes,title)

    def getTitle(self,settings):
        title=' '.join(settings)
        while not title.strip():
            title=input('Insert note title: ')
        return title

    def createNote(self,notes,title):
        note=self.createNoteDict(title)
        notes.append(note)
        saveNotes(notes)
        print('Created note %s'%len(notes))

    def createNoteDict(self,title):
        return {
            'title':title,
            'content':'',
            'modDate':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
