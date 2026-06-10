# Pelican Plugin: Security Tab

**Status**: Roadmapped, not yet built. Build trigger: customer feedback shows whitelist/security management is a top-3 support pain point.

## Goal

Add a "Security" tab to each game server in the customer-facing Pelican panel, providing a UI for common Minecraft security operations without requiring console commands or file editing.

## Scope (v1)

### Whitelist Management
- Display current whitelist (read from `whitelist.json`)
- Add user (sends `whitelist add <username>` to console if running, edits file if offline)
- Remove user (sends `whitelist remove <username>` or edits file)
- Toggle whitelist on/off (sends `whitelist on`/`whitelist off`)

### MOTD Editor
- Display current MOTD with Minecraft color code rendering preview
- Edit MOTD with helper buttons for common color codes (§a green, §c red, §l bold, §r reset)
- Save to `server.properties`, hot-reload via console command if supported

### Security Toggles
- Online-mode (warn user if disabling)
- PvP enabled
- Hardcore mode warning

### Server Visibility
- Public / Private toggle (combines whitelist + MOTD visibility)
- Quick "lock down server" button (enables whitelist, sets MOTD to "Private server")

## Out of scope (v1)

- Per-player permissions
- World-edit / op management (that's a separate tab if ever)
- Mod/plugin management

## Technical notes

- Pelican plugin system uses Filament admin panel framework
- Server commands go through Wings API
- File operations also through Wings (read/write `whitelist.json`, `server.properties`)
- Must handle offline-server case gracefully

## Estimated effort

3-7 days of focused development, assuming familiarity with Laravel/Filament. Add 50% time for first-plugin learning curve.

## When to build

After Phase 3 launch, when customer feedback validates this is among the top pain points. Until then, document the workarounds (console commands, file editor) in customer guides.