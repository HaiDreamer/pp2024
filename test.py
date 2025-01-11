import subprocess
import os
import shlex

def execute_command(command):
    """
    Executes a command with optional I/O redirection and piping.
    """
    try:
        # Split the command into parts
        parts = shlex.split(command)

        # Handle pipelines
        if '|' in parts:
            commands = command.split('|')
            processes = []
            prev_process = None

            for cmd in commands:
                cmd_parts = shlex.split(cmd.strip())
                if prev_process is None:
                    process = subprocess.Popen(cmd_parts, stdout=subprocess.PIPE)
                else:
                    process = subprocess.Popen(cmd_parts, stdin=prev_process.stdout, stdout=subprocess.PIPE)

                processes.append(process)
                prev_process = process

            # Capture the output of the final process
            output, _ = processes[-1].communicate()
            print(output.decode())

        # Handle I/O redirection
        elif '>' in parts or '>>' in parts or '<' in parts:
            if '>' in parts:
                redirect_index = parts.index('>')
                mode = 'w'
            elif '>>' in parts:
                redirect_index = parts.index('>>')
                mode = 'a'
            elif '<' in parts:
                redirect_index = parts.index('<')
                mode = 'r'

            cmd_parts = parts[:redirect_index]
            file_name = parts[redirect_index + 1]

            if mode in ['w', 'a']:  # Output redirection
                with open(file_name, mode) as f:
                    subprocess.run(cmd_parts, stdout=f)
            elif mode == 'r':  # Input redirection
                with open(file_name, 'r') as f:
                    subprocess.run(cmd_parts, stdin=f)

        # Execute a simple command
        else:
            subprocess.run(parts)

    except Exception as e:
        print(f"Error: {e}")


def shell():
    """
    Main loop for the custom shell.
    """
    print("Custom Shell: Type 'exit' to quit.")
    while True:
        try:
            command = input(">> ").strip()
            if command.lower() == 'exit':
                break
            if command:
                execute_command(command)
        except KeyboardInterrupt:
            print("\nType 'exit' to quit.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    shell()
