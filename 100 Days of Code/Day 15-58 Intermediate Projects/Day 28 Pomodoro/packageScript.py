import os
import subprocess

def package_program():
    # Define the files to include
    additional_files = [
        ('tomato.png', '.'),  # Copy tomato.png to the root of the distribution
        ('shortBreak.mp3', '.'),  # Copy shortBreak.mp3 to the root
        ('longBreak.mp3', '.')  # Copy longBreak.mp3 to the root
    ]

    # Create the PyInstaller command
    command = ['pyinstaller', '--onefile', '--windowed', 'pomodoro.py']

    # Add data files
    for file, destination in additional_files:
        command.extend(['--add-data', f'{file}{os.pathsep}{destination}'])

    # Run the command
    subprocess.run(command)

if __name__ == '__main__':
    package_program()
