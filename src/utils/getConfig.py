import json
def getConfig():

    with open("./src/utils/config.json") as f:
        config = json.load(f)
    return config 
