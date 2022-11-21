from cmdcheatsheet.logger import help_details


def help(command_list):
    for c in command_list:
        commands_to_help = []
        
        for responsible_command in c.responsible_commands:
            command_arguments = [f'<{a.name}{":optional" if not a.required else ""}>' for a in c.command_arguments]
            arguments = (' '  + ' '.join(command_arguments)) if command_arguments else ''
            commands_to_help.append(f'cmd {responsible_command}{arguments}')

        help_details(', '.join(commands_to_help), c.description)

