# La PIN

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2021

## Description

J’ai protégé le flag en le chiffrant avec des algorithmes modernes. Pourrez-vous le retrouver ?

## Write-Up

La sécurité de ce challenge repose sur un code pin qui fait 4 chiffres. Cela signifie qu’il y a 10 000 combinaisons possibles, ce qui est relativement faible. En utilisant une attaque par force brute, on peut essayer toutes les combinaisons possibles de pin jusqu’à trouver celui qui déchiffre correctement le flag.

La solution est dans le fichier `solve.py`.

