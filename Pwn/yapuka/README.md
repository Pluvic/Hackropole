# yapuka

## Spécification

**Catégorie**: Pwn

**Difficulté estimée**: Intro

**Année**: 2025

## Description

Le challenge est un binaire qui affiche un dump de sa mémoire et qui nous demande d'entrer une adresse mémoire et une valeur.

## Write-Up

En analysant le binaire et en le décompilant, on peut voir qu'il utilise la fonction `puts` avec en argument `/bin/sh`. On comprends donc qu'il va falloir modifier la GOT de `puts` pour rediriger son exécution vers la fonction `system`. En analysant le dump de mémoire, on peut récupérer les adresses de la base du binaire, de la libc et de la stack. Avec ces adresses, on peut calculer l'adresse de `puts` dans la GOT et l'adresse de `system` dans la libc. Il ne reste plus qu'à envoyer ces adresses au programme pour rediriger l'exécution vers `system` et ainsi récupérer le flag.

La solution se trouve dans le fichier `solve.py` qui utilise la bibliothèque `pwntools` pour automatiser l'exploitation du binaire.