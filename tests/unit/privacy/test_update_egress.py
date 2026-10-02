import pytest
from jarvis.privacy.local_only import LocalOnlyViolation,assert_outbound_allowed
def test_github_release_update_allowed(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1")
    assert_outbound_allowed("https://api.github.com/repos/x/y/releases/latest",purpose="signed_update")
    assert_outbound_allowed("https://github.com/x/y/releases/download/v1/app.exe",purpose="signed_update")
def test_github_never_allowed_for_inference(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1")
    with pytest.raises(LocalOnlyViolation):
        assert_outbound_allowed("https://api.github.com/",purpose="inference")
def test_arbitrary_update_host_blocked(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1")
    with pytest.raises(LocalOnlyViolation):
        assert_outbound_allowed("https://example.com/update.exe",purpose="signed_update")
