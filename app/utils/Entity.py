def getProperties(mobName):
    properties = {
        "zombush": {
            "name": "Zombush",
            "living": True,
            "physical": False,
            "textW": 32,
            "textH": 32,
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
            "physical": True,
            "textW": 9,
            "textH": 9,
            "growFactor": 4,
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
            "textW": 16,
            "textH": 32,
            "growFactor": 4,
            "hitboxW": 8,
            "hitboxH": 32,
            "skins": [
                ["normal_right", "vines", False],
            ]
        }
        
    }
    return properties[mobName]

def getEntitiesForStage(stageID):
    stageEntities = {
        "stage1": [
            {"id": "zombush", "pos": [1600, 300]},
            {"id": "champoline", "pos": [1100, 360]},
            {"id": "vines", "pos": [1450, 233]},
            {"id": "crate", "pos": [600, 560]}
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
