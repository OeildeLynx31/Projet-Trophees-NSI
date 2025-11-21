def getProperties(mobName):
    properties = {
        "zombush": {
            "name": "Zombush",
            "living": True,
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
        },
    }
    return properties[mobName]