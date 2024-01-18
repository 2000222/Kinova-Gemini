impimport yaml

def move_legs(command):
    if command not in ['move_forward', 'move_backward', 'turn_left', 'turn_right']:
        raise ValueError(f'Invalid command: {command}')

    if command == "move_forward":
        print("Moving legs forward")
    elif command == "move_backward":
        print("Moving legs backward")
    elif command == "turn_left":
        print("Turning left")
    elif command == "turn_right":
        print("Turning right")

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
    commands = load_commands('legs.yaml')  # The filename should be specific to leg commands
    for command in commands:
        move_legs(command)
except (FileNotFoundError, yaml.YAMLError) as e:
    print(f"Failed to load commands: {e}")
except (ValueError, TypeError) as e:
    print(f"Failed to execute commands
    : {e}")
