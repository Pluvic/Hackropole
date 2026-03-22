# Carotte Radis Tomate

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2025

## Description

Mangez cinq fruits et légumes par jour !

Le challenge peut être retrouvé dans le fichier `carotte-radis-tomate.py`. Le ficher applique 5 opérations de modulo sur la clé de chiffrement en utilisant des modulos différents. J'ai accès à tous les résultats de ces opérations, ainsi qu'à la clé chiffrée.

## Write-Up

Pour résoudre ce challenge, nous allons utiliser les résultats des opérations de modulo pour trouver la clé de chiffrement. Pour se faire, nous allons utiliser le théorème des restes chinois, qui nous permet de résoudre un système de congruences.

Le fichier `solve.py` contient le code pour résoudre ce système de congruences.