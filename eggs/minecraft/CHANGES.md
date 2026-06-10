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

### Schema fixes (Pelican beta34 export-import mismatch)
- Renamed `startup_commands` → `startup` (Pelican beta34 exports with the former, importer expects the latter)

### To update from upstream

1. Re-export upstream Paper egg from latest pelican-eggs/eggs
2. Review the upstream changelog for what changed
3. Re-apply each customization above
4. Test on a fresh server before deploying
5. Update version tag and CHANGELOG.md
6. Commit the new JSON file


## Important: deployment method

This egg's customizations were applied via Pelican admin UI, NOT via JSON import.

The exported JSON file in this directory is a record of the working state, intended for:
- Reference / diff against future versions
- Documentation of what's been customized
- Re-application via UI to a fresh Pelican install (manual)

**Do NOT attempt to re-import this JSON into a Pelican panel** — Pelican beta34 has multiple import-side bugs we documented in the v1.0.0 release notes that prevent clean re-import.

## v1.0.0 known issues / gotchas

During development we hit these Pelican beta34 bugs:
1. Export uses `startup_commands` key but importer expects `startup` (rename on import)
2. Validation rules with `|` characters in regex break form rendering
3. Pipe-separated rule strings fail validation (`Method validateNullable|string does not exist`)
4. The placeholder `{{server.build.env.X}}` does NOT work — must use `{{server.environment.X}}`
5. Some Filament `OptionStateCast` errors when array-formatted rules contain regex with alternation

When upstream Paper egg gets significant updates and we need to re-fork, the process is:
1. Import fresh upstream Paper egg as a new egg (stock, untouched)
2. Manually re-apply each customization via the admin UI (variables, config files, install script)
3. Export the result
4. Diff against this file to verify customizations match
5. Replace this file with the new export, tag new major version

Documented customizations:
- 9 new variables (see Variables section of admin UI for the egg)
- Extended Configuration Files JSON (server.properties parser rules)
- Install script appended with NORDLY-WELCOME.md generator (marked with === comments)