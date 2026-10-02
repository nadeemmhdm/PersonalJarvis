# Operations

## Normal lifecycle

1. The OS login starts Personal Jarvis through the existing cross-platform autostart manager.
2. Startup performs lightweight health checks; the dashboard starts even when an optional component is degraded.
3. The UI checks the latest published GitHub Release after boot and periodically while open.
4. A newer version appears as a dismissible announcement and in the existing Update control.
5. Update artifacts are downloaded only through the updater path and verified before installation.
6. Local AI inference, memory, speech and personal profile remain local.

## Operator commands

- `jarvis` — start the desktop assistant.
- `jarvis serve` — start the local server.
- `python -m jarvis --doctor` — comprehensive health report.
- Re-run the one-line installer — idempotent install/update/repair path.

## Update safety

Never execute an unverified release asset. Frozen installers require the SHA-256 manifest from the same release. Managed checkouts stage the published tag and finish the transaction after the running process exits. Development checkouts/forks are not silently reset by the in-app updater.

## Privacy

The private profile permits loopback runtime traffic. The only external exceptions are explicit model downloads from the Hugging Face allowlist and verified update traffic to the GitHub release allowlist. Neither exception is valid for prompts, memories, voice transcripts or inference.
