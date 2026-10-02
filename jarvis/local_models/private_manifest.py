"""Conservative model defaults for the 8 GB RAM private profile."""
MIN_RAM_GB=8
DEFAULT_CONTEXT=2048
MODEL_MANIFEST={
"brain":{"family":"Qwen3","size":"1.7B","format":"GGUF","quantization":"Q4_K_M","runtime":"llama.cpp","max_context_8gb":DEFAULT_CONTEXT,"purpose":"chat, tool planning, multilingual assistant"},
"stt":{"family":"Whisper","variant":"small multilingual","runtime":"faster-whisper","compute_type":"int8","purpose":"local Malayalam/English speech recognition"},
"tts":{"family":"Piper","runtime":"sherpa-onnx/Piper","purpose":"local speech output"},
"wake":{"family":"Vosk/openWakeWord","runtime":"local","purpose":"offline wake phrase detection"}}
