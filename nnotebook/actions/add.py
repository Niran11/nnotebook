from ._helpers import noteAction,NoteGetter
from .create import Create
from ..files import loadNotes,saveNotes

@noteAction
class Add:
    def __init__(self,settings):
        self.notes,self.settings=loadNotes(),settings
        self.note=NoteGetter(self.notes,self.settings).getNote()
        self.checkAndChangeNote()

    def checkAndChangeNote(self):
        if self.note is not None:
            self.addToNote()
        elif not len(self.settings):
            Create(self.settings,self.notes)

    def addToNote(self):
        self.changeNoteContent()
        saveNotes(self.notes)
        print('Added text to note "%s"'%(self.note['title']))


    def changeNoteContent(self):
        newText=' '.join(self.settings)
        if self.note['content']:self.note['content']+='\n'
        self.note['content']+=newText
