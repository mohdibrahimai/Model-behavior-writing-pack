import json, pathlib

metrics_path = pathlib.Path("public/metrics.json")
if not metrics_path.exists():
    print("metrics.json not found yet; skipping badges.")
    raise SystemExit(0)

m = json.loads(metrics_path.read_text(encoding="utf-8"))
sessions = int(m.get("sessions", 0))
sr = float(m.get("success_rate", 0.0))
pct = round(sr * 100)

if   pct >= 90: color = "brightgreen"
elif pct >= 80: color = "green"
elif pct >= 70: color = "yellowgreen"
elif pct >= 60: color = "yellow"
elif pct >= 50: color = "orange"
else:           color = "red"

badges_dir = pathlib.Path("public/badges")
badges_dir.mkdir(parents=True, exist_ok=True)

(badges_dir/"success.json").write_text(json.dumps({
  "schemaVersion": 1, "label": "Success", "message": f"{pct}%", "color": color
}), encoding="utf-8")

(badges_dir/"sessions.json").write_text(json.dumps({
  "schemaVersion": 1, "label": "Sessions", "message": str(sessions), "color": "informational"
}), encoding="utf-8")

print("✅ Wrote badges to public/badges/")
