# Error codes

Stable error codes make support and repair deterministic. User-facing failures should include one code plus a short explanation.

| Code | Area | Meaning | Recovery |
|---|---|---|---|
| JRV-1001 | Setup | Required runtime missing | Run the installer again or `jarvis doctor`. |
| JRV-1002 | Setup | Insufficient free disk space | Free disk space and retry. |
| JRV-1101 | Model | llama.cpp server missing | Run local-model setup/repair. |
| JRV-1102 | Model | GGUF model missing or invalid | Re-download the verified model. |
| JRV-1103 | Model | Local model server did not start | Check `jarvis doctor` and local logs. |
| JRV-1201 | Voice | STT model unavailable | Repair the local voice pack. |
| JRV-1202 | Voice | TTS voice unavailable | Repair/select a local voice. |
| JRV-1203 | Voice | Microphone unavailable | Check OS microphone permission/device. |
| JRV-1301 | Privacy | External inference blocked | Select a loopback local provider. |
| JRV-1302 | Privacy | Non-loopback endpoint blocked | Use localhost/127.0.0.1. |
| JRV-1401 | Update | Release check failed | Retry when GitHub is reachable. |
| JRV-1402 | Update | Update checksum failed | File is rejected; retry download. |
| JRV-1403 | Update | Update installation failed | Run Doctor; current version remains intact. |
| JRV-1501 | Dependency | Required component missing | Run setup/repair. |
| JRV-1502 | Dependency | Component version unsupported | Update/repair the component. |

Never turn a checksum, privacy, signature, permission, or destructive-action failure into an automatic bypass.
