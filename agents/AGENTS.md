# AGENTS.md

Project-local agent instructions - extends the global AGENTS.md.
Follow the base rules first, then apply the additions below.

## Memory

You wake up fresh each session. The files in `agents/memory/` are your
continuity.

- **Daily notes:** `agents/memory/YYYY-MM-DD.md` — raw logs of what happened.

Capture what matters: decisions, context, things to remember. Skip secrets
unless explicitly asked to keep them.

- You can **read, edit, and update** memories freely.
- Write significant events, thoughts, decisions, opinions, lessons learned.

### Write It Down — No "Mental Notes"

- **Memory is limited.** If you want to remember something, WRITE IT TO A FILE.
- "Mental notes" don't survive session restarts. Files do.
- When someone says "remember this" → append to `agents/memory/YYYY-MM-DD.md`.
- When you learn a lesson → append to `agents/memory/YYYY-MM-DD.md`.
- When you make a mistake → document it so future-you doesn't repeat it.
- **Text > Brain.**

### When to write

Append to `agents/memory/YYYY-MM-DD.md` in two cases:

1. **On significant events** during a session, as they happen:
   - A decision that affects future work
   - A lesson learned or a mistake to avoid next time
   - An opinion or convention worth preserving
   - Context that wasn't obvious from the code
2. **On explicit dump requests** — when the user says "dump memory",
   "save the session", "remember this session", or similar, append a
   concise session summary to today's file.

### File and entry format

- Filename: today's date in ISO format, e.g. `2026-04-30.md`. Get it with
  `date +%F`.
- **Append** — if the file already exists, add to the bottom. Never overwrite
  or delete past entries.
- One entry per event or session dump. Suggested entry shape:

````md
## <HH:MM> — <short title>

**Context:** one-line framing of the task or thread.

**Decisions / events:**
- ...

**Lessons:**
- ...

**Follow-ups:**
- ...
````

### What NOT to write to memory

- Secrets, credentials, tokens, API keys, PII.
- Contents of `.env` or any gitignored config file.
- Private info the user hasn't asked you to persist.

If unsure whether something belongs in memory, ask before writing.

