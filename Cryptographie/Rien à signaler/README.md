# Rien à signaler

## Specifications

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2024

## Description

J’ai chiffré le flag avec le cryptosystème à clé publique bien connu RSA.

## Write-Up

Le chiffrement RSA a été mal réalisé. En effet il a inversé la clé publique et la clé privée. Il a utilisé la clé privée pour chiffrer le message. Comme je connais la clé publique, je peux facilement déchiffrer le message chiffré pour obtenir le flag.

La solution est dans le fichier `solve.py`.