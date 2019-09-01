actions=[]
notebookOption='nb:'

def noteAction(cl):
    actions.append(cl.__name__.lower())
    return cl

def checkNotebook(settings):
    for i in range(len(settings)):
        if settings[i].startswith(notebookOption):
            notebook=settings[i][len(notebookOption):]
            del settings[i]
            return notebook

class NoteGetter:
    def __init__(self,notes,settings,notebook=None,warn=False):
        self.notes,self.settings,self.notebook,self.warn=(notes,
                                                          settings,
                                                          notebook,
                                                          warn)

    def getNote(self):
        try:
            note,settingsPosition=self.getNoteById()
            del self.settings[settingsPosition]
        except (ValueError,IndexError):
            note=self.getNoteByTitle()
        return self.verifyNote(note)

    def getNoteById(self):
        id,i=self.getNoteId()
        if id is None:raise ValueError()
        return self.notes[id],i

    def getNoteId(self):
        for i in range(len(self.settings)):
            try:
                return self.checkPositionForId(i)
            except ValueError:
                pass
        return None,None

    def checkPositionForId(self,i):
        id=int(self.settings[i])-1
        if id<0:raise ValueError()
        return id,i

    def getNoteByTitle(self):
        title=' '.join(self.settings).lower()
        for n in self.notes:
            if (n['title'].lower()==title
                    and (not self.notebook
                         or n['notebook']==self.notebook)):
                return n

    def verifyNote(self,note):
        if note is not None and 'end' not in note:
            return note
        elif not self.warn:
            print('No matches')
