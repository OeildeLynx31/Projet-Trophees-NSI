from .Storage import initFile, readFile, writeFile

def loadSettings():
    settings = {}
    initFile('settings', headers=['name', 'value'], data=[])
    try:
        settingsData = readFile('settings')
        if settingsData and len(settingsData) > 0:
            for row in settingsData:
                key = row.get('name', '').strip()
                value = row.get('value', '').strip()
                if key:
                    try:
                        settings[key] = int(value)
                    except ValueError:
                        try:
                            settings[key] = float(value)
                        except ValueError:
                            settings[key] = value
            print(f"Loaded {len(settingsData)} setting(s) from storage")
        else:
            print("No settings found in storage, using defaults")
            settings = getDefaults()
    except Exception as e:
        print(f"Could not load settings from storage: {e}, using defaults")
    return settings

def getDefaults():
    return {
        "volume": 100,
    }

def saveSettings(settings):
    try:
        settingsArray = []
        for key in settings.keys():
            settingsArray.append({"name": key, "value": settings[key]})
        writeFile("settings", settingsArray)
    except Exception as e:
        print(f"Error saving settings: {e}")