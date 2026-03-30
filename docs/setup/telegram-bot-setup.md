# Telegram Bot Setup

## Current V1 channel model
- Main: direct message with the bot
- Workers: private group
- Alerts: private group

## Current identifiers
- Main user/chat: `5143357049`
- Workers group: `-5185231049`
- Alerts group: `-5131828323`

## Access model
- Main DM allowlisted to the household operator
- Workers and Alerts groups enabled for the same allowlisted sender
- `requireMention: false` is intended for Workers and Alerts so the bot can see and act on group traffic without explicit mention

## Important Telegram requirement for no-mention groups
To ensure the bot sees all group messages reliably when `requireMention: false`:
- disable privacy mode via BotFather `/setprivacy`
  or
- make the bot an admin in the relevant groups

After changing privacy mode, remove and re-add the bot to affected groups if Telegram requires it for the change to take effect.

## Security note
Bot tokens are secrets and must not be committed to Git-tracked files.
If a token is exposed, rotate it in BotFather and update runtime configuration.
