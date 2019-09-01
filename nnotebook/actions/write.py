from tempfile import NamedTemporaryFile
from os import environ
import subprocess

from ._helpers import noteAction,NoteGetter
from ..files import loadNotes,saveNotes


@noteAction
class Write:
    def __init__(self,settings):
        self.notes,self.settings=loadNotes(),settings
        self.note=NoteGetter(self.notes,self.settings).getNote()
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

    def setNewContent(self,newContent):
        if newContent.endswith('\n'):
            newContent=newContent[:-1]
        self.note['content']=newContent

    def openAndEditFile(self,path):
        DEFAULT_EDITOR='/usr/bin/vi'
        editor=environ.get('EDITOR',DEFAULT_EDITOR)
        subprocess.run(' '.join((editor,path)),shell=True)
