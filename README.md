# Personal Jarvis

**Private, local-first personal AI for Windows, macOS and Linux.**

Personal Jarvis combines a local language model, voice, memory, computer tools, agents and automation in one desktop assistant. The private profile is designed for **8 GB RAM or more** and keeps inference and personal data on the user's machine.

> This fork is being hardened around a local-only runtime. Cloud inference providers are blocked when local-only mode is enabled. Internet access is limited to explicit model downloads and verified software updates.

## Quick install

### Windows

```powershell
irm https://raw.githubusercontent.com/nadeemmhdm/PersonalJarvis/main/install/install.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/nadeemmhdm/PersonalJarvis/main/install/install.sh | bash
```

The installer is intended to be idempotent: it checks prerequisites, installs missing supported components, updates an existing managed installation, registers the desktop launcher, and starts the app. Re-running it is the recovery/update path.

## Local AI profile

| Component | Default profile |
|---|---|
| Brain | Qwen3 1.7B-class GGUF, Q4_K_M |
| Runtime | llama.cpp / local OpenAI-compatible endpoint |
| Context target | 2048 tokens on the conservative 8 GB profile |
| Speech-to-text | Local multilingual Whisper, int8 |
| Text-to-speech | Local Piper / sherpa-onnx |
| Wake phrase | Local Vosk/openWakeWord |
| Memory | Local SQLite/wiki/profile storage |
| Runtime network | Loopback only |

Models are downloaded to the machine and run locally. Hugging Face is a **download source, not an inference provider**. After required models are present, core AI and voice functionality is designed to work without internet access.

## First run

The setup flow lets the owner choose:

- assistant name;
- how the assistant should address them;
- wake phrase;
- languages;
- response style;
- local voice;
- privacy and memory preferences.

These settings are stored locally. Real name, address, birthday and similar identity data are not required.

## Privacy boundary

With local-only mode enabled:

- cloud brain providers cannot be instantiated;
- local model endpoints must resolve to loopback;
- prompts, memories and voice transcripts are not authorised for external inference;
- Hugging Face HTTPS access is restricted to explicit model-download operations;
- GitHub HTTPS access is restricted to the software-update path;
- personal profile, conversation recall and knowledge stay in the local data directory.

Connected web/plugin functionality is separate and must be explicitly enabled; a strict offline session can simply run with networking unavailable.

See [Local Private AI](docs/LOCAL_PRIVATE_AI.md).

## Updates

Personal Jarvis checks published GitHub Releases while the app is running. When a newer release is available, the dashboard shows a dismissible announcement and the existing Update control.

Native installer updates are downloaded and checked against the SHA-256 manifest from the same release before installation. Managed source installs stage the published release transaction and finish it during restart. Development clones/forks are not silently reset by the updater.

Re-running the one-line installer also updates/repairs a managed installation.

See [Operations](docs/OPERATIONS.md).

## Health and recovery

```bash
python -m jarvis --doctor
```

Doctor checks registered capabilities, the selected brain, local-only policy and platform prerequisites. Security/privacy failures are not automatically bypassed.

Stable support codes are documented in [Error Codes](docs/ERROR_CODES.md).

## Core capabilities

- local chat and tool planning;
- searchable long-term conversation memory;
- local user profile and knowledge/wiki;
- voice conversation and wake phrase;
- file and terminal tools with permission controls;
- computer-use support where the OS permits it;
- persistent agents and scheduled routines;
- isolated coding missions and bounded workers;
- destructive-action confirmation and mission safety controls;
- desktop/web UI and CLI;
- verified self-update infrastructure and cross-platform autostart.

## Architecture

```text
Voice / Chat
     |
Personal identity + local memory + local wiki
     |
Local GGUF model -> llama.cpp (127.0.0.1)
     |
Planner / agents / routines
     |
Permission & safety gates
     |
Files / terminal / computer / approved tools
     |
Local history and results
```

## Documentation

- [Local Private AI](docs/LOCAL_PRIVATE_AI.md)
- [Operations and updates](docs/OPERATIONS.md)
- [Error codes](docs/ERROR_CODES.md)
- [Architecture overview](docs/architecture-overview.md)
- [Security policy](SECURITY.md)
- [Contributing](CONTRIBUTING.md)

## Security

Do not weaken the loopback restriction, checksum verification, tool approvals or destructive-action confirmations to make a failed setup appear healthy. Security reports should follow [SECURITY.md](SECURITY.md).

## Development

Before changing provider, networking, update, memory or tool-execution code, run the focused tests for that subsystem and the full project regression suite supported by your platform.

## License

Apache-2.0. Releases through 1.6.0 retain their original MIT license. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
