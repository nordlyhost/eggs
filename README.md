# Nordly Eggs

Custom Pelican Panel eggs powering [nordly.gg](https://nordly.gg) game server and Discord bot hosting.

This repository contains the egg definitions used by Nordly's Pelican infrastructure, including security-hardened defaults, custom variables exposed via the Pelican Startup tab, and Nordly-branded welcome experiences.

## What's here

- **`eggs/minecraft/`** — Custom Minecraft eggs (Paper, etc.)
- **`eggs/discord-bots/`** — Custom Node.js / Python eggs for Discord bots
- **`docs/customer/`** — Customer-facing documentation
- **`plugins/security-tab/`** — Scoped but unbuilt: Pelican plugin for in-panel security management

## Eggs included

| Egg | Version | Upstream | Notes |
|-----|---------|----------|-------|
| Paper (Nordly) | v1.0.0 | [pelican-eggs/eggs](https://github.com/pelican-eggs/eggs) | Security defaults, MOTD, gameplay vars in Startup tab |
| Node.js (Nordly) | v1.0.0 | [pelican-eggs/generic](https://github.com/pelican-eggs/generic) | Fixed MAIN_FILE bug, proper env var support |

## Versioning

Each egg version is tagged in this repo as `<egg>-vX.Y.Z` (e.g. `paper-v1.0.0`).

- **Major** (`v2.0.0`) — re-forked from upstream, breaking changes
- **Minor** (`v1.1.0`) — new variables or features added
- **Patch** (`v1.0.1`) — bug fixes, no behavioral change

## Maintenance schedule

Upstream eggs are reviewed quarterly. See `CHANGELOG.md` for what's been ported.

## License

MIT, matching upstream Pelican eggs.