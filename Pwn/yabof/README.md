# YABOF - Yet another Buffer Overflow

## Spécification

**Catégorie**: Pwn

**Difficulté estimée**: Intro

**Année**: 2025

## Description

Le challenge consiste en un binaire vulnérable à un buffer overflow. Le but est d'exploiter cette vulnérabilité pour exécuter du code arbitraire et récupérer le flag.

## Write-Up

Je teste et le programme et il me demande d'entrer soit y ou n. Il s'agit d'un input donc on peut y entrer n'importe quoi. En inspectant le programme grâce à l'outil gdb. Je repère qu'il y a une fonction qui s'appelle `vuln` qui récupérer l'entrée utilisateur. On peut aussi observer une fonction qui s'appelle `yabof` qui n'est jamais appelée. On peut récupérer son adresse pour rediriger le retour de la fonction `vuln` vers la fonction `yabof`. Pour savoir l'offset, on peut voir que le programme fait un `sub rsp 0x10` ce qui signifie que l'offset est de 16. En exploitant le buffer overflow, on peut rediriger le flux d'exécution vers la fonction `yabof` et ainsi récupérer le flag.

La solution se trouve dans le fichier `solve.py` qui utilise la bibliothèque `pwntools` pour automatiser l'exploitation du binaire.

## Flag
FCSC{2c4c4b3be7d86e1642ce6a8bf1bd75f33b9736e5943f51a49fb9327e248c3b6a}