from ._helpers import noteAction,NoteGetter
from ..files import loadNotes,saveNotes

@noteAction
class Display:
    def __init__(self,settings):
        self.notes=loadNotes()
        self.note=NoteGetter(self.notes,settings).getNote()
        self.displayNoteOrNotes()

    def displayNoteOrNotes(self):
        if self.note is None:
            self.displayNotes()
        else:
            self.displayNote()

    def displayNotes(self):
        self.trueNotes=[]
        self.printNotes()
        saveNotes(self.trueNotes)

    def printNotes(self):
        i=0
        for note in self.notes:
            if 'end' not in note:
                i+=1
                self.trueNotes.append(note)
                print('%s. %s'%(i,note['title']))

    def displayNote(self):
        print('Note "%s":\n'%self.note['title'])
        print(self.note['content'])
