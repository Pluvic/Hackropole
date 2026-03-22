# A l'aise

## Spécification

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2022

## Description

Cette épreuve vous propose de déchiffrer un message chiffré avec la méthode inventée par [Blaise de Vigénère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re). La clé est `FCSC` et le message chiffré est :

```
Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.
```

Le flag est le nom de la ville mentionnée dans ce message.

## Write-Up

La description parle d'elle même, pour retrouver le flag il s'agit d'appliquer le chiffrement de Vigenère sur ce chiffre ci dessus en utilisant la clé `FCSC`. Cela peut être réalisé de plusieurs manière: 
- Soit en utilisant directement un outil en ligne comme https://www.dcode.fr/chiffre-vigenere
- Soit en réalisant un script en python (ou autre langage)