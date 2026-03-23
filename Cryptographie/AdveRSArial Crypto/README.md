# AdveRSArial Crypto

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2024

## Description

Je viens de suivre un cours sur RSA mais je crois que j’ai oublié quelque chose. Il me semble que le prof parlait de deux trucs, mais je ne sais plus exactement quoi. Vous pouvez m’aider ?

## Write-Up

Le challenge est un RSA mais qui a mal été implémenté. En effet, le module n est un nombre premier plutôt qu'un multiple de nombre premiers. De ce fait, il est possible de calculer la clé privée d en utilisant la formule d = e^-1 mod (n-1). Ensuite, il suffit de calculer le flag en utilisant la formule flag = c^d mod n.

La solution est disponible dans le fichier `solve.py`.