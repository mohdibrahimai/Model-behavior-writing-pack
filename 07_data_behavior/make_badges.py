import json, pathlib
m = json.loads(pathlib.Path("public/metrics.json").read_text(encoding="utf-8"))
sessions = int(m.get("sessions", 0))
sr = float(m.get("success_rate", 0.0))
pct = round(sr * 100)

# Simple color ramp
if   pct >= 90: color = "brightgreen"
elif pct >= 80: color = "green"
elif pct >= 70: color = "yellowgreen"
elif pct >= 60: color = "yellow"
elif pct >= 50: color = "orange"
else:           color = "red"

badges_dir = pathlib.Path("public/badges")
badges_dir.mkdir(parents=True, exist_ok=True)

# Success badge (percent)
(badges_dir/"success.json").write_text(json.dumps({
  "schemaVersion": 1,
  "label": "Success",
  "message": f"{pct}%",
  "color": color
}), encoding="utf-8")

# Sessions badge
(badges_dir/"sessions.json").write_text(json.dumps({
  "schemaVersion": 1,
  "label": "Sessions",
  "message": str(sessions),
  "color": "informational"
}), encoding="utf-8")
