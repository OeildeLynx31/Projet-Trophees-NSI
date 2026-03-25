# Projet - Trophées NSI

Notre projet pour le concours de Trophées NSI 2025-2026.
Instructions aux devs pour la coordination du projet

# Instructions de dev : 

__L'organisation des fichiers :__

- `/sources` : Contient tout le code source du jeu.
  - `/sources/engine` : Le moteur du jeu (boutons, collisions, particules, etc.).
  - `/sources/entities` : Définitions des entités.
  - `/sources/stages` : Les différents niveaux du jeu.
- `/assets` : Toutes les ressources (images, sons, polices).
- `/data` : Données du jeu (sauvegardes, paramètres en CSV).
- `/docs` : Documentation du projet.
- `/examples` : Exemples d'utilisation ou de scripts annexes.
- `/main.py` : Point d'entrée du programme.

__La gestion du dépôt Github__

**Ne jamais coder directement dans la branche `main`:**\
Celle-ci ne contient que des versions fonctionelles et stables du jeu. Elle est mise à jour de manière ponctuelle dès que le jeu est fonctionnel et sans bug.

**L'endroit où coder est la branche `dev`:**\
Cette branche est faite exprès pour développer le jeu, introduire les fonctionnalités, etc. C'est sur cette branche que les modifications doivent êtres faites.

__Les commits (modifications)__

Il est essentiel de faire les modifications implicant plusieurs fichiers en un seul commit contenant l'ensemble des modifications, afin de faciliter le retour en arrière ou la consultation des modifications apportées, et vérifier leur fonctionnement de manière indépendante. 

Pour les messages de commit, le format ci-dessous est privilégié:

```
type(sujet): action qui est faite
```

Ainsi, le type peut être :
* `fix`, c'est à dire la correction d'un bug, d'une erreur ou l'amélioration apportée à un élément
* `feat`, c'est à dire l'ajout d'une feature (fonctionnalité) dans le jeu.

Le sujet (s'il y a lieu d'en préciser un) correspond à ce qui subit l'action, c'est à dire la partie ou le système qui reçoit la modification.

L'action commence par un verbe. Par convention, les commits sont en anglais.


Exemple :

```
feat(player): add a health bar to the player
```

__Ajout d'une fonctionnalité__

Si une fonctionnalité similaire existe déjà, lors de l'implémetation d'un nouvel élément il est utile de **réutiliser le code déjà existant**, en le copiant dans le nouvel élément afin de garder la même structure de code.