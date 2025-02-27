- [git-evaluation\_groupe-3](#git-evaluation_groupe-3)
  - [Format des Commit:](#format-des-commit)
- [Installation:](#installation)
- [Exécution](#exécution)
  - [1) Utilisation interactive](#1-utilisation-interactive)
  - [2) Utilisation en lisant `STDIN` avec `echo`](#2-utilisation-en-lisant-stdin-avec-echo)
  - [3) Utilisation en lisant `STDIN` avec `cat`](#3-utilisation-en-lisant-stdin-avec-cat)
- [Générator](#générator)
  - [Exécution](#exécution-1)
  - [Gestion des erreurs](#gestion-des-erreurs)
    - [1) Le paramètre doit être un entier positif](#1-le-paramètre-doit-être-un-entier-positif)
      - [Procédure pour reproduire cette erreur:](#procédure-pour-reproduire-cette-erreur)
    - [2) Un seul argument est attendu au lancement du programme](#2-un-seul-argument-est-attendu-au-lancement-du-programme)
      - [Procédure pour reproduire cette erreur:](#procédure-pour-reproduire-cette-erreur-1)
    - [3) Il faut entrer au moins un argument au lancement du programme](#3-il-faut-entrer-au-moins-un-argument-au-lancement-du-programme)
      - [Procédure pour reproduire cette erreur:](#procédure-pour-reproduire-cette-erreur-2)
  - [Github Actions - Test Minitrice](#github-actions---test-minitrice)
  - [Exécution](#exécution-2)
  - [Fonctionnement](#fonctionnement)
- [Publication](#publication)


# git-evaluation_groupe-3
Evaluation UE - Nouveaux services de communication.
Composition du groupe: 
  - Adrien Kenny
  - Beurard Kilian
  - Moutouvirin Jean-Philippe 

## Format des Commit:
  Pour le format des commits on utilisera ce standard: https://buzut.net/cours/versioning-avec-git/bien-nommer-ses-commits
  Sans les émojis de préférence.

# Installation:
Pour lancer ce programme, vous aurez besoin de python.
Pour installer python:

- Sur windows, dans le cmd, tapez la commande:
```bash
curl -o python-installer.exe https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe

python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

```

- Sur linux, dans un terminal, tapez la commande:
```bash
sudo apt install python3
```

# Exécution
## 1) Utilisation interactive
Pour éxécuter le programme tapez la commande:
```bash
./minitrice
```
tapez ensuite l'expresison que vous voulez évaluer dans le prompt qui s'affiche:
```bash
> 5+12
```
## 2) Utilisation en lisant `STDIN` avec `echo`
Vous pouvez aussi utiliser l'entrée standard ```STDIN``` pour évaluer votre expression:
```bash
$ echo "3+12" | ./minitrice
```
## 3) Utilisation en lisant `STDIN` avec `cat`
Vous pouvez aussi mettre un fichier en entrée pour calculer plusieurs expressions à la fois.

Soit le fichier exemple.txt contenant ces lignes:
```
2+5
2-3
14/4
4*5
```

On va l'envoyer à l'entrée du programme comme ceci:

```bash
$ cat exemple.txt | ./minitrice
```
Ceci va nous renvoyer sur la sortie ```STDOUT```:
```
7
-1
3.5
20
```
# Générator

```generator``` est un programme permettant de générer un nombre ```n``` opérations de façon aléatoire avant de les renvoyer sur la sortie ```STDOUT```. La valeur de ```n``` est choisie par l'utilisateur.

## Exécution
L'exécution de ce programme requiert la présence d'un argument en ligne de commande. Afin de générer ```n``` opérations, l'utilisateur devra exécuter la commande suivante :

```bash
./generator <n>
```

## Gestion des erreurs
Afin de garantir le bon fonctionnement de ce programme, les deux conditions suivantes doivent être respectées sous peine de lever les erreurs suivantes :

### 1) Le paramètre doit être un entier positif
Le paramètre doit être un nombre entier positif. Tout argument ne respectant pas cette condition lèvera l'erreur suivante :

```bash
"Exception: Erreur : L'argument en entree doit etre un nombre entier positif"
```
#### Procédure pour reproduire cette erreur:
```bash
$ ./generator a
```

### 2) Un seul argument est attendu au lancement du programme
Lancer le programme avec plus d'un seul argument lèvera l'erreur suivante :

```bash
"Exception: Erreur : Un seul argument attendu sur la ligne de commande !"
```
#### Procédure pour reproduire cette erreur:
```bash
$ ./generator 2 4
```

### 3) Il faut entrer au moins un argument au lancement du programme
Lancer le programme avec moins d'un argument lèvera l'erreur suivante :

```bash
"Erreur : L'argument en entree doit etre un nombre entier positif"
```
#### Procédure pour reproduire cette erreur:
```bash
$ ./generator
```

## Github Actions - Test Minitrice

```test_minitrice.yml``` est un workflow qui permet de tester le minitrice sur les fichiers de test fourni dans le répertoire ```test/```.

## Exécution
Ce workflow n'a pas de lancement automatique, pour l'exécuter il faut aller dans l'onglet Action puis accéder au workflow "Test Minitrice", ou plus simplement [en cliquant ici](https://github.com/Ke2nigrec/git-evaluation_groupe-3/actions/workflows/test_minitrice.yml). Appuyé ensuite sur le bouton "Run workflow" et lancez le sur le main.

## Fonctionnement
Ce worflow permet à la fois de mettre à jour les résultats de test sur les fichiers test mais aussi de constater simplement ces résultats.
Plus concrètement, il créer une branche qui met à jour le dossier ```/results```. Si vous souhaitez apporté ces modifications à la main, il vous suffit de lancer une Pull Request et de merge la branche au main. L'historique restera propre car la branche est rebase sur la main par défaut. Si vous ne souhaitez pas sauvegarder ces modifications, **supprimez la branche**.

REMINDER: Pensez à supprimer la branche à chaque fois que vous avez terminé son utilisation !

# Publication
- [Organisation du développement collaboratif](https://slides.com/frozar/git) : le support de cours pour git/github,
- [How to capture Control+D signal?](https://stackoverflow.com/questions/1516122/how-to-capture-controld-signal) : discussion sur l'interception du signal `End Of File`,
- [Find out if there is input from a pipe or not in Python?](https://stackoverflow.com/questions/33871836/find-out-if-there-is-input-from-a-pipe-or-not-in-python) : discussion sur la détection de l'utilisation d'un pipe en Python,
- [My Gource video production pipeline](https://dev.to/voieducode/my-gource-video-production-pipeline-5eb0) : décrit un exemple d'utilisation de gource,
- [Git: bien nommer ses commits](https://buzut.net/cours/versioning-avec-git/bien-nommer-ses-commits) : décrit les bonne utilisation des commentaires dans les commits git
