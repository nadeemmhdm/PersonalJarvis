from jarvis.setup.personalization import build_personalization,save_personalization,system_identity
def test_personalization_is_local_and_custom(tmp_path):
    p=build_personalization(assistant_name="Nila",owner_address="Nadeem",languages=("ml","en"),response_style="Malayalam/Manglish")
    path=save_personalization(p,tmp_path); assert path.parent==tmp_path; assert '"Nila"' in path.read_text(encoding="utf-8")
    prompt=system_identity(p); assert "Nila" in prompt and "Nadeem" in prompt and "ml, en" in prompt
