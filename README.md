# Projet - Trophées NSI

Notre projet pour le concours de Trophées NSI 2025-2026.

# Instructions de dev : 

__L'organisation des fichiers :__

Tous les ressources du jeu dans `/assets` : \
Sprites, scènes, sons, etc. rangés par sous-catégories.

Tous les programmes des éléments dans `/app/components` :\
Niveaux, joueur, entités, etc. également dans de sous-catégories.

Le dossier racine ne doit contenir que le `main.py` et le fichier `README.md`, et éventuellement d'autres fichier généraux concernant le projet en général, et non des éléments précis.

\
__La gestion du dépôt Github__

**Ne jamais coder directement dans la branche `main`:**\
Celle-ci ne contient que des versions fonctionelles et stables du jeu, ainsi elle est mise à jour de manière ponctuelle dès que le jeu est fonctionnel et sans bug.

**L'endroit où coder est la branche `dev`:**\
Cette branche est faites exprès pour développer le jeu, introduire les fonctionnalités, etc. C'est sur cette branche que vous faites vos modifications.

En cas de grosse modifications/modifications expérimentale, une branche exprès sera faite pour pouvoir bricoler dedans tranquillement. 

\
__Les commits (modifications)__

Il est essentiel de faire les modifications implicant plusieurs fichiers en un seul commit contenant l'ensemble des modifications, afin de faciliter le retour en arrière ou la consultation des modifications apportées, et vérifier leur fonctionnement de manière indépendante. 

Pour les messages de commit, le format ci-dessous est privilégié :

```
type(sujet): action qui est faite
```

Ainsi, le type peut être :
* `fix`, c'est-à-dire la correction d'un bug, d'une erreur ou l'amélioration apportée à un élément
* `feat`, c'est-à-dire l'ajout d'une _feature_ (fonctionnalité) dans le jeu.

Le sujet, s'il y en a un précisément, correspond à ce qui subit l'action, c'est à dire la partie ou le système qui reçoit la modification.

Et l'action commence par un verbe. De préférence et par convention, les commits sont en anglais.

En sautant des lignes lors de l'entrée du commit, vous pouvez ajouter une description au commit pour donner des détails sur les changement, expliquer ce qu'ils impliquent, etc.

Example :

```
feat(player): add a health bar to the player
```

__Ajout d'une fonctionnalité__

Si une fonctionnalité similaire existe déjà, lors de l'implémetation d'un nouvel élément il est utile de **réutiliser le code déjà existant**, en le copiant dans le nouvel élément afin de garder la même structure de code. 

Exemple, lord de l'implémentation d'un nouveau mob, vous pouvez réutiliser la majeure partie d'un mob préexistant pour garder la même logique de fonctionnement et la même structure, facilitant le développement grâce à la claireté du code.