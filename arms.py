import yaml

def move_arms(command):
    if command not in ['move_left', 'move_right']:
        raise ValueError(f'Invalid command: {command}')

    if command == "move_left":
        print("Moving arms to the left")
    elif command == "move_right":
        print("Moving arms to the right")

def load_commands(filepath):
    with open(filepath) as file:
        commands = yaml.safe_load(file)

    if not isinstance(commands, list):
        raise TypeError('Commands must be a list')

    for command in commands:
        if not isinstance(command, str):
            raise TypeError(f'All commands must be strings, found {type(command).__name__} instead')

    return commands

try:
    commands = load_commands('brain.yaml')
    for command in commands:
        move_arms(command)
except (FileNotFoundError, yaml.YAMLError) as e:
    print(f"Failed to load commands: {e}")
except (ValueError, TypeError) as e:
    print(f"Failed to execute commands
    : {e}")
