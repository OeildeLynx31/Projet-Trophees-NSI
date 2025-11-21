def getProperties(mobName):
    properties = {
        "zombush": {
            "name": "Zombush",
            "living": True,
            "textW": 32,
            "textH": 32,
            "growFactor": 2,
            "hitboxW": 20,
            "hitboxH": 32,
            "walkingSpeed": 5,
            "jumpHeight": 4,
            "health": 20,
        }
    }
    return properties[mobName]