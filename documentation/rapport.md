---
title: Résolution de Rubik's Cube
subtitle: Traîtement d'image
lang: fr
author:
- Bulloni Lucas <lucas.bulloni@he-arc.ch>
- Fleury Malik <malik.fleury@he-arc.ch>
- Wermeille Bastien <bastien.wermeille@he-arc.ch>
date: \today
pagesize: A4
numbersections: true
documentclass: scrartcl
geometry: margin=2.5cm
bibliography: rapport.bib
header-includes: |
      \usepackage{fancyhdr}
      \pagestyle{fancy}
      \fancyhead[R]{Lucas Bulloni, Malik Fleury \& Bastien Wermeille}
      \usepackage{float}
      \floatplacement{figure}{H}
---

\newpage

\tableofcontents

\newpage

# Introduction

# Configuration d'exécution

Pour la bonne exécution du programme, il vous installer le matériel **dans** la manière optimale.

## Matérielle nécessaire

- Caméra
- Rubik's cube
- *Optionnel :* Lampe

La lampe permet d'avoir un meilleur résultat pour la détection de la position du cube et la détection des couleurs.

Le but de ce projet était la réalisation d'une application permettant la détection d'un rubik's cube, sa reconnaissance ainsi que sa résolution avec affiche de celui-ci à travers un model 3D. Ce projet a été réalisé dans le cadre du cours "Traitemen d'image" à la He-Arc.

# Configuration du programme

Ce programme nécessite un certain nombre de package python. Nous avons utilisé un `venv` durant le dévelopement afin de faciliter l'intallation. Le fichier `requirements.txt` contient la liste des dépendances, pour créer le venv et installer celles-ci sur un système linux, vous pouvez executer les lignes de commandes suivantes. 

```sh
TODO: Ajouter VENV command lines
```

En ce qui concerne les dépendances externes, il est nécessaire d'installer la bibliothèque:
- kociemba

Installable de la manière suivante :

```sh
sudo apt install kociemba
```

# Fonctionnement et Architecture

Ce projet a été séparé en 5 étapes distinctes qui sont les suivantes:

1. Détection d'une face du rubik's cube
2. Reconnaissance des couleurs de la face
3. Reconstruction du rubik's cube valide à partir des 6 faces scannées dans n'importe quel ordre
4. Résolution du rubik's cube
5. Affichage du rubik's cube en 3D

## Détection d'une face du rubik's cube


TODO: Bastien

## Reconnaissance des couleurs d'une face

TODO: Lucas

## Reconstruction du rubik's cube

Les deux étapes précédentes permettant d'isoler chaque face et de reconnaitre leurs différentes couleurs, l'étape suivante était de remettre dans l'ordres les différentes faces du cube afin que celui-ci soit valide.

Cette étape consistait en deux points essentiels:
1. Détecter si l'ensemble des faces permettaient de reconstruire un  rubik's cube valide
2. Reconstruire le rubik's cube

Lors du développement nous avons écris nos propres tests afin de tester si le cube était valide notemment en comptant le nombre de couleurs totales mais celà ne suffisait pas alors nous avons décider d'utiliser la bibliothèque `kociemba` permettant de valider si un rubik's cube était valide.

Une fois la possibilité de pouvoir tester si un rubik's cube était valide, il nous restait à trouver comment agencer les différentes faces.

Après un certains nombre de tests avec la bibliothèque pour vérifier la validité du cube, nous nous sommes rendu compte que cette méthode était extrêmement rapide et que le meilleur moyen de trouver la bonne configuration était de proposer chaque solution à notre fonction.

Cette opération peut paraître conteuse mais le nombre de cas à tester est très petit: `4*4*4*4*4*4 = 5096`. Ce calcul découle du fait que le point central de chaque face ne bouge jamais et donc que nous savons quelles faces sont adjacentes. Il ne nous reste plus qu'à tester le composition des 4 rotations possibibles de chaque faces. Tester ces 4096 possibilités est extrêment rapide et dès que la solution est trouvée, le processus s'arrête. Il n'existe qu'une seule possibilité d'assemblage des différentes faces pour chaque cube. Le seul cas ou on peut avoir plusieurs faces valides est lorsque une face du rubik's cube est uniforme ou lorsqu'elle est symétrique.

## Résolution du rubik's cube

La résolution du rubik's n'a pas étée développée par nos soins car ce travail n'était pas le point central du projet. Nous avons utilisé l'algporithme de Kociemba afin d'effectuer cette étape.

Le code nécessaire a cette partie est relativement simple et est le suivant:
```python
import kociemba
solution = kociemba.solve(cube)
```

La variable cube étant une string définissant l'état du cube par exemple:
- `BBRUUUUDFBRUURRBBDLFFFFFRFBDLFDDDFDDLBDLLLRLRLBUUBRURL`.

## Affichage du rubik's cube en 3D

TODO: Malik

# Utilisation



# Méthode et solution



# Résultats



# Conclusion

\newpage

\listoffigures

# References