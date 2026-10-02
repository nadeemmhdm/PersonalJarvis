"""Managed llama.cpp runtime helpers for the private 8 GB profile."""
from __future__ import annotations
import os, shutil, socket, subprocess
from pathlib import Path
from jarvis.privacy.local_only import assert_local_endpoint

DEFAULT_HOST="127.0.0.1"; DEFAULT_PORT=8080
def find_server(explicit=""):
    candidates=[explicit,os.environ.get("LLAMA_SERVER",""),shutil.which("llama-server") or "",shutil.which("llama-server.exe") or ""]
    for item in candidates:
        if item and Path(item).expanduser().exists(): return str(Path(item).expanduser().resolve())
    return None
def validate_model(path):
    p=Path(path).expanduser().resolve()
    if p.suffix.lower()!=".gguf" or not p.is_file(): raise ValueError("A local .gguf model file is required")
    return p
def build_command(server,model,*,threads=None,context=2048,port=DEFAULT_PORT):
    assert_local_endpoint(f"http://{DEFAULT_HOST}:{port}")
    threads=threads or max(1,min(4,(os.cpu_count() or 2)-1))
    return [str(Path(server).resolve()),"-m",str(validate_model(model)),"-t",str(threads),"-c",str(context),"-b","128","-ngl","0","-np","1","--host",DEFAULT_HOST,"--port",str(port)]
def port_open(port=DEFAULT_PORT):
    try:
        with socket.create_connection((DEFAULT_HOST,port),timeout=.35): return True
    except OSError: return False
def start(server,model,*,threads=None,context=2048,port=DEFAULT_PORT,log_path=None):
    if port_open(port): raise RuntimeError(f"port {port} is already in use")
    cmd=build_command(server,model,threads=threads,context=context,port=port)
    sink=subprocess.DEVNULL
    if log_path:
        lp=Path(log_path); lp.parent.mkdir(parents=True,exist_ok=True); sink=open(lp,"ab")
    flags=getattr(subprocess,"CREATE_NO_WINDOW",0) if os.name=="nt" else 0
    return subprocess.Popen(cmd,stdin=subprocess.DEVNULL,stdout=sink,stderr=sink,creationflags=flags)
