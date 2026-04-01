# SMIC (2)

## Specifications

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2020

## Description

La sécurité du cryptosystème RSA repose sur un problème calculatoire bien connu.

On vous demande de déchiffrer le “message” chiffré c ci-dessous pour retrouver le “message” en clair m associé à partir de la clé publique (n, e).

Valeurs :

    e = 65537
    n = 632459103267572196107100983820469021721602147490918660274601
    c = 63775417045544543594281416329767355155835033510382720735973

Le flag est FCSC{xxxx} où xxxx est remplacé par la valeur de m en écriture décimale.


## Write-Up

Pour résoudre ce challenge, il suffit de factoriser n pour retrouver les facteurs premiers p et q, puis calculer la clé privée d et enfin déchiffrer le message c pour obtenir m. On peut retrouver les facteurs premiers de n en utilisant l'outil en ligne `factordb.com`. Une fois ceux-ci obtenus, il suffit d'appliquer les formules de RSA pour trouver d et ensuite m.

La solution est implémentée dans le fichier `solve.py`.