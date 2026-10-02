import pytest
from jarvis.privacy.local_only import LocalOnlyViolation,assert_local_endpoint,assert_outbound_allowed
def test_loopback_runtime_allowed(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1"); assert_local_endpoint("http://127.0.0.1:8080/v1"); assert_local_endpoint("http://localhost:47821")
def test_cloud_runtime_blocked(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1")
    with pytest.raises(LocalOnlyViolation): assert_local_endpoint("https://api.openai.com/v1")
def test_hf_download_only_exception(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1"); assert_outbound_allowed("https://huggingface.co/model/file.gguf",purpose="model_download")
    with pytest.raises(LocalOnlyViolation): assert_outbound_allowed("https://huggingface.co/api/inference",purpose="inference")
