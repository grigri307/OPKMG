import os
import platform

# Fonction pour effacer l'écran du terminal
def effacer_ecran():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Dessin ASCII
dessin = """
  ________  ________  ___  __    _____ ______   _______   _______      
 |\   __  \|\   __  \|\  \|\  \ |\   _ \  _   \|\  ___ \ |\  ___ \     
 \ \  \|\  \ \  \|\  \ \  \/  /|\ \  \\\__\ \  \ \   __/|\ \   __/|    
  \ \  \\\  \ \   ____\ \   ___  \ \  \\|__| \  \ \  \_|/_\ \  \_|/__  
   \ \  \\\  \ \  \___|\ \  \\ \  \ \  \    \ \  \ \  \_|\ \ \  \_|\ \ 
    \ \_______\ \__\    \ \__\\ \__\ \__\    \ \__\ \_______\ \_______\
     \|_______|\|__|     \|__| \|__|\|__|     \|__|\|_______|\|_______|
                                                                       
"""

# Demande à l'utilisateur de saisir un chemin d'emplacement
chemin_emplacement = input("Veuillez entrer le chemin d'emplacement (ex: C:\\user\\bureau) : ")

# Nom du fichier à créer
nom_du_fichier = "texte_saisi.txt"

# Combine le chemin d'emplacement et le nom du fichier
chemin_complet = os.path.join(chemin_emplacement, nom_du_fichier)

def afficher_menu():
    effacer_ecran()
    print(dessin)
    print("\nMenu :")
    print("1. Voir les mots enregistrés")
    print("2. Ajouter un mot")
    print("3. Quitter")

def voir_mots():
    effacer_ecran()
    if os.path.exists(chemin_complet):
        with open(chemin_complet, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            if contenu:
                print("Mots enregistrés :")
                print(contenu)
            else:
                print("Aucun mot n'est enregistré pour le moment.")
    else:
        print("Aucun mot n'est enregistré pour le moment.")

def ajouter_mot():
    effacer_ecran()
    texte = input("Veuillez entrer un mot, une phrase ou autre texte : ")
    with open(chemin_complet, 'a', encoding='utf-8') as fichier:
        fichier.write(texte + '\n')
    print(f"Le texte a été enregistré dans le fichier {chemin_complet}")

while True:
    afficher_menu()
    choix = input("Veuillez choisir une option (1, 2 ou 3) : ")

    if choix == '1':
        voir_mots()
        input("Appuyez sur Entrée pour revenir au menu...")
    elif choix == '2':
        ajouter_mot()
        input("Appuyez sur Entrée pour revenir au menu...")
    elif choix == '3':
        effacer_ecran()
        print("Fin du programme.")
        break
    else:
        print("Choix invalide, veuillez réessayer.")
        input("Appuyez sur Entrée pour revenir au menu...")
