import json, os, sys

S = os.path.dirname(os.path.abspath(__file__))
tasks = json.load(open(f"{S}/tasks.json"))
WS = os.environ.get("WS", "workspace")
marker = os.path.getmtime(f"{S}/marker")


def changed(arm):
    root = f"{S}/{arm}/{WS}"
    out = []
    for d, _, fs in os.walk(root):
        if "/.git" in d:
            continue
        for f in fs:
            p = os.path.join(d, f)
            if os.path.getmtime(p) > marker:
                out.append(os.path.relpath(p, root))
    return out


rows, tot = [], {}
for arm in ("base", "wb"):
    ch = changed(arm)
    for t in tasks:
        p = f"{S}/out/{arm}-{t['id']}.json"
        try:
            r = json.load(open(p))
        except Exception as e:
            rows.append((arm, t["id"], "ERROR", 0, 0, 0, str(e)[:60])); continue
        text = r.get("result", "") or ""
        if t["kind"] == "read":
            ok = all(k.lower() in text.lower() for k in t["expect"])
            if ok and t.get("expect_any"):
                ok = any(k.lower() in text.lower() for k in t["expect_any"])
            where = ""
        else:
            hits = [f for f in ch if os.path.basename(f) == t["file_hint"] and
                    all(k in open(f"{S}/{arm}/{WS}/{f}", errors="replace").read() for k in t["expect"])]
            ok = bool(hits)
            where = ",".join(hits) or "elsewhere: " + ",".join(
                f for f in ch if any(k in open(f"{S}/{arm}/{WS}/{f}", errors="replace").read() for k in t["expect"][:1]))[:80]
        cost, turns, ms = r.get("total_cost_usd", 0), r.get("num_turns", 0), r.get("duration_ms", 0)
        rows.append((arm, t["id"], "PASS" if ok else "FAIL", round(cost, 3), turns, round(ms / 1000), where))
        a = tot.setdefault(arm, [0, 0, 0.0, 0, 0])
        a[0] += ok; a[1] += 1; a[2] += cost; a[3] += turns; a[4] += ms / 1000

print("| Setup | Task | Result | Cost $ | Turns | Seconds | Write landed |")
print("|---|---|---|---|---|---|---|")
for r in sorted(rows, key=lambda r: (r[1], r[0])):
    print("| " + " | ".join(str(x) for x in r) + " |")
print()
for arm, (p, n, c, tu, s) in tot.items():
    print(f"{arm}: {p}/{n} pass, ${c:.2f}, {tu} turns, {s:.0f}s total")
if "-v" in sys.argv:
    for arm in ("base", "wb"):
        for t in tasks:
            try:
                print(f"\n## {arm} {t['id']}\n" + json.load(open(f"{S}/out/{arm}-{t['id']}.json")).get("result", "")[:700])
            except Exception:
                pass
