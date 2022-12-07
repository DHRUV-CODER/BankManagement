U=exit
P=True
L=False
K=int
H=input
C=print
import os,colorama as Q
from colorama import Fore as A,Style as B
Q.init(autoreset=P)
R=B.BRIGHT+A.LIGHTYELLOW_EX+f"""·▄▄▄▄   ▄ .▄▄▄▄  ▄• ▄▌ ▌ ▐·.▄▄ · 
██▪ ██ ██▪▐█▀▄ █·█▪██▌▪█·█▌▐█ ▀. 
▐█· ▐█▌██▀▐█▐▀▀▄ █▌▐█▌▐█▐█•▄▀▀▀█▄
██. ██ ██▌▐▀▐█•█▌▐█▄█▌ ███ ▐█▄▪▐█
▀▀▀▀▀• ▀▀▀ ·.▀  ▀ ▀▀▀ . ▀   ▀▀▀▀ {B.BRIGHT+A.LIGHTRED_EX}
██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██████╔╝███████║██╔██╗ ██║█████╔╝
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝"""+A.RESET
S=A.CYAN+f"""
{A.RESET+B.BRIGHT}1){A.LIGHTCYAN_EX}View The Amount of Money Left
{A.RESET+B.BRIGHT}2){A.LIGHTCYAN_EX}Deposit Money
{A.RESET+B.BRIGHT}3){A.LIGHTCYAN_EX}Cash-out
{A.RESET+B.BRIGHT}4){A.LIGHTCYAN_EX}Lend Money
{A.RESET+B.BRIGHT}5){A.LIGHTRED_EX+B.BRIGHT}Exit"""+A.RESET
D=1
T=100
M=0
I=1000
E=L
while P:
	if E:
		N=str(H(A.RESET+B.BRIGHT+'\n\nWanna Continue Y/N:'+A.LIGHTYELLOW_EX))
		if N.lower()=='y':os.system('cls');E=L;continue
		elif N.lower()=='n':E=L;U()
		else:continue
	E=L;C(R);C(S);F=K(H(B.BRIGHT+A.LIGHTWHITE_EX+'\nChoose An Option: '+A.GREEN));E=P
	if F==1:C(A.LIGHTBLUE_EX+f"You Have {B.BRIGHT+A.GREEN}${D}{A.LIGHTBLUE_EX} Left"+A.RESET)
	elif F==2:
		O=K(H(A.RESET+f"Amount Of Money To Be Deposited: {A.YELLOW}$"))
		if O>T:C('Bro you Broke :(')
		else:D+=O;C(A.LIGHTBLUE_EX+f"Now You Have {B.BRIGHT+A.GREEN}${D}{A.LIGHTBLUE_EX}"+A.RESET)
	elif F==3:
		J=K(H(f"Money To Be Transacted Out Ff ${D}"))
		if J>D:C(f"Compromise on ${J-D}")
		else:C(f"${J} Transacted Successfully!!")
	elif F==4:
		G=K(H(f"Amount of Money You Want To Lend , Currently You Have {B.BRIGHT+A.RED}${I}{A.RESET} That You Can Lend : "+A.RESET))
		if G>I:C(f"You Have To Compromise On {A.RED+B.BRIGHT}${G-I}"+A.RESET)
		else:D+=G;M+=G;C(f"{A.GREEN+B.BRIGHT}${G}{A.RESET} Lended , Now You Have Debt Of {A.RED+B.BRIGHT}${M}{A.RESET}\n")
	elif F==5:U()