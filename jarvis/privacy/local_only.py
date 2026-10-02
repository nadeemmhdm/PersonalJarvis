"""Fail-closed network policy for the private/local Personal Jarvis profile."""
from __future__ import annotations
import ipaddress, os
from urllib.parse import urlparse
_TRUTHY={"1","true","yes","on"}
_HF_HOSTS={"huggingface.co","hf.co","cdn-lfs.huggingface.co"}\n_UPDATE_HOSTS={"api.github.com","github.com","objects.githubusercontent.com","release-assets.githubusercontent.com","raw.githubusercontent.com"}
class LocalOnlyViolation(RuntimeError): pass
def is_local_only():
    return os.environ.get("JARVIS_LOCAL_ONLY","1").strip().lower() in _TRUTHY
def _loopback(host):
    host=(host or "").strip().lower().rstrip(".")
    if host=="localhost": return True
    try: return ipaddress.ip_address(host).is_loopback
    except ValueError: return False
def assert_local_endpoint(url):
    if not is_local_only(): return
    p=urlparse(url if "://" in url else "http://"+url)
    if not _loopback(p.hostname or ""):
        raise LocalOnlyViolation("Local-only mode blocked non-loopback endpoint: "+(p.hostname or url))
def assert_outbound_allowed(url, *, purpose):
    if not is_local_only(): return
    p=urlparse(url if "://" in url else "https://"+url)
    host=(p.hostname or "").lower().rstrip(".")
    if _loopback(host): return
    if purpose=="model_download" and host in _HF_HOSTS and p.scheme=="https": return\n    if purpose=="signed_update" and host in _UPDATE_HOSTS and p.scheme=="https": return
    raise LocalOnlyViolation("Local-only mode blocked outbound "+repr(purpose)+" traffic to "+(host or url))
def local_only_status():
    return {"enabled":is_local_only(),"runtime_network":"loopback-only" if is_local_only() else "configured","download_exception":"HTTPS model downloads and verified GitHub release updates only","telemetry":"disabled by policy"}
