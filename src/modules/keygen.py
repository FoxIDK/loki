# Imports.
import sys
import os
import subprocess
from colorama import Fore
from cryptography.fernet import Fernet
import json
from datetime import datetime

# Pre-run.
subprocess.run("clear", shell=True)
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

# Program.
def keygen():
    try:
        os.chdir(os.path.expanduser("~"))
        with open(".config/loki_config.json") as f:
            loki_config = json.load(f)
            install_dir = loki_config["loki_dir"]

        os.chdir(os.path.expanduser("~"))
        print(f"\n{print_question} Do you want to back up your current key? [Y/n]: ")
        option = input(f"{print_command}")
        option = option.lower()

        # Backup key
        current_datetime = datetime.now()
        dt = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
        if option == 'y':
            os.chdir(os.path.expanduser("~"))
            with open("loki/var/pipes/loki.key",'r') as loki_key:
                print(f"\n{print_prompt} Previous key: {loki_key.read()}")
                subprocess.run(['cp', f"{install_dir}/var/pipes/loki.key", f"{install_dir}/var/pipes/recovery/loki_{dt}.key"])

            gen_key = "loki.key"
            # Generate new key
            with open(gen_key, 'wb') as loki_key:
                key = Fernet.generate_key()
                loki_key.write(key)
                print(f'\n{print_alert} New key: {key.decode("utf8")}\n')
                subprocess.run(['mv', './loki.key', f"{install_dir}/var/pipes/loki.key"])

        if option == 'n':
            print(f'\n{print_exited} {print_notice} {print_successfully}\n')

# Error handling.
    except KeyboardInterrupt:
        print(f"\n{print_exited} {print_notice} {print_successfully}")
        print(f'{print_notice} You interrupted the program.\n')
        try:
            os._exit(0); sys.exit(0)
        except SystemExit:
            os._exit(0); sys.exit(0)
    except ValueError:
        print(f"\n{print_exited} {print_notice} {print_successfully}")
        print(f'{print_notice} You entered invalid data into a field.\n')
        try:
            os._exit(0); sys.exit(0)
        except SystemExit:
            os._exit(0); sys.exit(0)