from pathlib import Path
import pytest
from jarvis.local_models.llamacpp_runtime import build_command,validate_model
def test_requires_real_gguf(tmp_path):
    bad=tmp_path/"model.bin"; bad.write_bytes(b"x")
    with pytest.raises(ValueError): validate_model(bad)
def test_build_is_loopback_cpu_profile(tmp_path):
    server=tmp_path/"llama-server.exe"; server.write_bytes(b"x")
    model=tmp_path/"model.gguf"; model.write_bytes(b"GGUF")
    cmd=build_command(str(server),str(model),threads=4)
    assert "--host" in cmd and "127.0.0.1" in cmd
    assert "-ngl" in cmd and cmd[cmd.index("-ngl")+1]=="0"
    assert "-c" in cmd and cmd[cmd.index("-c")+1]=="2048"
