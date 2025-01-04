# Linux Commandline Editors

## vi

### vi Shortcut

```text
:xReturn quit vi, writing out modified file to file named in original invocation
:wqReturn quit vi, writing out modified file to file named in original invocation
:qReturn quit (or exit) vi
:q!Return quit vi even though latest changes have not been saved for this vi call

↓ move cursor down one line
↑ move cursor up one line
← move cursor left one character
→ move cursor right one character

u undo whatever you just did; a simple toggle
. redo whatever you just did

i insert text before cursor, until Esc hit
I insert text at beginning of current line, until Esc hit
a append text after cursor, until Esc hit
A append text to end of current line, until Esc hit
o open and put text in a new line below current line, until Esc hit
O open and put text in a new line above current line, until Esc hit
r replace single character under cursor (no Esc needed)
cw change the current word with new text,starting with the character under cursor, until Esc hit
x delete single character under cursor
Nx delete N characters, starting with character under cursor
dw delete the single word beginning with character under cursor
C change (replace) the characters in the current line, until Esc hit
D delete the remainder of the line, starting with current cursor position

dd delete entire current line
Ndd delete N lines, beginning with the current line; e.g., 5dd deletes 5 lines
yy copy (yank, cut) the current line into the buffer
Nyy copy (yank, cut) the next N lines, including the current line, into the buffer
p paste the line(s) in the buffer into the text after the current line

0 (zero) move cursor to start of current line (the one with the cursor)
$ move cursor to end of current line
w move cursor to beginning of next word
b move cursor back to beginning of preceding word
:0Return or 1G move cursor to first line in file
:nReturn or nG move cursor to line n
:$Return or G move cursor to last line in file

/string search forward for occurrence of string in text
?string search backward for occurrence of string in text
n move to next occurrence of search string
N move to next occurrence of search string in opposite directio

```
### vi To Set Arrow Keys in Edit Mode
```bash
vi ~/.exrc
set nocompatible
```

### vi TODO Read Shortcut

* https://askubuntu.com/questions/353911/hitting-arrow-keys-adds-characters-in-vi-editor
* https://www.cs.colostate.edu/helpdocs/vi.html


## nano

### nano Shortcut
