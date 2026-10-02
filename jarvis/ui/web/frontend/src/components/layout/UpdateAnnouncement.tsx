import { useEffect, useState } from "react";
import { Download, X } from "lucide-react";
import { useUpdate } from "@/hooks/useUpdate";

const keyFor = (version: string) => `jarvis.update.dismissed.${version}`;

export function UpdateAnnouncement() {
  const { status } = useUpdate();
  const version = status?.latest ?? "";
  const [dismissed, setDismissed] = useState(false);
  useEffect(() => {
    if (!version) return setDismissed(false);
    try { setDismissed(window.localStorage.getItem(keyFor(version)) === "1"); }
    catch { setDismissed(false); }
  }, [version]);
  if (!status?.managed || !status.update_available || !version || dismissed) return null;
  const dismiss = () => {
    try { window.localStorage.setItem(keyFor(version), "1"); } catch { /* optional UI preference */ }
    setDismissed(true);
  };
  return (
    <div data-testid="update-announcement" className="mx-3 mt-2 flex items-center gap-3 rounded-lg border border-border bg-card px-4 py-3 text-sm shadow-sm">
      <Download aria-hidden className="h-4 w-4 shrink-0" />
      <div className="min-w-0 flex-1">
        <strong>Personal Jarvis {version} is available.</strong>
        <span className="ml-2 text-muted-foreground">Verified update ready. Use the Update button to install it.</span>
      </div>
      <button type="button" onClick={dismiss} aria-label="Hide update announcement" className="rounded-md p-1 hover:bg-secondary">
        <X aria-hidden className="h-4 w-4" />
      </button>
    </div>
  );
}
