#!/usr/bin/env python3

import subprocess

def get_avds():
    result = subprocess.run(['~/Android/Sdk/emulator/emulator', '-list-avds'], stdout=subprocess.PIPE, text=True, shell=True)
    avds = result.stdout.splitlines()
    return avds

def select_avd(avds):
    print("avds")
    print(avds)
    rofi_command = ['rofi', '-dmenu', '-i', '-p', 'Select AVD', '-theme', '~/.config/rofi/rofidmenu.rasi']
    result = subprocess.run(rofi_command, input='\n'.join(avds), stdout=subprocess.PIPE, text=True)
    selected_avd = result.stdout.strip()
    return selected_avd

def launch_avd(avd):
    print(avd)
    subprocess.run(['~/Android/Sdk/emulator/emulator', '-avd', avd], shell=True)

def main():
    avds = get_avds()
    if not avds:
        print("No AVDs found")
        return

    selected_avd = select_avd(avds)
    if selected_avd:
        launch_avd(selected_avd)

if __name__ == "__main__":
    main()
