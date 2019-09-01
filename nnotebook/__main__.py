from sys import argv
from .files import changeDir
from . import actions

def getOption():
    for i in range(1,len(argv)):
        if argv[i] in actions.actions:
            getattr(actions,argv[i].title())(argv[1:i]+argv[i+1:])
            return True

def main():
    try:
        changeDir()
        if not getOption():
            actions.Display([])
    except KeyboardInterrupt:
        print('\nAction cancelled')

if __name__=='__main__':
    main()
