# Projet - Trophées NSI 2025-2026

## Présentation du Projet
Ce projet est un moteur de jeu de plateforme et d'action développé en Python avec la bibliothèque **Pygame**. Il a été conçu dans le cadre du concours des Trophées NSI.

Le joueur incarne un personnage évoluant dans différents niveaux (stages), affrontant des ennemis avec une IA propre, explorant des environnements riches en interactions.
L'arbre monde se meurt et le joueur doit s'enfoncer dans les profondeurs pour en trouver la cause et ainsi protéger l'écosystème et la nature aux alentours de l'arbre.

## Équipe
Développé par l'équipe de Première NSI au lycée Emilie de Rodat, Toulouse.
Jules: design des assets (décors et éléments), anim maker, co-création de la vision du jeu, level designer
Valentin: design des assets (entités), anim maker, co-création de la vision de jeu
Vincent: Programmation globale
Ewenn: Aide à la programmation
Collaboration via serveur discord pour la répartition des tâches
Temps de travail estimé: 90h

## Etapes du projet

Tout d'abord, choix du gameplay --> combat dynamique en temps réel
Puis, création de l'Univers et du Lore (pas encore intégralement implémenté)
Design des premiers assets, le joueur et de ses premières animations.
Ensuite, création du moteur de jeu
Implémentation du reste des assets + ajout de features progressivement.

## Caractéristiques Techniques
- **Moteur de jeu sur mesure** développé en Python.
- **Système de stages** dynamique permettant une transition fluide entre les niveaux.
- **Gestion d'entités** : ennemis (Grolem, Zombush, MiniRock), objets interactifs (Crates, Champolines, Florifts).
- **Effets visuels** : Système de particules et filtres d'image (ex: effet de dégâts).
- **Sauvegarde et paramètres** : Gestion des paramètres (volume, sensibilité) et des sauvegardes via fichiers CSV.

## Validation de l'opérationnalité et du fonctionnement

Avancement général : non terminé, le projet actuel peut-être vu comme une démo ou une beta, plus de contenu pourra et sera rajouté ultérieurement.
Le code fonctionne sans erreur, depistage de bugs à l'aide de game testers tout au long du projet.
Pas de problèmes majeurs, mais une succession de problèmes mineurs rapidement réglés.

## Ouverture

Certains systèmes n'ont pas été finalisés (comme l'inventaire), certains assets notamment les entités sont encore grossières, il n'y a que 2 salles.
Avec du temps supplémentaire, nous comptons rajouter tout d'abord d'autres salles puis d'autres biomes afin de pouvoir appliquer tout l'univers et l'histoire que nous avons conçu pour ce jeu.
Nous aurions également pu améliorer le système d'objets (et donc d'inventaire), rajouter éventuellement du leveling, etc...
Ce projet nous a appris comment répartir les rôles selon nos compétences respectives, il nous a aussi formé sur la collaboration sur un projet de groupe de longue durée, avec donc les désaccords qui l'accompagnent.
Pour ma part, avec Valentin, nous avons appris à maitriser des outils jusqu'alors inconnus pour la création de pixel art et nous nous sommes confronté aux choix de direction et de game design qui ne sont pas toujours évident.
Du côté de Vincent et Ewenn je pense que ça a été également formateur pour eux afin d'arriver à un haut niveau de maitrise de la bibliothèque pygame sur un projet d'envergure.

**Veuillez trouver les inspirations et/ou informations concernant l'utilisation d'aide de tiers dans `./docs/credits.md`**

*Plus d'informations dans la section ABOUT implémentée directement dans le jeu*
