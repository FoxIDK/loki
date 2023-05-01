# Imports.
import os
import sys
import time
import json
from colorama import Fore
from pathlib import Path
from cryptography.fernet import Fernet

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Config (Prints).
print_text = (f"{Fore.WHITE}") # Change the colour of text output in the client side prints.
print_dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side prints.
print_success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]") # Success output.
print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]") # Failed output.
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]") # Prompt output.
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]") # Notice output.
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]") # Alert output.
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]") # Alert output.
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]") # Execited output.
print_disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]") # Disconnected output.
print_command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ") # Always asks for a command on a new line.

def config():
    confirmation = input(f"\n{print_alert} Do you want to continue, this will overwrite previous config [y/n]: ")
    if confirmation == "y" or confirmation == "Y":
        os.chdir(os.path.expanduser("~"))
        # Requests full path for configuration file.
        install_dir = input(f"\n{print_question} Loki directory (Example: ~/loki): ")
        vault_dir = input(f"\n{print_question} Full vault path (Local): ")
        # Don't touch this, it works for some reason.
        loki_config = {
            "config_check": "updated",
            "loki_dir": install_dir,
            "vault_location": vault_dir,
        }
        with open("loki_config.json", "w") as outfile:
            json.dump(loki_config, outfile, indent=1)
        # Checks for update valid.
        with open(f'loki_config.json') as f:
            data = json.load(f)
            update_verify = ("config_check")
            if update_verify in data:
                print(f"\n{print_notice} Config have been", loki_config[update_verify], f"{print_successfully}!")
            else:
                print(f"\n{print_alert} Config has {print_failed}!.")
        # Asks if they have an initial key.
        os.system(f"mv ./loki_config.json ~/.config/loki_config.json")
        req_initial = input(f"\n{print_question} Do you need an initial key? [y/n]: ")
        if req_initial == "y".lower():
            initial_key = "loki.key"
            # Generate new key
            with open(initial_key, 'wb') as loki_key:
                key = Fernet.generate_key()
                loki_key.write(key)
                print(f'\n{print_alert} Initial key: {key.decode("utf8")}\n')
                print(f"{print_prompt} It will be stored in {install_dir} for later use, this is your first key!\n")
                os.system(f"mv ./loki.key {install_dir}/var/pipes/loki.key")
        if req_initial == "n".lower():
            print(f"\n{print_notice} Quitting program for safety reasons.")
    # Simply quits if not wanting to update.
    if confirmation == "n" or confirmation == "N":
        print(f"\n{print_notice} Quitting program for safety reasons.")
# Run apicon.
if __name__ == '__main__':
    config()