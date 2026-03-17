# Smolkkey

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2025

## Description

On a un chiffrement RSA du flag avec un exposant utilisé qui est de **3**. Le code du challenge est présent dans le fichier `smolkkey.py`.

## Write-Up

Comme l'exposant est très petit, on peut penser que le message original est petit également. Dans ce cas, le chiffrement RSA peut être vulnérable à une attaque de racine cubique. On va donc calculer la racine cubique et retrouver le flag.

La solution est présente dans le fichier `solve.py`

## Flag

FCSC{30f7c4b2fa7f0fb48bfbd9bbd413491c0a6da660764961b862fe38a83b4bc00f}