actions=[]

def noteAction(cl):
    actions.append(cl.__name__.lower())
    return cl

class NoteGetter:
    def __init__(self,notes,settings):
        self.notes,self.settings=notes,settings

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
            if n['title'].lower()==title:
                return n

    def verifyNote(self,note):
        if note is not None and 'end' not in note:
            return note
        elif self.settings!=[]:
            print('No matches')
