from ._helpers import noteAction,NoteGetter,checkNotebook
from ..files import loadNotes,saveNotes

@noteAction
class Delete:
    def __init__(self,settings):
        self.notes,notebook=loadNotes(),checkNotebook(settings)
        self.note=NoteGetter(self.notes,settings,notebook).getNote()
        self.checkAndDeleteNote()

    def checkAndDeleteNote(self):
        if self.note is not None:
            self.confirmAndDelete()

    def confirmAndDelete(self):
        confirm=None
        while confirm not in ['y','yes','n','no']:
            confirm=input('Delete note "%s"? (yes/no) '%self.note['title'])
        if confirm in ['y','yes']:
            self.deleteNote()
        else:
            print('Note not deleted')

    def deleteNote(self):
        self.note['end']=True
        saveNotes(self.notes)
        print('Deleted note %s'%self.note['title'])
