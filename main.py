# Menu Driven Banking system
# Author : Dhruv
# LICENCE : MIT

import os

import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)

TITLE=Style.BRIGHT+Fore.LIGHTYELLOW_EX+f"""·▄▄▄▄   ▄ .▄▄▄▄  ▄• ▄▌ ▌ ▐·.▄▄ · 
██▪ ██ ██▪▐█▀▄ █·█▪██▌▪█·█▌▐█ ▀. 
▐█· ▐█▌██▀▐█▐▀▀▄ █▌▐█▌▐█▐█•▄▀▀▀█▄
██. ██ ██▌▐▀▐█•█▌▐█▄█▌ ███ ▐█▄▪▐█
▀▀▀▀▀• ▀▀▀ ·.▀  ▀ ▀▀▀ . ▀   ▀▀▀▀ {Style.BRIGHT+Fore.LIGHTRED_EX}
██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██████╔╝███████║██╔██╗ ██║█████╔╝
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝"""+Fore.RESET

menu = Fore.CYAN+f"\n{Fore.RESET+Style.BRIGHT}1){Fore.LIGHTCYAN_EX}View The Amount of Money Left\n{Fore.RESET+Style.BRIGHT}2){Fore.LIGHTCYAN_EX}Deposit Money\n{Fore.RESET+Style.BRIGHT}3){Fore.LIGHTCYAN_EX}Cash-out\n{Fore.RESET+Style.BRIGHT}4){Fore.LIGHTCYAN_EX}Lend Money\n{Fore.RESET+Style.BRIGHT}5){Fore.LIGHTRED_EX+Style.BRIGHT}Exit"+Fore.RESET

MoneyInTheBankRN = 1
DeafultMoneyGiven = 100
DEBT = 0
LOAN = 1000
ContinutionGoingOn = False
while True:
    if ContinutionGoingOn:
        askthem = str(input(Fore.RESET+Style.BRIGHT+"\n\nWanna Continue Y/N:"+Fore.LIGHTYELLOW_EX))
        if askthem.lower() == "y":
            os.system('cls')
            ContinutionGoingOn = False
            continue
        elif askthem.lower() == "n" :
            ContinutionGoingOn = False
            exit()
        else:continue
    
    ContinutionGoingOn = False
    print(TITLE)
    print(menu)
    user_input = int(input(Style.BRIGHT+Fore.LIGHTWHITE_EX+"\nChoose An Option: "+Fore.GREEN))
    ContinutionGoingOn = True

    if user_input == 1:
        print(Fore.LIGHTBLUE_EX+f"You Have {Style.BRIGHT+Fore.GREEN}${MoneyInTheBankRN}{Fore.LIGHTBLUE_EX} Left"+Fore.RESET)
    elif user_input == 2:
        AmountOfMoneyToBeDeposited = int(input(Fore.RESET+f"Amount Of Money To Be Deposited: {Fore.YELLOW}$"))
        if AmountOfMoneyToBeDeposited > DeafultMoneyGiven:
            print("Bro you Broke :(")
        else:
            MoneyInTheBankRN += AmountOfMoneyToBeDeposited
            print(Fore.LIGHTBLUE_EX+f"Now You Have {Style.BRIGHT+Fore.GREEN}${MoneyInTheBankRN}{Fore.LIGHTBLUE_EX}"+Fore.RESET)
    elif user_input == 3:
        AmountOfMoneyToBeTransacted = int(input(f"Money To Be Transacted Out Ff ${MoneyInTheBankRN}"))
        if AmountOfMoneyToBeTransacted > MoneyInTheBankRN:
            print(f"Compromise on ${AmountOfMoneyToBeTransacted-MoneyInTheBankRN}")
        else:
            print(f"${AmountOfMoneyToBeTransacted} Transacted Successfully!!")
    elif user_input ==4:
        AmountOfMoneyToBeLended = int(input(f"Amount of Money You Want To Lend , Currently You Have {Style.BRIGHT+Fore.RED}${LOAN}{Fore.RESET} That You Can Lend : "+Fore.RESET))
        if AmountOfMoneyToBeLended > LOAN:
            print(f"You Have To Compromise On {Fore.RED+Style.BRIGHT}${AmountOfMoneyToBeLended-LOAN}"+Fore.RESET)
        else:
            MoneyInTheBankRN += AmountOfMoneyToBeLended
            DEBT += AmountOfMoneyToBeLended
            print(f"{Fore.GREEN+Style.BRIGHT}${AmountOfMoneyToBeLended}{Fore.RESET} Lended , Now You Have Debt Of {Fore.RED+Style.BRIGHT}${DEBT}{Fore.RESET}\n")
    elif user_input == 5:exit()
    
# TO-DO:IMPLEMENT DB-SYSTEM