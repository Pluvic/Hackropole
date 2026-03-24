# Hamac

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2022

## Description

Connaissez-vous l’existence de `rockyou` ?

## Write-Up

Il s'agit d'un challenge avec un chiffrement de mot de passe en utilisant HMAC. La description du challenge suggère que le mot de passe est dans la liste `rockyou`, qui est une liste de mots de passe couramment utilisés. En itérant sur les mots de passe de la liste `rockyou` et en utilisant le même processus de chiffrement que celui utilisé dans le challenge, on peut trouver le mot de passe correct qui correspond au mac fourni dans l'output.

La solution est dans le fichier `solve.py`.