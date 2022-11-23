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
cmdcheatsheet configuration folder is located at `~/.config/cmdcheatsheet`.\
The config is called `config.json`

#### Available configurations
* `commandsStoreLocation` - Path to file in JSON format that consists of the command list.
* `alternativeStoreLocations` - Path list to JSON files that might be used as an alternative commands store location.
Every item in the list has a `storeName` property, which is just a store name and the second property is `storeLocation`, responsible for the path to the commands store (JSON file location).

Here is a `config.json` example:
```json
{
    "commandsStoreLocation": "/Users/myusername/.config/cmdcheatsheet/commands.json",
    "alternativeStoreLocations": [
        {
            "storeName": "unix",
            "storeLocation": "/Users/myusername/my-configs/cmdcheatsheet/unix_commands.json"
        },
        {
            "storeName": "windows",
            "storeLocation": "/Users/myusername/my-configs/cmdcheatsheet/windows_commands.json"
        }
    ]
}
```

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

# Alternative commands stores
It's possible to have multiple command stores and switch between them.
In this way, you'll be able to have separate configs for windows, Linux, and OSX, or in case you want to split the config in some other way.
This feature is called alternative command stores. 

### Add alternative commands store
```bash
cmdcheatsheet -aas <store_name> <store_location>
```

### Update alternative commands store 
```bash
cmdcheatsheet -uas <store_name> <store_location>
```

### Delete alternative commands store
```bash
cmdcheatsheet -das <store_name>
```

### Display alternative commands store details
```bash
cmdcheatsheet -dasd
```

### Switch to alternative commands store
```bash
cmdcheatsheet -stas <store_name>
```

### Display applied alternative store
```bash
cmdcheatsheet -daasn
```
