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
            "skins": [
                ["normal_right", "zombush", False],
                ["normal_left", "zombush", True],
                ["walk_right1", "zombush-walk", False],
                ["walk_left1", "zombush-walk", True],
                ["walk_right2", "zombush-walk2", False],
                ["walk_left2", "zombush-walk2", True],
            ]
        },
    }
    return properties[mobName]