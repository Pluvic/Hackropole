# La quête de l'anneau

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: ⭐

**Année**: 2025

## Description

Sauron a mis au point un système de chiffrement pour communiquer avec les Nazgûl. Il n’a pas pu s’empêcher d’utiliser un anneau secret pour le sécuriser. Vos alliés elfes ont tendu leurs oreilles pour intercepter des messages. Saurez-vous montrer à Sauron que sa maîtrise des anneaux n’est pas encore au point ?

## Write-Up

Le chiffrement utilisé a une faille. En effet comme il nous donne deux paires de messages chiffrés avec des IV différents, on peut faire un calcul de PGCD pour trouver la valeur de s. Ensuite, il suffit de faire un calcul de division modulaire pour trouver le flag.

C1 = m1 * iv1 mod s donc C1 = m1 * iv1 - k * s pour un certain k

C2 = m2 * iv2 mod s donc C2 = m2 * iv2 - l * s pour un certain l

On peut faire le calcul suivant :

pgcd(m1 * iv1 - C1, m2 * iv2 - C2) = s

Une fois qu'on a notre s, on peut faire le calcul suivant pour trouver le flag :

flag = C * pow(iv, -1, s) mod s

La solution est présente dans le fichier `solve.py`
