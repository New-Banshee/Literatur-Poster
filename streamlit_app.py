
import json
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Poster-Literaturliste", page_icon="📚")

# ---- Einleitung -------------------------------------------------------------
st.markdown("""
**Willkommen zu der Literaturliste zum Thema:**

### Pflegerische Unterstützungsbedarfe von An- und Zugehörigen ehemaliger Intensivpatientinnen und –patienten nach erfolgreicher eCPR

**Autorin:** Jennifer Zimmermann, B. Sc.
""")

# ---- Daten laden ------------------------------------------------------------
@st.cache_data
def load_refs(path="data/references.json"):
    p = Path(path)
    if not p.exists():
        st.error(f"Die Datei {path} fehlt.")
        return []
    return json.loads(p.read_text(encoding="utf-8"))

refs = load_refs()
if not refs:
    st.stop()

# ---- Vollständiger Nachweis---------------------------
for r in refs:
    st.write(f"**[{r.get('id','?')}] {r.get('short','')}**")
    st.write(r.get("full", "—"))
    url = r.get("url")
    if url:
        st.markdown(f"[DOI/Link]({url})")
    st.markdown("---")

st.caption("")

@st.cache_data
def load_refs():
    with open("data/references.json", "r", encoding="utf-8") as f:
        return json.load(f)

refs = load_refs()



