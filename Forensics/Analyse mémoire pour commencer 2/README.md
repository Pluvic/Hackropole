# Analyse mémoire - Pour Commencer 2

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

Par exemple : FCSC{calc.exe:Mes comptes 2025.txt}.

## Write-Up

Pour retrouver les infos qu'il nous faut, il suffit d'utiliser volatility avec la commande `vol.py -f analyse-memoire.dmp windows.commandline`. Cette commande affiche les processus en cours d'exécution et leurs arguments de ligne de commande. En filtrant les résultats, on peut trouver le processus correspondant au logiciel d'édition et le nom du document.

## Flag

FCSC{soffice.exe:[SECRET-SF][TLP-RED]Plan FCSC 2026.odt}