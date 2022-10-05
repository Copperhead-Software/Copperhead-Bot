import json, os
import interactions

server_data = {}
global DefData
DefData = {"subscribed": True, "mints": -1, "analysis": -1, "license": True, "Akey": "key"} # fix this when key system is implimented

def Csave():
    with open(f"configs.json", 'w') as fl:
        json.dump(server_data, fl, indent=2)

def Cload(guild):
    DefData = {"subscribed": True, "mints": -1, "analysis": -1, "license": True, "Akey": "key"} # fix this when key system is implimented
    if os.path.exists(f"configs.json"):
        with open(f'configs.json', 'r') as fl:
            loaded = json.load(fl)
            if f"{guild.id}" in loaded:
                DefData = loaded[f"{guild.id}"]
    else:
        with open(f'configs.json', 'w') as fl:
            json.dump(DefData, fl)

    return DefData

def embed(title: str = None, *, body: str, footer = None, color = 0x00ff00):
    """embed builder"""
    embed = interactions.Embed(title=title, description=body, footer=footer, color=color)
    return embed
