import pytest
from jarvis.brain.provider_registry import BrainProviderRegistry
from jarvis.privacy.local_only import LocalOnlyViolation
class Dummy: pass
def registry(name):
    r=BrainProviderRegistry(); r._loaded=True; r._classes={name:Dummy}; return r
def test_cloud_provider_refused(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1")
    with pytest.raises(LocalOnlyViolation): registry("openai").instantiate("openai")
