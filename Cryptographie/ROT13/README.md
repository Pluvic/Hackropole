# ROT13

## Specifications

**Catégorie**: Cryptographie

**Difficulté estimée**: Intro

**Année**: 2023

## Description

Un de vos collègues ne jure que par cette méthode de chiffrage révolutionnaire appelée rot13.

Il l’a utilisée pour dissimuler un flag dans ce texte. Démontrez-lui qu’il a tort de supposer que cet algorithme apporte une quelconque notion de confidentialité !

```
GBQB yvfgr :
- Cnva (2 onthrggrf)
- Ynvg (1 yvger)
- Pbevnaqer (fhegbhg cnf, p'rfg cnf oba)
- 4 onanarf, 4 cbzzrf, 4 benatrf
- Cbhyrg (4 svyrgf qr cbhyrg)
- 1 synt : SPFP{rq24p7sq86p2s0515366}
- Câgrf (1xt)
- Evm (fnp qr 18xt)
- Abheve zba qvabfnher
```


## Write-Up

Pour résoudre ce challenge, il suffit d'appliquer la transformation rot13 au texte donné. La transformation rot13 remplace chaque lettre par la lettre située 13 positions plus loin dans l'alphabet, en bouclant à partir de 'z' vers 'a'. Pour se faire, on peut utiliser l'outil `CyberChef` ou un script Python simple.