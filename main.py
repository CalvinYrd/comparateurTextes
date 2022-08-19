from os import name as os_name, system as os_system
from colorama import Fore as colorama_Fore

if os_name == "nt":
	clear = lambda: os_system("cls")

else:
	clear = lambda: os_system("clear")

clear()
a = input("Saisissez le premier texte :\n> ")
b = input("Saisissez le second texte :\n> ")

if a.replace(" ", "").replace("\t", "") and b.replace(" ", "").replace("\t", ""):
	reduceSpace = [True if input("\nRéduire les espaces résiduels ? (o/n ; tappez <Entrer> pour refuser (valeur par défaut))\n> ").replace(" ", "").replace("\t", "").lower() == "o" else False][0]
	lower = [False if input("\nactiver la casse (ex : salut != sALuT) ? (o/n ; tappez <Entrer> pour refuser (valeur par défaut))\n> ").replace(" ", "").replace("\t", "").lower() == "o" else True][0]

	if lower:
		a = a.lower()
		b = b.lower()

	if reduceSpace:
		a = " ".join([word for word in a.split(" ") if word])
		b = " ".join([word for word in b.split(" ") if word])

	if len(a) < len(b):
		var = "a"

	else:
		var = "b"

	globals()[var] += (max((len(a), len(b))) - min((len(a), len(b)))) * " "

	aResult = ""
	bResult = ""
	clear()

	for i in range(max((len(a), len(b)))):
		if a[i] != b[i]:
			aResult += colorama_Fore.GREEN + a[i] + colorama_Fore.RESET
			bResult += colorama_Fore.GREEN + b[i] + colorama_Fore.RESET

		else:
			aResult += a[i]
			bResult += b[i]

	print("Les différences sont écrites en" + colorama_Fore.GREEN + " VERT" + colorama_Fore.RESET + ".\n\n" + aResult + '\n\n' + bResult)

else:
	print("un ou plusieurs des champs est/sont vide(s)")
