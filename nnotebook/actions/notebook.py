from datetime import datetime

from ._helpers import noteAction,NoteGetter,checkNotebook
from ..files import loadNotes,saveNotes,modDateFormat

@noteAction
class Notebook:
    def __init__(self,settings):
        self.notes,self.settings=loadNotes(),settings
        nb=checkNotebook(settings)
        self.note=NoteGetter(self.notes,self.settings,nb).getNote()
        if self.note is not None:
            self.changeNotebook()

    def changeNotebook(self):
        notebook=self.getNotebook()
        self.note['notebook']=notebook
        self.note['modDate']=datetime.now().strftime(modDateFormat)
        print('Note notebook changed')
        saveNotes(self.notes)

    def getNotebook(self):
        notebook=' '.join(self.settings)
        while not notebook.strip():
            notebook=input('Insert new note notebook: ')
        return notebook
