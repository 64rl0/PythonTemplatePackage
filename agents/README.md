# agents/

Working folder for AI coding agents on this project.

## Purpose

Centralize everything related to how AI agents operate here: instructions
that extend the global agent config, and persistent memory so agents keep
context across sessions.

## Structure

```
agents/
├── README.md           # this file (for humans)
├── AGENTS.md           # agent instructions (extends the global AGENTS.md)
└── memory/
    └── YYYY-MM-DD.md   # one file per session date, appended by agents
```

## How to use

**Agents** — read `AGENTS.md` and follow the memory protocol defined there.

**Humans**:
- Browse `memory/` to see what an agent did, decided, or learned on a given
  day. Treat it as read-only history; only edit to redact secrets or tidy up.
- Memory files are committed to git on purpose — they travel with the repo
  and give continuity across machines and teammates.
- Never paste secrets, tokens, or `.env` contents into memory files.

