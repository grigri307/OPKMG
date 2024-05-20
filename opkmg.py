import os
import platform

def effacer_ecran():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

dessin = """
  ________  ________  ___  __    _____ ______   _______       
 |\   __  \|\   __  \|\  \|\  \ |\   _ \  _   \|\  ___ \      
 \ \  \|\  \ \  \|\  \ \  \/  /|\ \  \\\__\ \  \ \   __/|   
  \ \  \\\  \ \   ____\ \   ___  \ \  \\|__| \  \ \  \_|/_  
   \ \  \\\  \ \  \___|\ \  \\ \  \ \  \    \ \  \ \  \_|\ \ 
    \ \_______\ \__\    \ \__\\ \__\ \__\    \ \__\ \_______\ 
     \|_______|\|__|     \|__| \|__|\|__|     \|__|\|_______|
                                                                       
"""

chemin_emplacement = input("Veuillez entrer le chemin d'emplacement (ex: C:\\user\\bureau) : ")

def liste_fichiers():
    effacer_ecran()
    print(dessin)
    print("\nListe des fichiers créés :")
    fichiers = os.listdir(chemin_emplacement)
    if fichiers:
        for fichier in fichiers:
            print(fichier)
    else:
        print("Aucun fichier n'a été créé dans ce répertoire.")

nom_fichier = input("Veuillez entrer le nom du fichier (ex: texte_saisi) : ")

extension_fichier = input("Veuillez entrer l'extension du fichier (ex: txt) : ")

nom_du_fichier = f"{nom_fichier}.{extension_fichier}"

chemin_complet = os.path.join(chemin_emplacement, nom_du_fichier)

def afficher_menu_principal():
    effacer_ecran()
    print(dessin)
    print("\nMenu principal :")
    print("1. Voir les mots enregistrés")
    print("2. Ajouter un mot")
    print("3. Supprimer un mot")
    print("4. Configurer le fichier texte")
    print("5. Exécuter le fichier texte")
    print("6. Voir tous les fichiers")
    print("7. Supprimer le fichier")
    print("8. Quitter")

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

def supprimer_mot():
    effacer_ecran()
    if os.path.exists(chemin_complet):
        mot_a_supprimer = input("Veuillez entrer le mot à supprimer : ")
        with open(chemin_complet, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()
        with open(chemin_complet, 'w', encoding='utf-8') as fichier:
            for ligne in lignes:
                if ligne.strip() != mot_a_supprimer:
                    fichier.write(ligne)
        print(f"Le mot '{mot_a_supprimer}' a été supprimé avec succès.")
    else:
        print("Aucun mot n'est enregistré pour le moment.")

def configurer_fichier():
    global chemin_emplacement, nom_fichier, extension_fichier, chemin_complet
    chemin_emplacement = input("Veuillez entrer le nouveau chemin d'emplacement : ")
    nom_fichier = input("Veuillez entrer le nouveau nom du fichier : ")
    extension_fichier = input("Veuillez entrer la nouvelle extension du fichier : ")
    nom_du_fichier = f"{nom_fichier}.{extension_fichier}"
    chemin_complet = os.path.join(chemin_emplacement, nom_du_fichier)
    print("Configuration du fichier texte mise à jour avec succès.")

def executer_fichier():
    effacer_ecran()
    if os.path.exists(chemin_complet):
        os.system(chemin_complet)
    else:
        print("Le fichier spécifié n'existe pas.")

def supprimer_fichier():
    effacer_ecran()
    if os.path.exists(chemin_complet):
        os.remove(chemin_complet)
        print(f"Le fichier {nom_du_fichier} a été supprimé avec succès.")
    else:
        print("Le fichier spécifié n'existe pas.")

while True:
    afficher_menu_principal()
    choix_principal = input("Veuillez choisir une option (1-8) : ")

    if choix_principal == '1':
        voir_mots()
        input("Appuyez sur Entrée pour revenir au menu principal...")
    elif choix_principal == '2':
        ajouter_mot()
        input("Appuyez sur Entrée pour revenir au menu principal...")
    elif choix_principal == '3':
        supprimer_mot()
        input("Appuyez sur Entrée pour revenir au menu principal...")
    elif choix_principal == '4':
        configurer_fichier()
        input("Appuyez sur Entrée pour revenir au menu principal...")
    elif choix_principal == '5':
        executer_fichier()
        input("Appuyez sur Entrée pour revenir au menu principal...")
    elif choix_principal == '6':
        liste_fichiers()
        input("Appuyez sur Entrée pour revenir au menu principal...")
    elif choix_principal == '7':
        supprimer_fichier()
        input("Appuyez sur Entrée pour revenir au menu principal...")
    elif choix_principal == '8':
        effacer_ecran()
