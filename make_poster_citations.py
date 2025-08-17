
"""
CLI: Erzeugt komprimierte Literaturzeilen für dein Poster
python make_poster_citations.py --width 90
"""
import json, argparse, textwrap

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--json", default="data/references.json")
    p.add_argument("--width", type=int, default=90, help="max. Zeichen pro Zeile")
    args = p.parse_args()
    refs = json.load(open(args.json, "r", encoding="utf-8"))
    for r in refs:
        line = f"[{r['id']}] {r['short']}"
        if len(line) > args.width:
            line = textwrap.shorten(line, width=args.width, placeholder="…")
        print(line)

if __name__ == "__main__":
    main()
