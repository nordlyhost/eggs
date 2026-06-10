#!/usr/bin/env python3
"""
Nordly Paper egg customizer.

Adds the 9 Nordly Startup-tab variables, extends config.files server.properties
parser rules, and modifies install script to drop a NORDLY-WELCOME.md file.

Idempotent: safe to re-run. Will replace existing Nordly variables/rules if present.
"""

import json
import sys
from pathlib import Path

INPUT = Path("/home/claude/egg-paper-nordly.json")
OUTPUT = Path("/home/claude/egg-paper-nordly.json")  # in-place

# ---------------------------------------------------------------------------
# The 9 new variables to expose in the Pelican Startup tab.
# Sort values start at 10 to appear below the existing 4 variables (sort 1-4).
# Rules use array format (Pelican beta34 doesn't accept pipe-separated strings).
# ---------------------------------------------------------------------------
NORDLY_VARS = [
    {
        "name": "Server MOTD",
        "description": "The message of the day shown in the Minecraft server list. "
                       "Supports Minecraft color codes (§a green, §c red, §l bold, §r reset).",
        "env_variable": "MOTD",
        "default_value": "\u00a7a\u00a7lHosted by Nordly \u00a7r\u00a77\u00b7 \u00a7fnordly.gg",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "string", "max:200"],
        "sort": 10,
    },
    {
        "name": "Enable Whitelist",
        "description": "When enabled, only players in the whitelist can join. "
                       "Add players in the Console tab: /whitelist add <username>. "
                       "Nordly default: enabled for new server security.",
        "env_variable": "WHITELIST",
        "default_value": "true",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "string", "in:true,false"],
        "sort": 11,
    },
    {
        "name": "Online Mode",
        "description": "Require premium (paid) Minecraft accounts. "
                       "Strongly recommended on. Disabling allows cracked/pirated clients but enables account spoofing attacks.",
        "env_variable": "ONLINE_MODE",
        "default_value": "true",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "string", "in:true,false"],
        "sort": 12,
    },
    {
        "name": "Difficulty",
        "description": "World difficulty level.",
        "env_variable": "DIFFICULTY",
        "default_value": "easy",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "string", "in:peaceful,easy,normal,hard"],
        "sort": 13,
    },
    {
        "name": "Game Mode",
        "description": "Default game mode for new players.",
        "env_variable": "GAMEMODE",
        "default_value": "survival",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "string", "in:survival,creative,adventure,spectator"],
        "sort": 14,
    },
    {
        "name": "Max Players",
        "description": "Maximum concurrent players. Set based on your plan's slot allocation.",
        "env_variable": "MAX_PLAYERS",
        "default_value": "20",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "integer", "min:1", "max:200"],
        "sort": 15,
    },
    {
        "name": "PvP",
        "description": "Allow player vs player combat.",
        "env_variable": "PVP",
        "default_value": "true",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "string", "in:true,false"],
        "sort": 16,
    },
    {
        "name": "View Distance",
        "description": "Render distance in chunks. Higher = more visible terrain but more server load. "
                       "Recommended: 8-12 for shared, 12-16 for dedicated.",
        "env_variable": "VIEW_DISTANCE",
        "default_value": "10",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "integer", "min:3", "max:32"],
        "sort": 17,
    },
    {
        "name": "Spawn Protection",
        "description": "Radius in blocks around spawn where only operators can build. Set to 0 to disable.",
        "env_variable": "SPAWN_PROTECTION",
        "default_value": "16",
        "user_viewable": True,
        "user_editable": True,
        "rules": ["required", "integer", "min:0", "max:100"],
        "sort": 18,
    },
]

# Set of env_variables we own (for idempotent re-runs)
NORDLY_ENV_VARS = {v["env_variable"] for v in NORDLY_VARS}

# ---------------------------------------------------------------------------
# server.properties parser rules to add (mapping property -> Pelican variable).
# Pelican uses {{server.build.env.VAR_NAME}} to read env vars during config parse.
# ---------------------------------------------------------------------------
NORDLY_FIND_RULES = {
    "motd": "{{server.build.env.MOTD}}",
    "white-list": "{{server.build.env.WHITELIST}}",
    "enforce-whitelist": "{{server.build.env.WHITELIST}}",
    "online-mode": "{{server.build.env.ONLINE_MODE}}",
    "difficulty": "{{server.build.env.DIFFICULTY}}",
    "gamemode": "{{server.build.env.GAMEMODE}}",
    "max-players": "{{server.build.env.MAX_PLAYERS}}",
    "pvp": "{{server.build.env.PVP}}",
    "view-distance": "{{server.build.env.VIEW_DISTANCE}}",
    "spawn-protection": "{{server.build.env.SPAWN_PROTECTION}}",
}

# ---------------------------------------------------------------------------
# Nordly install script addition.
# Appended to the end of the upstream Paper install script.
# Creates NORDLY-WELCOME.md visible to customer in file manager.
# Marker comment so we can detect and replace on re-run.
# ---------------------------------------------------------------------------
NORDLY_INSTALL_MARKER = "# === NORDLY INSTALL ADDITION ==="
NORDLY_INSTALL_END = "# === END NORDLY INSTALL ADDITION ==="

NORDLY_INSTALL_SNIPPET = f"""
{NORDLY_INSTALL_MARKER}
# Drop a Nordly welcome file for new customers.
cat > /mnt/server/NORDLY-WELCOME.md <<'WELCOME_EOF'
# Welcome to your Nordly-hosted Minecraft server

Your server is now running on **nordly.gg** infrastructure.

## Security defaults applied
Your server starts with these Nordly-recommended defaults:

- **Whitelist enabled** — only invited players can join
- **Online mode enabled** — premium Minecraft accounts required
- **Spawn protection** — 16 blocks around spawn protected

These keep your server private and prevent random players from joining.
Adjust them anytime in the Startup tab of your Nordly panel.

## Add players to the whitelist
1. Start your server
2. Open the Console tab in your Nordly panel
3. Type: `whitelist add <YourMinecraftUsername>`
4. Repeat for each friend

## Make your server public
If you want anyone to join:
1. Go to the Startup tab
2. Set "Enable Whitelist" to false
3. Restart your server

## Need help?
- Email: hi@nordly.gg
- Docs: https://nordly.gg/docs

Welcome to the Nordly community.
WELCOME_EOF
echo -e "Nordly welcome file deployed to /mnt/server/NORDLY-WELCOME.md"
{NORDLY_INSTALL_END}
"""


def merge_variables(existing: list, new_vars: list) -> list:
    """Drop any prior Nordly variables (by env_variable) then append new ones."""
    kept = [v for v in existing if v.get("env_variable") not in NORDLY_ENV_VARS]
    return kept + new_vars


def extend_config_files(config_files_str: str) -> str:
    """
    config.files is stored as a stringified JSON inside the egg JSON.
    Parse it, merge Nordly find rules into the server.properties parser, re-stringify.
    """
    cfg = json.loads(config_files_str)

    sp = cfg.setdefault("server.properties", {})
    sp.setdefault("parser", "properties")
    find = sp.setdefault("find", {})

    # Idempotent: overwrite any existing Nordly keys with current values
    for key, value in NORDLY_FIND_RULES.items():
        find[key] = value

    # Re-stringify with Pelican's typical formatting (4-space indent)
    return json.dumps(cfg, indent=4)


def extend_install_script(script: str) -> str:
    """
    Append Nordly install snippet to the install script. Idempotent:
    if marker exists, replace the existing block.
    """
    if NORDLY_INSTALL_MARKER in script:
        # Replace existing block
        start = script.find(NORDLY_INSTALL_MARKER)
        end = script.find(NORDLY_INSTALL_END)
        if end == -1:
            print("WARN: found start marker but no end marker; appending fresh block")
            return script + NORDLY_INSTALL_SNIPPET
        end += len(NORDLY_INSTALL_END)
        return script[:start] + NORDLY_INSTALL_SNIPPET.strip() + script[end:]
    return script.rstrip() + "\n\n" + NORDLY_INSTALL_SNIPPET.strip() + "\n"


def main() -> int:
    with INPUT.open() as f:
        egg = json.load(f)

    print(f"Loaded: {egg['name']} (UUID: {egg['uuid']})")
    print(f"Variables before: {len(egg.get('variables', []))}")

    # 1. Add Nordly variables
    egg["variables"] = merge_variables(egg.get("variables", []), NORDLY_VARS)
    print(f"Variables after:  {len(egg['variables'])}")

    # 2. Extend server.properties config parser rules
    cfg_files_str = egg["config"]["files"]
    egg["config"]["files"] = extend_config_files(cfg_files_str)
    print(f"Config find rules: {len(json.loads(egg['config']['files'])['server.properties']['find'])} keys")

    # 3. Extend install script
    install = egg["scripts"]["installation"]
    install["script"] = extend_install_script(install["script"])
    print(f"Install script: {len(install['script'])} chars")

    # 4. Validate JSON serialization
    output = json.dumps(egg, indent=4, ensure_ascii=False)
    json.loads(output)  # round-trip check

    # 5. Write output
    with OUTPUT.open("w") as f:
        f.write(output)
    print(f"\nWrote: {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size} bytes")

    return 0


if __name__ == "__main__":
    sys.exit(main())
