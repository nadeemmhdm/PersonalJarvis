"""Local first-run identity/preferences for the user's personal assistant."""
from __future__ import annotations
import json, os, secrets
from dataclasses import asdict, dataclass
from pathlib import Path
@dataclass(frozen=True)
class Personalization:
    assistant_name:str="Assistant"; owner_address:str="User"; wake_phrase:str="Hey Assistant"
    languages:tuple[str,...]=("en",); response_style:str="natural"; voice:str="local-default"
    local_only:bool=True; memory_enabled:bool=True
def _clean(value,fallback,limit=80):
    value=" ".join((value or "").split()).strip()
    return value[:limit] or fallback
def build_personalization(*,assistant_name,owner_address,wake_phrase="",languages=("en",),response_style="natural",voice="local-default"):
    name=_clean(assistant_name,"Assistant"); owner=_clean(owner_address,"User"); wake=_clean(wake_phrase,"Hey "+name)
    langs=tuple(dict.fromkeys(x.strip().lower() for x in languages if x.strip())) or ("en",)
    return Personalization(name,owner,wake,langs,_clean(response_style,"natural"),_clean(voice,"local-default"))
def save_personalization(profile,data_dir:Path):
    data_dir.mkdir(parents=True,exist_ok=True); target=data_dir/"personalization.json"; tmp=target.with_suffix(".tmp-"+secrets.token_hex(4))
    payload=asdict(profile); payload["languages"]=list(profile.languages)
    with open(tmp,"w",encoding="utf-8",newline="") as fp:
        json.dump(payload,fp,indent=2,ensure_ascii=False); fp.flush(); os.fsync(fp.fileno())
    try:
        if os.name!="nt": os.chmod(tmp,0o600)
        os.replace(tmp,target)
    finally: tmp.unlink(missing_ok=True)
    return target
def system_identity(profile):
    return f"Your name is {profile.assistant_name}. Address the user as {profile.owner_address}. Preferred languages: {', '.join(profile.languages)}. Response style: {profile.response_style}. Keep private user data local."
