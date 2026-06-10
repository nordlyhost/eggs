# Changelog

All notable changes to Nordly's custom eggs are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [paper-v1.0.0] - 2026-06-10

### Added
- Initial fork from upstream Paper egg
- Custom variables exposed in Pelican Startup tab:
  - `MOTD` — Server message of the day (defaults to Nordly branding)
  - `WHITELIST` — Whitelist toggle (defaults to `true`)
  - `ONLINE_MODE` — Premium account enforcement (defaults to `true`)
  - `DIFFICULTY` — Difficulty dropdown (defaults to `easy`)
  - `GAMEMODE` — Game mode dropdown (defaults to `survival`)
  - `MAX_PLAYERS` — Max player count (defaults to `20`)
  - `PVP` — PvP toggle (defaults to `true`)
  - `VIEW_DISTANCE` — Render distance (defaults to `10`)
  - `SPAWN_PROTECTION` — Spawn protection radius (defaults to `16`)
- Configuration file rules mapping all variables to `server.properties`
- Nordly welcome file (`NORDLY-WELCOME.md`) deployed to server root on install
- Secure-by-default install (whitelist on, online-mode on)

## [nodejs-v1.0.0] - 2026-06-10

### Added
- Initial fork from upstream Node.js generic egg
- Custom `DISCORD_TOKEN` environment variable
- Defaults to Node.js 24

### Fixed
- Broken `MAIN_FILE` glob check that incorrectly routed all servers through ts-node
- Startup command simplified and made more reliable