LICENCE = """
Copyright © 2022 Celwo#4471

Ce logiciel a été developper entièrement par Celwo (ps: c"est mon premier tool).

L'avis de copyright ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.


"""

import time
import os

print(LICENCE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

import random
import string
import ctypes

try: # Vérifiez si les éléments requis ont été installés
    from discord_webhook import DiscordWebhook # Essayer d'importer discord_webhook
except ImportError: # Si elle ne peut être installée
    input(f"Le module discord_webhook n'est pas installé, pour l'installer exécutez '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPressez Entrée pour quitter.") # Indiquer à l'utilisateur qu'il n'a pas été installé et comment l'installer.
    exit() # Quitter le programme
try: # Mise en place d'une instruction try pour attraper l'erreur
    import requests # Essayer d'importer des demandes
except ImportError: # S'il n'a pas été installé
    input(f"Le module requests n'est pas installé, pour l'installer exécutez '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPressez Entrée pour quitter.")# Indiquer à l'utilisateur qu'il n'a pas été installé et comment l'installer.
    exit() # Quitter le programme


class NitroGen: # Initialiser la classe
    def __init__(self): # La fonction d'initialisation
        self.fileName = "Nitro Valides.txt" # Le nom du fichier dans lequel les codes sont stockés

    def main(self): # La fonction principale contient le code le plus important
        os.system('cls' if os.name == 'nt' else 'clear') # Effacer l'écran
        if os.name == "nt": # Si le système est Windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Celwo | Nitro Generator and Checker") # Changer le
        else: # Ou si c'est unix
            print(f'\33]0;Celwo | Nitro Generator and Checker\a', end='', flush=True) # Mettre à jour le titre du cmd

        print("""
_________        .__                
\_   ___ \  ____ |  |__  _  ______  
/    \  \/_/ __ \|  |\ \/ \/ /  _ \ 
\     \___\  ___/|  |_\     (  <_> )
 \______  /\___  >____/\/\_/ \____/ 
        \/     \/                   
          Par Celwo#4471
    Join our Discord ! https://discord.gg/cXsCgk37CU          
                                                  
                                                  """) 
        time.sleep(2) # Attendre quelques secondes
        self.slowType("", .02) # Afficher qui a développer le code
        time.sleep(1) # Attendre un peu plus
        self.slowType("\nSaisissez le nombre de codes à générer et à vérifier: ", .02, newLine = False) # Afficher la première question

        num = int(input('')) # Demander à l'utilisateur le nombre de codes à générer et à check

        # Obtenez l'url du webhook, si l'utilisateur ne souhaite pas utiliser un webhook, le message sera une chaîne vide.
        self.slowType("\nSouhaitez-vous utiliser un webhook discord ? Si oui, tapez-le ici ou appuyez sur Entrée pour ignorer.: ", .02, newLine = False)
        url = input('') # Obtenir la réponse.
        webhook = url if url != "" else None # Si l'url est vide, il doit être remplacé par None.

        # print() # Afficher une nouvelle ligne.

        valide = [] # Gardez la trace des codes Validees
        invalide = 0 # Gardez une trace du nombre de codes inValidees détectés.

        for i in range(num): # Boucle sur le nombre de codes à vérifier
            try: # Corriger les erreurs qui peuvent survenir
                code = "".join(random.choices( # Générer l'identifiant pour le cadeau
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" # Générer l'url

                result = self.quickChecker(url, webhook) # Vérifiez les codes

                if result: # Si le code était Valide
                    valide.append(url) # Ajoutez ce code à la liste des codes trouvés
                else: # Si le code n'était pas Valide
                    invalide += 1 # Augmenter d'une unité le compteur d'invalidité
            except Exception as e: # Si la demande échoue
                print(f" Erreur | {url} ") # Indiquer à l'utilisateur qu'une erreur s'est produite

            if os.name == "nt": # Si le système est Windows
                ctypes.windll.kernel32.SetConsoleTitleW(f"Celwo | Nitro Generator and Checker - {len(valide)} Valide | {invalide} Invalide ") # Modifier le titre du cmd
                print("")
            else: # S'il s'agit d'un système unix
                print(f'\33]0;Nitro Generator and Checker - {len(valide)} Valide | {invalide} InValide \a', end='', flush=True) # Modifier le titre du cmd

        print(f"""
Results:
 valide: {len(valide)}
 invalide: {invalide}
 valide Codes: {', '.join(valide )}""") # Donner un rapport sur les résultats du contrôle

        input("\nFin ! Appuyez 5 fois sur la touche Entrer pour fermer le programme.") # Indiquer à l'utilisateur que le programme est terminé
        [input(i) for i in range(4,0,-1)] # Attendez 4 pressions d'entrée


    def slowType(self, text, speed, newLine = True): # Fonction utilisée pour afficher un texte un peu plus sophistiqué
        for i in text: # Loop over the message
            print(i, end = "", flush = True) # Imprime le seul caractère, flush est utilisé pour forcer python à afficher le caractère.
            time.sleep(speed) # Dormir un peu avant la prochaine
        if newLine: # Vérifier si l'argument newLine a la valeur True.
            print() # afficher une nouvelle ligne finale pour que l'opération se déroule comme une instruction d'impression normale.

    def generator(self, amount): # Fonction utilisée pour générer et stocker les codes nitro dans un fichier séparé.
        with open(self.fileName, "w", encoding="utf-8") as file: # Chargement du fichier en mode écriture
            print("Attendez, je génère pour vous") # Faire savoir à l'utilisateur que le code génère les nitros

            start = time.time() # Notez le temps d'initialisation

            for i in range(amount): # Boucler la quantité de codes à générer
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # Générer le code d'identification

                file.write(f"https://discord.gift/{code}\n") # Écrire le code

            # Dire à l'utilisateur que la génération est terminée et combien de temps cela a pris.
            print(f"{amount} nitros générés | Temps pris: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): # Fonction utilisée pour vérifier les codes nitro à partir d'un fichier
        Valide = [] # Une liste de codes Valide
        inValide = 0 # La quantité de codes invalides détectés
        with open(self.fileName, "r", encoding="utf-8") as file: # Ouvrir le fichier contenant les codes nitro
            for line in file.readlines(): # Boucle sur chaque ligne du fichier
                nitro = line.strip("\n") # Enlever le newline à la fin du code nitro

                # Créer l'url de la demande pour une utilisation ultérieure
                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) # Obtenir la réponse à partir de l'url

                if response.status_code == 200: # Si la réponse est passée
                    print(f" Valide | {nitro} ") # Notifier à l'utilisateur que le code a été Valide
                    Valide.append(nitro) # Ajouter le code nitro à la liste des codes Valide.

                    if notify is not None: # Si un webhook a été ajouté
                        DiscordWebhook( # Envoyer le message sur discord pour faire savoir à l'utilisateur qu'il y a eu un code nitro Valide.
                            url = notify,
                            content = f"Code Nitro Valide détecté ! @everyone \n{nitro}"
                        ).execute()
                    else: # S'il n'y a pas eu d'installation de webhook discord, arrêter le code.
                        break # terminer la boucle puisqu'aucun code Valide a été trouvé

                else: # Si la réponse a été ignorée ou est invalide ( comme une 404 ou 405 )
                    print(f" invalide | {nitro} ") # Dire à l'utilisateur qu'il a testé un code et qu'il était invalide
                    invalide += 1 # Augmenter le compteur invalide d'une unité

        return {"valide" : valide, "invalide" : invalide} # Renvoyer un rapport des résultats

    def quickChecker(self, nitro, notify = None): # Utilisé pour vérifier un seul code à la fois
        # Générer l'url de la requête
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # Obtenir la réponse de discord

        if response.status_code == 200: # Si la réponse est passée
            print(f" valide | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Notifier à l'utilisateur que le code a été Valide
            with open("Nitro Valides.txt", "w") as file: # Ouvrir le fichier pour écrire
                file.write(nitro) # Ecrire le code nitro dans le fichier, il ajoutera automatiquement une nouvelle ligne.

            if notify is not None: # Si un webhook a été ajouté
                DiscordWebhook( # Envoyer le message sur discord pour faire savoir à l'utilisateur qu'il y a eu un code nitro Valide.
                    url = notify,
                    content = f"Code Nitro Valide détecté! @everyone \n{nitro}"
                ).execute()

            return True # Dire à la fonction principale que le code a été trouvé

        else: # Si la réponse a été ignorée ou est invalide (par exemple 404 ou 405).
            print(f" invalide | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Dire à l'utilisateur qu'il a testé un code et qu'il était invalide
            return False # Dire à la fonction principale qu'il n'y a pas de code trouvé

if __name__ == '__main__':
    Gen = NitroGen() # Créer l'objet générateur de nitro
    Gen.main() # Exécuter le code principal
