# CocoRICo

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: ⭐

**Année**: 2025

## Description

On a un chiffrement AES en mode OFB de l'utilisateur toto avec son champ admin à true. Le code du challenge ne nous permet que d'avoir des tokens avec le champ admin à false. Le code du challenge est présent dans le fichier `cocorico.py`.

## Write-Up

Le chiffrement AES en mode OFB est un chiffrement par flot, ce qui signifie que le chiffrement de chaque bloc dépend du bloc précédent. Cependant, dans ce challenge, nous avons la possibilité de récupérer le keystream en XORant le token chiffré avec le plain text connu (le token d'un utilisateur choisi aléatoirement avec admin à false). Une fois que nous avons le keystream, nous pouvons construire un token chiffré pour l'utilisateur admin en XORant le plain text de l'utilisateur admin avec le keystream.

La solution est présente dans le fichier `solve.py`
