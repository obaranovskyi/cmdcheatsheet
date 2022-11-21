# cmd-cheatsheet
A package that allows storing terminal commands.

### Help command
```bash
cmd-cheatsheet -h
```
or:
```bash
cmd-cheatsheet --help
```

### Add command
```bash
cmd-cheatsheet -a <command> <command_description>
```
for example:
```bash
cmd-cheatsheet -a "ls" "list directory content"
```

### Display command

Display all commands:
```bash
cmd-cheatsheet -p
```
or:
```bash
cmd-cheatsheet
```
Display commands along with ids:
```
cmd-cheatsheet -i
```
Display commands using table view:
```bash
cmd-cheatsheet -t
```

### Search for a command: 
```bash
cmd-cheatsheet -f <command>
```
Search for a command and show it along with an id:
```bash
cmd-cheatsheet -fi <command>
```
Search for a command and show it using the table view:
```bash
cmd-cheatsheet -ft <command>
```

### Update command
```bash
cmd-cheatsheet -u <command_id> <command> <command_description>
```

### Remove command
```bash
cmd-cheatsheet -d <command_id>
```

### Show all command names
```bash
cmd-cheatsheet -nl
```
