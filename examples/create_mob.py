slime_properties = {
    "slime": {
        "name": "Slime Vert",        # Nom affiché (ex: pour les logs ou interface)
        "living": True,              # True = possède une IA et peut mourir
        "physical": False,           # True = le joueur peut marcher dessus et entrer en collision
        "immortal": False,           # Si True, ne prend pas de dégâts
        "textW": 32, "textH": 32,    # Taille d'origine de l'image (en pixels)
        "growFactor": 2,             # Multiplicateur de taille
        "hitboxW": 20, "hitboxH": 20,# Taille de la zone de collision
        "health": 10,                # Points de vie
        "points": 25,                # Score donné au joueur à sa mort
        "walkingSpeed": 2,           # Vitesse de déplacement
        "jumpHeight": 3,             # Force de saut
        "canJump": True,             # L'IA peut-elle sauter les obstacles ?
        "fallInVoid": False,         # L'IA évite-t-elle de tomber dans les trous ?
        "maxPlayerDistance": 400,    # Distance à laquelle il commence à poursuivre
        "minPlayerDistance": 50,     # Distance d'arrêt
        "attackRange": 40,           # Distance de déclenchement de l'attaque
        "attackDamage": 2,           # Dégâts infligés au joueur
        "skins": [
            # [Nom du costume, Nom du fichier image (sans .png/.jpg), Miroir horizontal]
            ["normal_right", "slime_idle", False], 
            ["normal_left", "slime_idle", True],
        ]
    }
}

def example_placement():
    return {
        "id": "slime",      # Doit correspondre à la clé définie à l'Étape 1
        "pos": [1200, 500]  # Coordonnées X, Y dans le niveau
    }