# Le Rat Conteur

## Specifications

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2020

## Description

Le fichier suivant a été chiffré en AES-128 en mode CTR, avec la clé de 128 bits 00112233445566778899aabbccddeeff et un IV nul.

À vous de le déchiffrer pour obtenir le flag.

## Write-Up

Le chiffrement AES-128 en mode CTR est un chiffrement par flux, ce qui signifie que le chiffrement de chaque bloc dépend de l'IV et de la clé, mais pas du bloc précédent. Avec une clé et un IV connus, il est possible de déchiffrer le message chiffré sans soucis.

La solution est dans le fichier `solve.py`.