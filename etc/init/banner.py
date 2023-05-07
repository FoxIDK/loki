# Imports.
import sys
import os
from colorama import Fore
import random

# Program.
version = ("3.9.12") # Major.Minor.Rev/Build
motd = (f"{Fore.YELLOW}The god of mischief{Fore.WHITE}") # Always use 20 char max.
tag = ['              (Did you know, Loki can be used for host-defensive?)', '              (Loki is the world eaters father Pagan and Norse folklore!)'] # Use spaces to centre the tag to the divider bar.

def banner():
    try:
        print("\n            :~77::                                             ::77~     ")
        print("          :5#@@5G&5^                                         ~P&5P@@#J:  ")
        print("          B@@@@JG@@@Y                                      ^5@@@5Y@@@@P  ")
        print("         ^&@@@@5:J#@@#!                                   7&@@B? G@@@@#  ")
        print("         :&@@@@#:  !G@@Y                                 5@@P!  ^&@@@@#  ")
        print("          B@@@@@J    ~5@G:                             ^B&Y^    5@@@@@P  ")
        print("          J@@@@@&^     ^5G^                           ~BY:     ~&@@@@@!  ")
        print("          ^&@@@@@G       ~?                           ?^       B@@@@@B   ")
        print("           J@@@@@@Y                                           P@@@@@@~   ")
        print("            B@@@@@@7                                         J@@@@@@Y    ")
        print("            ~@@@@@@&~                                       7@@@@@@P     ")
        print("             ?@@@@@@#^                                     ~&@@@@@G:     ")
        print("              5@@@@@@B:                                   ^&@@@@@&^      ")
        print("               P@@@@@@B:                                 ^#@@@@@@J       ")
        print("               :G@@@@B&G     :  ::            ::: ::    ^#&B@@@@P        ")
        print("                :B@@@&J#G ^Y5JJYYY^~PB#####B5^~5JYJJYY::#GY&@@@P         ")
        print("                 :B@@@&7GG~7!B@?G& 5@@@@@@@@@J:@5Y@G~7~B5?&@@@P          ")
        print("                  :G@@@&75P:P5YP5P:!@@@@@@@@&^^PYPY55:BY?@@@@5           ")
        print("                    P@@@@7JP!&&PY?~ ?@@@@@@&7 !?YP&#!G?J@@@@Y            ")
        print("                     Y@@@@??57&@@B5! ^P&@#5: 75B@@#7P7Y@@@@?             ")
        print("                     !?@@@@Y!Y!#@@@&GYJ5G5J5B@@@@G~Y!5@@@&7!             ")
        print("                     Y~~&@@@5~! J#@@@@@@@@@@@@@#? 7~P@@@#^7?             ")
        print("                     ~#?~G@@@P~: 7Y#@@@@@@@@@BJ7 :~B@@@P^JB:             ")
        print("                      Y@B??5B&P  ?GJYB&&&&&BJJG! :G&G5?J#@?              ")
        print("                     7J5@@&BGP5!7JJ@#!!GGG^?#@?Y!75PGB&@@YY!             ")
        print("                     !@5?P&@@@&@@@YJ@&7B@P7@@?5@@&@@@@&P?G@^             ")
        print("                      G@? !J5PP5P#@55@#~~!&@YP@BP5PP5?~ 5@Y              ")
        print("                      ^#!7B5??Y5J!!J^5@P B@J~J!!J5Y??PB~?G:              ")
        print("                       7YJ@#~ :^7J7~  !~ !!  ~7?7^  !#@75!               ")
        print("                       !J?5                          :P7Y~               ")
        print("                       :YY                            :PJ                ")
        print("                       :!JP:                         ~G?!                ")
        print("                        ~J?B~                       !B7J^                ")
        print("                         J5!B7                     JG!P7                 ")
        print("                          PP~G!                   ?P~B5                  ")
        print("                          :&G^!!:               ^~!~#B                   ")
        print("                           ~@B::?               J ^#&^                   ")
        print("                            J@B:7^             !!^#@7                    ")
        print("                             P@G^J             Y^#@Y                     ")
        print("                              G@5?!           77G@5                      ")
        print("                               J5^7            ^Y?                       ")
        print("")
        print(f"                            {Fore.RED}LOKI{Fore.WHITE} - {motd}         ")
        print(f"                                     {version}")
        print("                                                                                ")
        print(f"{Fore.RED}  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.   .{Fore.WHITE}")
        print(f"{Fore.WHITE}:::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}:::")
        print(f"{Fore.RED}'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `.'{Fore.WHITE}")
        print(random.choice(tag))

    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)