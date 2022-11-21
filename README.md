# cmdcheatsheet
A package that allows storing terminal commands.

### Help command
```bash
cmdcheatsheet -h
```
or:
```bash
cmdcheatsheet --help
```

### Add command
```bash
cmdcheatsheet -a <command> <command_description>
```
for example:
```bash
cmdcheatsheet -a "ls" "list directory content"
```

### Display command

Display all commands:
```bash
cmdcheatsheet -p
```
or:
```bash
cmdcheatsheet
```
Display commands along with ids:
```
cmdcheatsheet -i
```
Display commands using table view:
```bash
cmdcheatsheet -t
```

### Search for a command: 
```bash
cmdcheatsheet -f <command>
```
Search for a command and show it along with an id:
```bash
cmdcheatsheet -fi <command>
```
Search for a command and show it using the table view:
```bash
cmdcheatsheet -ft <command>
```

### Update command
```bash
cmdcheatsheet -u <command_id> <command> <command_description>
```

### Remove command
```bash
cmdcheatsheet -d <command_id>
```

### Show all command names
```bash
cmdcheatsheet -nl
```
