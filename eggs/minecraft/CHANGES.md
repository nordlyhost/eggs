# Minecraft Egg Customizations

This document records what differs between Nordly's Minecraft eggs and their upstream sources.

## Paper (Nordly)

**Source**: `pelican-eggs/eggs/game_eggs/minecraft/java/paper/egg-paper.json`
**Forked on**: 2026-06-10
**Upstream commit at fork time**: [TODO - fill in actual commit hash]

### Customizations

1. **New variables** (visible in Pelican Startup tab):
   - `MOTD` — string, defaults to `§a§lHosted by Nordly §r§7· §fnordly.gg`
   - `WHITELIST` — boolean toggle, defaults to `true`
   - `ONLINE_MODE` — boolean toggle, defaults to `true`
   - `DIFFICULTY` — enum [peaceful, easy, normal, hard], defaults to `easy`
   - `GAMEMODE` — enum [survival, creative, adventure, spectator], defaults to `survival`
   - `MAX_PLAYERS` — integer, defaults to `20`
   - `PVP` — boolean toggle, defaults to `true`
   - `VIEW_DISTANCE` — integer, defaults to `10`
   - `SPAWN_PROTECTION` — integer, defaults to `16`

2. **Configuration file rules** added to map each variable to `server.properties`:
   - `motd → {{MOTD}}`
   - `white-list → {{WHITELIST}}`
   - `online-mode → {{ONLINE_MODE}}`
   - `difficulty → {{DIFFICULTY}}`
   - `gamemode → {{GAMEMODE}}`
   - `max-players → {{MAX_PLAYERS}}`
   - `pvp → {{PVP}}`
   - `view-distance → {{VIEW_DISTANCE}}`
   - `spawn-protection → {{SPAWN_PROTECTION}}`

3. **Install script additions** (at end of stock script):
   - Creates `/mnt/server/NORDLY-WELCOME.md` with onboarding instructions
   - Applies secure defaults if `server.properties` doesn't exist

### To update from upstream

1. Re-export upstream Paper egg from latest pelican-eggs/eggs
2. Review the upstream changelog for what changed
3. Re-apply each customization above
4. Test on a fresh server before deploying
5. Update version tag and CHANGELOG.md
6. Commit the new JSON file