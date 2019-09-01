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

`note display` or `note` - all notes
`note display id/title` - display note with given id/title

`note title id` - change title of note

`note write id/title` - opens vi or editor set in $EDITOR variable and lets you edit it, save and exit to save changes
