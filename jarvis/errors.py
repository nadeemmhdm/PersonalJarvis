"""Stable user-facing Personal Jarvis error identifiers."""
ERRORS={
"JRV-1001":"Required runtime missing","JRV-1002":"Insufficient free disk space",
"JRV-1101":"llama.cpp server missing","JRV-1102":"GGUF model missing or invalid","JRV-1103":"Local model server did not start",
"JRV-1201":"STT model unavailable","JRV-1202":"TTS voice unavailable","JRV-1203":"Microphone unavailable",
"JRV-1301":"External inference blocked","JRV-1302":"Non-loopback endpoint blocked",
"JRV-1401":"Release check failed","JRV-1402":"Update checksum failed","JRV-1403":"Update installation failed",
"JRV-1501":"Required component missing","JRV-1502":"Component version unsupported"}
def explain(code:str)->str:
    return ERRORS.get(code,"Unknown Personal Jarvis error")
