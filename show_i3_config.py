#!/usr/bin/env python3

import subprocess
import os

def get_i3_shortcuts():
    config_path = os.path.expanduser('~/.config/i3/config')
    with open(config_path, 'r') as file:
        lines = file.readlines()
    
    # Extract shortcuts (bindsym) and format them
    shortcuts = []
    for line in lines:
        if line.startswith('bindsym'):
            parts = line.split()
            # Reconstruct the command without 'bindsym' and 'exec'
            shortcut = f"{parts[1]} {' '.join(parts[2:])}"
            shortcuts.append(shortcut)
    return shortcuts

def show_info(info):
    rofi_command = ['rofi', '-dmenu', '-i', '-p', 'i3 Shortcuts', '-theme', '~/.config/rofi/rofidmenu.rasi']
    result = subprocess.run(rofi_command, input='\n'.join(info), stdout=subprocess.PIPE, text=True)
    selected_info = result.stdout.strip()
    return selected_info

def main():
    shortcuts = get_i3_shortcuts()
    if not shortcuts:
        print("No shortcuts found in i3 config")
        return

    show_info(shortcuts)

if __name__ == "__main__":
    main()
