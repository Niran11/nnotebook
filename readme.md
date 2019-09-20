# Nnotebook
notebook written in python
## Install:

`python setup.py install`

if `--user is used` then add `~/.local/bin/` to your $PATH variable:
`$PATH=${PATH}:${HOME}/.local/bin/`

## Usage:

`note create title` - creates note

`note add id/title text` - add text to note, if no id/title is provided then creates new note

`note delete id/title` - removes note

`note display` or `note` - displays all notes in format `id. notebook/title (modification date)`

`note id/title` - displays note with given id/title

`note display id/title` - display note with given id/title

`note title id` - change title of note

`note write id/title` - opens vi or editor set in $EDITOR variable and lets you edit it, save and exit to save changes

You may add `nb:name` (where `name` is name of notebook) to search note in given notebook when catching note by title

Adding `nb:name` to display outputs list of notes in given notebook if no title of note to display is provided/found
