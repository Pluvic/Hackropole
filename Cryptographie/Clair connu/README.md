# Clair connu

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2021

## Description

Votre but est de déchiffrer le flag.

## Write-Up

Le fichier `clair-connu.py` contient le code de chiffrement du flag. En analysant ce code, on peut voir que le chiffrement est fait en utilisant une opération de XOR entre le flag et une clé. On sait que la clé est quatre bits généré aléatoirement qui sont répétés sur tout le flag. Comme on connait les 4 premiers caractères du flag : `FCSC{`, on peut facilement trouver la clé en faisant un XOR entre ces 4 caractères et les 4 premiers caractères du flag chiffré. Une fois que nous avons la clé, nous pouvons déchiffrer le flag en faisant un XOR entre le flag chiffré et la clé répétée sur toute la longueur du flag.

Le fichier `solve.py` contient le code pour trouver la clé et déchiffrer le flag.