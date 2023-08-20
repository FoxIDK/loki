# Imports.
import sys
import os
import subprocess
from colorama import Fore
import json

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
print_red_command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: {Fore.RED}¤{Fore.WHITE} ") # Always asks for a command on a new line.

# Program.
def vault():
        try:
            os.chdir(os.path.expanduser("~"))
            with open(".config/loki_config.json") as f:
                loki_config = json.load(f)
                install_dir = loki_config["loki_dir"]
                vault_dir = loki_config["vault_location"]

            print(f"\n{print_alert} VCP: Vault Control Panel {print_alert}")
            print(f"\n{print_prompt} VAULTING MAY RISK DATA | READ DOCUMENTATION")
            option = input(f"{print_red_command}").lower()

            if option == "open":
                subprocess.run(['cp', f"{install_dir}/src/modules/decryptor.py", vault_dir])
                subprocess.run(['cp', f"{install_dir}/var/pipes/loki.key", vault_dir])
                os.chdir(os.path.expanduser(vault_dir))
                subprocess.run(['python3', "decryptor.py"])
                os.remove("decryptor.py")
                os.remove("loki.key")
                print(f"\n{print_exited} {print_notice} {print_successfully}\n")

            elif option == "close":
                subprocess.run(['cp', f"{install_dir}/src/modules/encryptor.py", vault_dir])
                subprocess.run(['cp', f"{install_dir}/var/pipes/loki.key", vault_dir])
                os.chdir(os.path.expanduser(vault_dir))
                subprocess.run(['python3', "encryptor.py"])
                os.remove("encryptor.py")
                os.remove("loki.key")
                print(f"\n{print_exited} {print_notice} {print_successfully}\n")

            elif option == "import":
                os.chdir(os.path.expanduser("~"))
                print(f"\n{print_alert} Importing will open the vault.")
                subprocess.run(['cp', f"{install_dir}/src/modules/decryptor.py", vault_dir])
                subprocess.run(['cp', f"{install_dir}/var/pipes/loki.key", vault_dir])
                os.chdir(os.path.expanduser(vault_dir))
                subprocess.run(['python3', "decryptor.py"])
                os.remove("decryptor.py")
                os.remove("loki.key")
                import_file = input(f"\n{print_question} Full Dir of the file: ")
                subprocess.run(['mv', import_file, vault_dir])
                print(f"\n{print_alert} File has been imported, closing the vault now.")
                os.chdir(os.path.expanduser(vault_dir))
                subprocess.run(['cp', f"{install_dir}/src/modules/encryptor.py", vault_dir])
                subprocess.run(['cp', f"{install_dir}/var/pipes/loki.key", vault_dir])
                subprocess.run(['python3', "encryptor.py"])
                os.remove("encryptor.py")
                os.remove("loki.key")
                print(f"\n{print_exited} {print_notice} {print_successfully}\n")

# Error handling.
        except KeyboardInterrupt:
            print(f"\n{print_exited} {print_notice} {print_successfully}\n")
            print(f'{print_notice} You interrupted the program.\n')
            try:
                os._exit(0); sys.exit(0)
            except SystemExit:
                os._exit(1); sys.exit(1)
        except ValueError:
            print(f"\n{print_exited} {print_notice} {print_successfully}")
            print(f'\n{print_notice} You entered invalid data into a field.\n')
            try:
                os._exit(0); sys.exit(0)
            except SystemExit:
                os._exit(1); sys.exit(1)
        except FileNotFoundError as not_found:
            print("This file is missing:" + not_found.filename)