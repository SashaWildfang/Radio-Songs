"""
Radio song library - built by Sasha Wildfang for Fractal Network.

Rebuilds index.json from every .nbs file in this repository. Servers running the
Radio plugin read index.json to know which songs to download, update or remove,
so run this after adding, removing, renaming or changing songs, then commit and push:

    python update_index.py
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    songs = []
    for file in ROOT.rglob("*.nbs"):
        relative = file.relative_to(ROOT)
        if any(part.startswith(".") for part in relative.parts):
            continue
        data = file.read_bytes()
        songs.append({
            "path": relative.as_posix(),
            "size": len(data),
            "sha1": hashlib.sha1(data).hexdigest(),
        })
    songs.sort(key=lambda s: s["path"].lower())

    lines = ['{', '  "songs": [']
    lines.append(",\n".join("    " + json.dumps(s, ensure_ascii=False) for s in songs))
    lines += ['  ]', '}', '']
    (ROOT / "index.json").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {len(songs)} songs to index.json")


if __name__ == "__main__":
    main()
