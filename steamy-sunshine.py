import json
import re
import os


WINDOWS_STEAMAPPS_DIR = "C:\\Program Files (x86)\\Steam\\steamapps\\"
APPS_WINDOWS_JSON_FILEPATH = "C:\\Sunshine-Windows\\assets\\apps_windows.json"

EXCLUDE_APPIDS = []

apps_windows_json = {
    "env": {"PATH": "$(PATH);C:\\Program Files (x86)\\Steam"},
    "apps": []
}

for item in os.listdir(WINDOWS_STEAMAPPS_DIR):
    if item.endswith(".acf"):
        app_manifest = open(f"{WINDOWS_STEAMAPPS_DIR}{item}").readlines()
        game = {}

        for line in app_manifest:
            if "name" in line:
                game["name"] = re.sub(
                    r"[^A-Za-z0-9 ]",
                    "",
                    re.sub(
                        "\t\"name\"\t",
                        "",
                        line
                    )
                )
            if "appid" in line:
                game["appid"] = re.sub(
                    r"[^\d]",
                    "",
                    line
                )

        if game["appid"] not in EXCLUDE_APPIDS:
            game["output"] = ""
            game["detached"] = [f"steam steam://rungameid/{game.pop('appid')}"]
            game["image-path"] = ""
            apps_windows_json["apps"].append(game)

with open(APPS_WINDOWS_JSON_FILEPATH, "w") as f:
    f.write(json.dumps(apps_windows_json, indent=4))
