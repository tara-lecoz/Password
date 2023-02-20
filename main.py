#----------------Password----------------

#-----Nécessaire ici pour crypter le mot de passe de l'utilisateur-----
import hashlib
#-----Nécessaire ici pour vérifier le mot de passe de l'utilisateur-----
import re
#-----Nécessaire ici pour créer un fichier json qui va créer une sauvegarde des mots de passe cryptés-----
import json
#-----Ouverture du fichier json en lecture et chargement des données présentes dans le fichier grâce au .load-----
try:
    with open("mdp_utilisateur.json", "r") as verif_utilisateurmdp:
        utilisateur_mdp = json.load(verif_utilisateurmdp)
#-----Si le fichier n'existe pas, création du fichier-----
except:
    utilisateur_mdp = {}
#-----Fonction qui vérifie que le mot de passe respecte les conditions-----
def verifier_mdp():
    global mdp
    mdp = input("Votre mot de passe : ")
    if len(mdp) < 8:
        print("Le mot de passe n'est pas valide (caractères < 8)")
    elif not re.search("[A-Z]", mdp):
        print("/!\ ERREUR /!\ Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not re.search("[a-z]", mdp):
        print("/!\ ERREUR /!\ Le mot de passe doit au moins contenir une lettre minuscule.")
    elif not re.search("[0-9]", mdp):
        print("/!\ ERREUR /!\ Le mot de passe doit au moins contenir un chiffre.")
    elif not re.search("[!@#$%^&*]", mdp):
        print("/!\ ERREUR /!\ Le mot de passe doit contenir au moins un caractère spécial.")
    else:
        print("Félicitations, votre mot de passe est valide !")
        return mdp
        
if verifier_mdp() == None:
    verifier_mdp()
#-----Hachage du mot de passe valide avec l'algorithme SHA-256-----
def mdp_hashe(mdp):
    mdp_hashe = hashlib.sha256(mdp.encode()).hexdigest()
    print("Mot de passe crypté : ", mdp_hashe)
    return mdp_hashe
#-----Vérification de la correspondance utilisateur / mot de passe & écriture dans le dictionnaire-----
utilisateur = input("Veuillez renseigner votre nom d'utilisateur :")
mdp_json = mdp
if utilisateur in utilisateur_mdp:
    if mdp_json in utilisateur_mdp[utilisateur]:
        print("Le mot de passe existe déjà !")
    elif mdp_json not in utilisateur_mdp[utilisateur]:
        utilisateur_mdp[utilisateur] += [mdp_hashe(mdp_json)]
        print("Mot de passe ajouté.")
else:
    utilisateur_mdp[utilisateur] = [mdp_hashe(mdp_json)]
    print("Mot de passe ajouté à l'historique.")
mdp_validehash = input("Afficher l'ensemble des mots de passe ? (o/n)")
if mdp_validehash.lower() == 'o':
    print(utilisateur_mdp[utilisateur])
with open("mdp_utilisateur.json", "w") as verif_utilisateurmdp:
    json.dump(utilisateur_mdp, verif_utilisateurmdp, separators=(",", " : "), indent=4)
mdp_valider = mdp
mdp_hashe(mdp_valider)