from tempfile import NamedTemporaryFile
from os import environ
from datetime import datetime
import subprocess

from ._helpers import noteAction,NoteGetter,checkNotebook
from ..files import loadNotes,saveNotes,modDateFormat

@noteAction
class Write:
    def __init__(self,settings):
        self.notes,self.settings=loadNotes(),settings
        nb=checkNotebook(settings)
        self.note=NoteGetter(self.notes,self.settings,nb).getNote()
        self.checkAndChangeNote()

    def checkAndChangeNote(self):
        if self.note is not None:
            self.changeNote()
            saveNotes(self.notes)
            print('Changed note "%s"'%self.note['title'])

    def changeNote(self):
        with NamedTemporaryFile() as file:
            file.write(bytes(self.note['content'],'utf-8'))
            file.seek(0)
            self.openAndEditFile(file.name)
            newContent=file.read().decode()
        self.setNewContent(newContent)

    def openAndEditFile(self,path):
        DEFAULT_EDITOR='/usr/bin/vi'
        editor=environ.get('EDITOR',DEFAULT_EDITOR)
        subprocess.run(' '.join((editor,path)),shell=True)

    def setNewContent(self,newContent):
        if newContent.endswith('\n'):
            newContent=newContent[:-1]
        self.note['content']=newContent
        self.note['modDate']=datetime.now().strftime(modDateFormat)
