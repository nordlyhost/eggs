# Discord Bot Egg Customizations

## Node.js Generic (Nordly)

**Source**: `pelican-eggs/generic/nodejs/egg-node-js-generic.json`
**Forked on**: 2026-06-10
**Upstream commit at fork time**: [TODO - fill in actual commit hash]

### Customizations

1. **New variable**:
   - `DISCORD_TOKEN` — string, nullable, user-editable. Pelican variable rules: `nullable` + `string` (entered separately, not pipe-separated, due to Pelican beta validation bug)

2. **Startup command** replaced from broken upstream version to:
```bash
   if [[ -f /home/container/package.json ]]; then /usr/local/bin/npm install --omit=dev; fi; /usr/local/bin/node /home/container/${MAIN_FILE}
```
   
   Upstream version had a broken `MAIN_FILE` glob check (`[[ "${MAIN_FILE}" == "*.js" ]]`) that always falls through to ts-node regardless of whether the bot is plain JS or TypeScript.

3. **Default `MAIN_FILE`** kept as `index.js`.

### To update from upstream

1. Re-export upstream Node.js generic egg
2. Re-apply the startup command fix
3. Re-add the DISCORD_TOKEN variable
4. Test by deploying a bot
5. Update CHANGELOG and tag new version