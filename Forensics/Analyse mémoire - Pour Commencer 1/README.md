# Analyse mémoire - Pour Commencer 1

## Spécification

**Catégorie**: Forensics

**Difficulté estimée**: Intro

**Année**: 2025

## Description

La capture mémoire a été réalisée pendant qu’un utilisateur était en train de travailler sur un document hautement sensible. Si une compromission du poste a eu lieu, ce document a peut-être été volé. Pouvez-vous retrouver :

- le nom du logiciel d’édition du document,
- le nom du document.

Le flag est au format FCSC{<nom du logiciel>:<nom du document>} où :

- <nom du logiciel> est le nom de l'exécutable du logiciel d'édition et
- <nom du document> est le nom du document en cours d'édition par l'utilisateur (sans le chemin du fichier).


## Write-Up

Pour analyser la capture mémoire, j'utilise l'outil Volatility (Version 3). Je commence par identifier le système d'exploitation de la machine cible en utilisant la commande `vol.py -f memory_dump.raw windows.info`. Cela me donne des informations sur la version de Windows utilisée. 

### Retrouver le nom d'utilisateur de du pc
`vol.py -f analyse-memoire.dmp windows.sessions`

### Retrouver l'adresse IP de la machine
`vol.py -f analyse-memoire.dmp windows.netscan`

## Flag

FSCS{userfcsc-10:DESKTOP-JV996VQ:10.0.2.15}