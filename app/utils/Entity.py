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
            "health": 10,
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
            "attackRange": 100,
            "attackDamage": 100,
            "skins": [
                ["normal_right", "spike", False],
                ["normal_left", "spike", False]
            ]
        }
    }
    return properties[mobName]

def getEntitiesForStage(stageID):
    stageEntities = {
        "stage1": [
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
        ]
    }
    return stageEntities[stageID]

def getEntityID(sprite):
    if hasattr(sprite, "entityType"):
        return sprite.entityType
    elif sprite.Player:
        return "player"
    else:
        return None
