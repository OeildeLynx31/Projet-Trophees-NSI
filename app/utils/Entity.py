def getProperties(mobName):
    properties = {
        "zombush": {
            "name": "Zombush",
            "living": True,
            "physical": False,
            "immortal": False,
            "textW": 32,
            "textH": 32,
            "points": 50,
            "growFactor": 3,
            "hitboxW": 20,
            "hitboxH": 32,
            "walkingSpeed": 3,
            "jumpHeight": 4,
            "canJump": True,
            "fallInVoid": False,
            "health": 20,
            "maxPlayerDistance": 500,
            "minPlayerDistance": 100,
            "attackRange": 50,
            "attackDamage": 5,
            "skins": [
                ["normal_right", "zombush", False],
                ["normal_left", "zombush", True],
                ["walk_right1", "zombush2", False],
                ["walk_left1", "zombush2", True],
                ["walk_right2", "zombush3", False],
                ["walk_left2", "zombush3", True],
            ]
        },
        "champoline": {
            "name": "Champoline",
            "living": False,
            "physical": True,
            "immortal": False,
            "textW": 32,
            "textH": 16,
            "growFactor": 3,
            "hitboxW": 32,
            "hitboxH": 12,
            "skins": [
                ["normal_right", "champoline", False],
            ]
        },
        "crate": {
            "name": "Crate",
            "living": False,
            "destructible": True,
            "health": 20,
            "points": 10,
            "physical": True,
            "immortal": False,
            "textW": 9,
            "textH": 9,
            "growFactor": 5,
            "hitboxW": 9,
            "hitboxH": 9,
            "skins": [
                ["normal_right", "crate1", False],
            ]
        },
        "vines": {
            "name": "Vines",
            "living": False,
            "physical": False,
            "immortal": False,
            "textW": 16,
            "textH": 32,
            "growFactor": 4,
            "hitboxW": 8,
            "hitboxH": 32,
            "skins": [
                ["normal_right", "vines", False],
            ]
        },
        "minirock":{
            "name": "MiniRock",
            "living": True,
            "physical": False,
            "immortal": False,
            "textW": 20,
            "textH": 20,
            "points": 30,
            "growFactor": 4,
            "hitboxW": 12,
            "hitboxH": 18,
            "walkingSpeed": 2,
            "jumpHeight": 4,
            "canJump": True,
            "fallInVoid": False,
            "health": 20,
            "maxPlayerDistance": 150,
            "minPlayerDistance": 100,
            "attackRange": 50,
            "attackDamage": 4,
            "skins": [
                ["normal_right", "minirock", False],
                ["normal_left", "minirock", True],
                ["walk_right1", "minirock2", False],
                ["walk_left1", "minirock2", True],
                ["walk_right2", "minirock3", False],
                ["walk_left2", "minirock3", True],
            ]
        },
        "grolem":{
            "name": "Grolem",
            "living": True,
            "physical": False,
            "immortal": False,
            "textW": 46,
            "textH": 35,
            "points": 100,
            "growFactor": 5,
            "hitboxW": 24,
            "hitboxH": 24,
            "walkingSpeed": 2,
            "jumpHeight": 4,
            "canJump": False,
            "fallInVoid": False,
            "health": 40,
            "maxPlayerDistance": 400,
            "minPlayerDistance": 100,
            "attackRange": 100,
            "attackDamage": 10,
            "skins": [
                ["normal_right", "grolem", False],
                ["normal_left", "grolem", True],
                ["walk_right1", "grolem2", False],
                ["walk_left1", "grolem2", True],
                ["walk_right2", "grolem3", False],
                ["walk_left2", "grolem3", True],
            ]
        },
        "spike":{
            "name": "Spike",
            "living": True,
            "physical": False,
            "immortal":True,
            "textW": 16,
            "textH": 4,
            "growFactor": 8,
            "hitboxW": 16,
            "hitboxH": 3,
            "walkingSpeed": 0,
            "jumpHeight": 0,
            "canJump": False,
            "fallInVoid": False,
            "health": 4000,
            "maxPlayerDistance": 400,
            "minPlayerDistance": 100,
            "attackRange": 200,
            "attackDamage": 100,
            "touchKill": True,
            "skins": [
                ["normal_right", "spike", False],
                ["normal_left", "spike", False]
            ]
        },
        "secretwall1": {
            "name": "SecretWall1",
            "living": False,
            "destructible": True,
            "health": 1,
            "physical": False,
            "immortal": False,
            "textW": 16,
            "textH": 16,
            "growFactor": 4,
            "hitboxW": 16,
            "hitboxH": 16,
            "skins": [
                ["normal_right", "secretwall1", False],
            ]
        },
        "secretwall2": {
            "name": "SecretWall2",
            "living": False,
            "destructible": True,
            "health": 1,
            "physical": False,
            "immortal": False,
            "textW": 16,
            "textH": 16,
            "growFactor": 4,
            "hitboxW": 16,
            "hitboxH": 16,
            "skins": [
                ["normal_right", "secretwall2", False],
            ]
        },
        "florift": {
            "name": "Florift",
            "living": False,
            "physical": False,
            "immortal": True,
            "textW": 16,
            "textH": 16,
            "growFactor": 4,
            "hitboxW": 16,
            "hitboxH": 16,
            "skins": [
                ["normal_right", "fleurtp", False],
            ]
        },
    }
    return properties[mobName]

def getEntitiesForStage(stageID):
    stageEntities = {
        "stage1": [
            {"id": "florift", "pos": [700, 460]},
            {"id": "florift", "pos": [1300, 300]},
            {"id": "zombush", "pos": [1600, 300]},
            {"id": "champoline", "pos": [1100, 550]},
            {"id": "vines", "pos": [1450, 460]},
            {"id": "crate", "pos": [400, 520]}
        ],
        "stage2": [
            {"id": "champoline", "pos": [1260, 550]},
            {"id": "champoline", "pos": [2270, 404]},
            {"id": "vines", "pos": [1476, 276]},
            {"id": "vines", "pos": [1870, 128]},
            {"id": "minirock", "pos": [2050, 212]},
            {"id": "minirock", "pos": [1420, 506]},      
            {"id": "minirock", "pos": [3120, 260]},   
            {"id": "grolem", "pos": [900, 420]},
            {"id": "crate", "pos": [1680, 488]},
            {"id": "crate", "pos": [3220, 583]},
            {"id": "spike", "pos": [1792, 628]},
            {"id": "spike", "pos": [1840, 628]},
            {"id": "spike", "pos": [1888, 628]},
            {"id": "spike", "pos": [1936, 628]},
            {"id": "spike", "pos": [1984, 628]},
            {"id": "spike", "pos": [2032, 628]},
            {"id": "spike", "pos": [2080, 628]},
            {"id": "spike", "pos": [2128, 628]},
            {"id": "spike", "pos": [2176, 628]},
            {"id": "spike", "pos": [2224, 628]},
            {"id": "spike", "pos": [2272, 628]},
            {"id": "spike", "pos": [2320, 628]},
            {"id": "spike", "pos": [2368, 628]},
            {"id": "spike", "pos": [2752, 372]},
            {"id": "spike", "pos": [2822, 372]},
            {"id": "secretwall1", "pos": [3264, 500]},
            {"id": "secretwall1", "pos": [3264, 564]},
            {"id": "secretwall2", "pos": [3200, 500]},
            {"id": "secretwall2", "pos": [3200, 564]},
        ],
        "stage3": [
            # === ZONE 1 — Départ (x 200-700) : pression immédiate ===
            # Deux minirock au sol dès le spawn
            {"id": "minirock",   "pos": [280,  540]},
            {"id": "minirock",   "pos": [500,  540]},
            # Crate accessible facilement pour encourager le joueur
            {"id": "crate",      "pos": [350,  540]},
            # Spikes au sol entre les minirock — oblige à sauter
            {"id": "spike",      "pos": [420,  620]},
            {"id": "spike",      "pos": [468,  620]},

            # === ZONE 2 — Première montée (x 700-1200) ===
            # Grolem sur plateforme basse, bloque la progression principale
            {"id": "grolem",     "pos": [800,  420]},
            # Vines sur la plateforme haute — ralentit le passage
            {"id": "vines",      "pos": [950,  210]},
            # Minirock sur la plateforme haute — piège le joueur qui monte
            {"id": "minirock",   "pos": [1050, 210]},
            # Florift paire A — téléporte vers la zone 4 (récompense pour les explorateurs)
            {"id": "florift",    "pos": [900,  360]},
            {"id": "florift",    "pos": [2600, 340]},
            # Champoline cachée sous la plateforme haute pour aider à monter
            {"id": "champoline", "pos": [870,  470]},

            # === ZONE 3 — Passage de spikes (x 1200-1700) ===
            # Long couloir de spikes au sol — doit tout passer en sautant
            {"id": "spike",      "pos": [1250, 620]},
            {"id": "spike",      "pos": [1298, 620]},
            {"id": "spike",      "pos": [1346, 620]},
            {"id": "spike",      "pos": [1394, 620]},
            {"id": "spike",      "pos": [1442, 620]},
            {"id": "spike",      "pos": [1490, 620]},
            {"id": "spike",      "pos": [1538, 620]},
            {"id": "spike",      "pos": [1586, 620]},
            # Zombush sur plateforme intermédiaire au milieu des spikes
            {"id": "zombush",    "pos": [1380, 360]},
            {"id": "zombush",    "pos": [1520, 360]},
            # Champoline au début des spikes pour aider le saut
            {"id": "champoline", "pos": [1220, 500]},
            # Crate au-dessus des spikes — récompense pour ceux qui restent en hauteur
            {"id": "crate",      "pos": [1450, 330]},

            # === ZONE 4 — Plateforme centrale (x 1700-2300) : cœur du level ===
            # Grolem sur plateforme haute — gardien central
            {"id": "grolem",     "pos": [1800, 210]},
            # Minirock au sol en contrebas
            {"id": "minirock",   "pos": [1900, 540]},
            {"id": "minirock",   "pos": [2100, 540]},
            # Spikes sur plateforme intermédiaire — piège pour ceux qui descendent
            {"id": "spike",      "pos": [1970, 370]},
            {"id": "spike",      "pos": [2018, 370]},
            {"id": "spike",      "pos": [2066, 370]},
            # Vines sur plateforme haute — ralentit l'approche du grolem
            {"id": "vines",      "pos": [1750, 120]},
            # Crate cachée sur plateforme très haute
            {"id": "crate",      "pos": [2200, 210]},
            # Florift paire B — téléporte au-dessus de la zone finale
            {"id": "florift",    "pos": [2000, 200]},
            {"id": "florift",    "pos": [3100, 190]},

            # === ZONE 5 — Avant-dernière (x 2300-2900) ===
            # Duo grolem + zombush qui se cumulent — très dangereux
            {"id": "grolem",     "pos": [2400, 540]},
            {"id": "zombush",    "pos": [2550, 540]},
            {"id": "zombush",    "pos": [2700, 540]},
            # Spikes sur les plateformes latérales — coupe les chemins alternatifs
            {"id": "spike",      "pos": [2480, 370]},
            {"id": "spike",      "pos": [2528, 370]},
            {"id": "spike",      "pos": [2576, 370]},
            {"id": "spike",      "pos": [2624, 370]},
            # Minirock en hauteur — attaque depuis au-dessus
            {"id": "minirock",   "pos": [2800, 210]},
            {"id": "minirock",   "pos": [2900, 210]},
            # Champoline pour atteindre les plateformes hautes
            {"id": "champoline", "pos": [2360, 470]},

            # === ZONE 6 — Finale (x 2900-3700) : gauntlet ===
            # Grolem + minirock simultanément — boss de fin
            {"id": "grolem",     "pos": [3000, 540]},
            {"id": "grolem",     "pos": [3200, 540]},
            {"id": "minirock",   "pos": [3050, 340]},
            {"id": "minirock",   "pos": [3150, 340]},
            {"id": "minirock",   "pos": [3300, 340]},
            # Couloir de spikes final au sol — dernière épreuve
            {"id": "spike",      "pos": [3350, 620]},
            {"id": "spike",      "pos": [3398, 620]},
            {"id": "spike",      "pos": [3446, 620]},
            {"id": "spike",      "pos": [3494, 620]},
            {"id": "spike",      "pos": [3542, 620]},
            # Zombush gardien de la sortie
            {"id": "zombush",    "pos": [3600, 540]},
            {"id": "zombush",    "pos": [3650, 540]},
            # Crate récompense juste avant la sortie
            {"id": "crate",      "pos": [3500, 540]},
        ],
    }
    return stageEntities[stageID]

def getEntityID(sprite):
    if hasattr(sprite, "entityType"):
        return sprite.entityType
    elif sprite.Player:
        return "player"
    else:
        return None
