```
                    _      _                _       _               _
  ___ _ __ ___   __| | ___| |__   ___  __ _| |_ ___| |__   ___  ___| |_
 / __| '_ ` _ \ / _` |/ __| '_ \ / _ \/ _` | __/ __| '_ \ / _ \/ _ \ __|
| (__| | | | | | (_| | (__| | | |  __/ (_| | |_\__ \ | | |  __/  __/ |_
 \___|_| |_| |_|\__,_|\___|_| |_|\___|\__,_|\__|___/_| |_|\___|\___|\__|

```

###### `cmdcheatsheet` is a package that allows storing terminal commands.

---

#### Help command
```bash
cmdcheatsheet -h
```
or:
```bash
cmdcheatsheet --help
```

#### Add command
```bash
cmdcheatsheet -a <command> <command_description>
```
for example:
```bash
cmdcheatsheet -a "ls" "list directory content"
```

#### Display commands

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

#### Search for a command
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

#### Update command
```bash
cmdcheatsheet -u <command_id> <command> <command_description>
```

#### Remove command
```bash
cmdcheatsheet -d <command_id>
```

#### Show all command names
```bash
cmdcheatsheet -nl
```

# Configuration
cmdcheatsheet configuration folder is located at `~/.config/cmdcheatsheet`.

#### Available configurations
* `commandsStoreLocation` - Path to file in JSON format that consists of the command list.

#### Display configuration
```bash
cmdcheatsheet -dc
```
or display configuration by key:
```bash
cmdcheatsheet -dc <config_key>
```

#### Display available configurations
This command displays all available configurations. Each command consists of a key and an explanation.
```bash
cmdcheatsheet -dac
```

#### Set configuration
```bash
cmdcheatsheet -sc <configuration_key> <configuration_value>
```

#### Remove configuration by key
```bash
cmdcheatsheet -rc <configuration_key>
```

#### Set configuration to default
```bash
cmdcheatsheet -sctd
```

#### Set a single config value
```bash
cmdcheatsheet -ssctd <configuration_key>
```
