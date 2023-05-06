# Imports.
import sys
import os
from colorama import Fore

# Modules.
import src.modules.encrypt as encrypt
import src.modules.decrypt as decrypt
import src.modules.keygen as keygen
import src.modules.vault as vault
import src.config as config

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
def main_script():
        try:
            owd = os.getcwd() # Gets source dir.
            os.chdir(owd) # Changes back to source dir.
            print(f"\n    -=-=-=-=-COMMANDS-=-=-=-=-\n")
            print(f"{print_prompt}  {Fore.GREEN}•{Fore.WHITE} Encrypt       {Fore.WHITE}(Secure)")
            print(f"{print_prompt}  {Fore.GREEN}•{Fore.WHITE} Decrypt       {Fore.WHITE}(Decrypt)")
            print(f"{print_prompt}  {Fore.YELLOW}•{Fore.WHITE} Vault         {Fore.WHITE}(Access vault)")
            print(f"{print_prompt}  {Fore.GREEN}•{Fore.WHITE} Keygen        {Fore.WHITE}(New key)")
            print(f"{print_prompt}  {Fore.GREEN}•{Fore.WHITE} Config        {Fore.WHITE}(Config)")
            option = input(f"{print_command}")

            if option == "encrypt".lower(): # Runs the encrypt program.
                encrypt.encrypt() 
                os._exit(0)

            if option == "decrypt".lower(): # Runs the decrypt program.
                decrypt.decrypt() 
                os._exit(0)

            if option == "keygen".lower(): # Runs the keygen program.
                keygen.keygen() 
                os._exit(0)

            if option == "vault".lower(): # Runs the keygen program.
                vault.vault() 
                os._exit(0)

            if option == "config".lower(): # Runs the keygen program.
                config.config() 
                os._exit(0)

        except KeyboardInterrupt:
            print(f"\n{print_exited} {print_notice} {print_successfully}")
            print(f'\n{print_notice} You interrupted the program.\n')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except FileNotFoundError as not_found:
            print("This file is missing:" + not_found.filename)