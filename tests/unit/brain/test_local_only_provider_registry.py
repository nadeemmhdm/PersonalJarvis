import pytest
from jarvis.brain.provider_registry import BrainProviderRegistry
from jarvis.privacy.local_only import LocalOnlyViolation

def test_cloud_provider_refused_before_construction(monkeypatch):
    monkeypatch.setenv("JARVIS_LOCAL_ONLY","1")
    class MustNotConstruct:
        def __init__(self,*a,**k): raise AssertionError("cloud provider was constructed")
    r=BrainProviderRegistry(); r._loaded=True; r._classes={"openai":MustNotConstruct}
    with pytest.raises(LocalOnlyViolation): r.instantiate("openai")
