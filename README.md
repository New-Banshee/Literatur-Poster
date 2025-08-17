
# Poster-Literatur (komprimiert) – Streamlit

Dieses kleine Repo liefert:
- **Kurze Literaturliste** für das Poster (Kopierblock)
- **Vollbelege** + anklickbare DOI-Links
- **Export** als TXT & (heuristische) BibTeX

## Lokal starten (VS Code)

1. Python 3.10+ aktivieren, dann:
   ```bash
   pip install -r requirements.txt
   streamlit run streamlit_app.py
   ```
2. Die Daten liegen in `data/references.json`.
3. Den kopierfertigen Block siehst du oben in der App oder per CLI:
   ```bash
   python make_poster_citations.py --width 90 > poster_shortlist.txt
   ```

## Deployment (kostenlos & stabil)

### Option A: Streamlit Community Cloud
1. Dieses Verzeichnis nach GitHub pushen.
2. Auf **share.streamlit.io** dein Repo verbinden (Public reicht).
3. Als **App entry** `streamlit_app.py` wählen.
4. Den erzeugten **permanenten App-Link** auf dem Poster (kein URL-Shortener).

### Option B: GitHub Pages (statisch)
- Wenn du nur die TXT/BibTeX bereitstellen willst, kannst du in deinem Repo unter `docs/`
  die Dateien ablegen und GitHub Pages aktivieren. Auf dem Poster den Pages-Link nutzen.

## Warum keine QR-Shortener?
QR-Codes selbst sind kostenlos – problematisch sind **Link-Shortener** mit Ablauf/Limits.
Nutze stattdessen **DOI-Links** (`https://doi.org/...`) oder deinen **permanenten App-/Pages-Link**.

