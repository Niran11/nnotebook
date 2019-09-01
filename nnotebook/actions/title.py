from datetime import datetime

from ._helpers import noteAction,NoteGetter
from ..files import loadNotes,saveNotes

@noteAction
class Title:
    def __init__(self,settings):
        self.notes,self.settings=loadNotes(),settings
        self.getNoteAndChangeTitle()

    def getNoteAndChangeTitle(self):
        try:
            self.note,_=NoteGetter(self.notes,self.settings).getNoteById()
        except (ValueError,IndexError):
            print('No matches')
        else:
            self.changeTitle()

    def changeTitle(self):
        title=self.getTitle()
        self.note['title']=title
        print('Note title changed')
        saveNotes(self.notes)

    def getTitle(self):
        title=''
        while not title.strip():
            title=input('Insert new note title: ')
        return title
