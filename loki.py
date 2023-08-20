# Imports.
import sys
import os
import subprocess
from colorama import Fore
import argparse

# Modules.
import src.modules.encrypt as encrypt
import src.modules.decrypt as decrypt
import src.modules.vault as vault
import src.modules.keygen as keygen
import src.config as config
import etc.init.banner as banner

# Pre-run.
subprocess.run("clear")
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

# Dummy threading.
from multiprocessing.dummy import Pool as ThreadPool
# Makes the little workers!
threads = ThreadPool(8)

# Benchmark, remember to uncomment in `if __name__ == '__main__':` at the end.
#from time import perf_counter
#start = perf_counter()

# Arg parser.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('-encrypt', help='Encrypt specified directory.',    action="store_true")
ap.add_argument('-decrypt', help='Decrypt specified directory.',    action="store_true")
ap.add_argument('-vault',   help='Access the Vault Control Panel.', action="store_true")
ap.add_argument('-keygen',  help='Generate a key.',                 action="store_true")
ap.add_argument('-recovery',help='Recovery system, in-dev.',        action="store_true")
ap.add_argument('-config',  help='Configure Loki.',                 action="store_true")
args = vars(parser.parse_args())

# Args.
if args['encrypt']: # Runs the encrypt program.
    while True:
        try:
            os.chdir(os.path.expanduser("~"))
            encrypt.encrypt()
            os._exit(0); sys.exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Encrypt failed to run here!\n")
            os._exit(0); sys.exit(0)

if args['decrypt']: # Runs the decrypt program.
    while True:
        try:
            os.chdir(os.path.expanduser("~"))
            decrypt.decrypt()
            os._exit(0); sys.exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Decrypt failed to run here!\n")
            os._exit(0); sys.exit(0)

if args['vault']: # Runs the keygen program.
    while True:
        try:
            os.chdir(os.path.expanduser("~"))
            vault.vault() 
            os._exit(0); sys.exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Vault failed to run here!\n")
            os._exit(0); sys.exit(0)

if args['keygen']: # Runs the keygen program.
    while True:
        try:
            os.chdir(os.path.expanduser("~"))
            keygen.keygen()
            os._exit(0); sys.exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Keygen failed to run here!\n")
            os._exit(0); sys.exit(0)

if args['config']: # Runs the keygen program.
    while True:
        try:
            os.chdir(os.path.expanduser("~"))
            config.config()
            os._exit(0); sys.exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Config failed to run here!\n")
            os._exit(0); sys.exit(0)

# Program.
if __name__ == '__main__':
    try:
        #banner.banner() # Shows the banner.
        threads.close()
        threads.join()
#        end = perf_counter()
#        print(f"Time: {end - start} seconds")
        main.main_script() # Runs the primary program.
    except KeyboardInterrupt:
        print(f"\n{print_exited} {print_notice} {print_successfully}\n")
        print(f'{print_notice} You interrupted the program.\n')
        try:
            os._exit(0); sys.exit(0)
        except SystemExit:
            os._exit(1); sys.exit(1)
    except FileNotFoundError as not_found:
        print("This file is missing:" + not_found.filename)