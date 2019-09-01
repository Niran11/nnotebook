from datetime import datetime

from ._helpers import noteAction,NoteGetter
from ..files import loadNotes,saveNotes,modDateFormat

@noteAction
class Title:
    def __init__(self,settings):
        self.notes,self.settings=loadNotes(),settings
        self.getNoteAndChangeTitle()

    def getNoteAndChangeTitle(self):
        try:
            self.note,position=NoteGetter(self.notes,self.settings)\
                                    .getNoteById()
            del self.settings[position]
        except (ValueError,IndexError):
            print('No matches')
        else:
            self.changeTitle()

    def changeTitle(self):
        title=self.getTitle()
        self.note['title']=title
        self.note['modDate']=datetime.now().strftime(modDateFormat)
        print('Note title changed')
        saveNotes(self.notes)

    def getTitle(self):
        title=' '.join(self.settings)
        while not title.strip():
            title=input('Insert new note title: ')
        return title
