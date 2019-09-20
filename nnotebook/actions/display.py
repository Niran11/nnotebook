from datetime import datetime

from ._helpers import noteAction,NoteGetter,checkNotebook
from ..files import loadNotes,saveNotes,modDateFormat

@noteAction
class Display:
    def __init__(self,settings,noMatchesWarn=False):
        self.notes,self.settings=loadNotes(),settings
        self.notebook=checkNotebook(self.settings)
        self.note=NoteGetter(self.notes,self.settings,
                             self.notebook,noMatchesWarn).getNote()
        self.displayNoteOrNotes()

    def displayNoteOrNotes(self):
        if self.note is None:
            self.displayNotes()
        else:
            self.displayNote()

    def displayNotes(self):
        self.trueNotes=[]
        self.notes.sort(key=lambda x:datetime.strptime(x['modDate'],modDateFormat),
                        reverse=True)
        self.printNotes()
        saveNotes(self.trueNotes)

    def printNotes(self):
        i=0
        for note in self.notes:
            if 'end' not in note:
                i+=1
                self.processNote(note,i)

    def processNote(self,note,i):
        self.trueNotes.append(note)
        if not self.notebook or note['notebook']==self.notebook:
            print('%s. %s/%s (%s)'%(i,note['notebook'],
                                    note['title'],note['modDate']))

    def displayNote(self):
        print('Note %s/%s (mod. date: %s):\n'%(self.note['notebook'],
                                               self.note['title'],
                                               self.note['modDate']))
        print(self.note['content'])
