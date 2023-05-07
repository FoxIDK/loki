# Imports.
import sys
import json
import os
import time
from colorama import Fore

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

# Program.
def decrypt():
        try:
            os.chdir(os.path.expanduser("~"))
            # Loki Config.
            with open('.config/loki_config.json') as f:
                loki_config = json.load(f)
                install_dir = loki_config["loki_dir"]

            print(f"\n{print_question} What directory would you like to decrypt?\n")
            dir_decrypt = input(f"{print_command}")
            dir_notice = dir_decrypt
            print(f"\n{print_alert} Decrypting: {dir_notice} | You have 5s to cancel. (ctrl+c)")
            time.sleep(4)
            os.system(f"\ncp {install_dir}/src/modules/decryptor.py {dir_decrypt}")
            os.system(f"cp {install_dir}/var/pipes/loki.key {dir_decrypt}")
            os.chdir(os.path.expanduser(f"{dir_decrypt}"))
            os.system(f"cd {dir_decrypt}")
            os.system(f"python3 {dir_decrypt}/decryptor.py")
            os.system("rm decryptor.py")
            os.system("rm loki.key")
            print(f"\n{print_exited} {print_notice} {print_successfully}\n")

# Error handling.
        except KeyboardInterrupt:
            print(f"\n{print_exited} {print_notice} {print_successfully}\n")
            print(f'{print_notice} You interrupted the program.\n')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except ValueError:
            print(f"\n{print_exited} {print_notice} {print_successfully}\n")
            print(f'{print_notice} You entered invalid data into a field.\n')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)