# Local Private AI profile

This profile targets **8 GB RAM or more** and treats privacy as a fail-closed runtime invariant.

- LLM inference: local llama.cpp-compatible runtime on loopback.
- Memory/profile/history/wiki: local data directory only.
- STT: local multilingual Whisper (int8).
- TTS: local Piper/sherpa-onnx.
- Wake phrase: local Vosk/openWakeWord.
- Cloud inference providers are forbidden while local-only mode is enabled.
- Hugging Face is allowed only for explicit HTTPS model downloads, never inference, prompts, memory, transcripts, telemetry or analytics.
- After weights are downloaded, the assistant can operate with internet disconnected.

The conservative 8 GB brain profile is Qwen3 1.7B-class GGUF Q4_K_M with a 2048-token context. Speech components should load independently rather than keeping every model resident.

First run stores assistant name, owner's preferred form of address, wake phrase, languages, response style and local voice selection in the local data directory. Sensitive identity fields are not required.

Runtime endpoints must be loopback in local-only mode. External access must pass the central outbound policy with an explicit purpose; only model downloads can reach the Hugging Face allowlist.
