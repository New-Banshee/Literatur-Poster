import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Poster-Literaturliste", page_icon="📚")

# --- Einleitung --------------------------------------------------------------
st.markdown("""
**Willkommen zu der Literaturliste zum Thema:**

### Pflegerische Unterstützungsbedarfe von An- und Zugehörigen ehemaliger Intensivpatientinnen und –patienten nach erfolgreicher eCPR

**Autorin:** Jennifer, Zimmermann B. Sc.
""")

# --- Daten laden -------------------------------------------------------------
DATA_PATH = Path("data/references.json")

@st.cache_data
def load_refs(path: Path):
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Fehler beim Einlesen: {e}")
        return []

refs = load_refs(DATA_PATH)

# --- Prüfung, ob Daten vorhanden sind ----------------------------------------
if not refs:
    st.error("Die Datei 'data/references.json' fehlt oder ist leer.")
    st.stop()

# --- Vollständige Nachweise --------------------------------------------------
for r in refs:
    st.write(f"**[{r.get('id','?')}] {r.get('short','')}**")
    st.write(r.get("full", "—"))
    url = r.get("url")
    if url:
        st.markdown(f"[DOI/Link]({url})")
    st.markdown("---")
