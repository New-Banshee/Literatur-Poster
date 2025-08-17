
import json
import streamlit as st

st.set_page_config(page_title="Poster-Literaturliste", page_icon="📚")

# ------------------------------------------------------------------
# Einleitung (genau wie gewünscht)
st.markdown("""
**Willkommen zu der Literaturliste zum Thema:**

### Pflegerische Unterstützungsbedarfe von An- und Zugehörigen ehemaliger Intensivpatientinnen und –patienten nach erfolgreicher eCPR

**Autorin:** Mein Name
""")
# ------------------------------------------------------------------

st.caption("Hinweis: Verlinke am besten direkt auf DOI-URLs (dauerhaft), statt Shortener zu benutzen.")

@st.cache_data
def load_refs():
    with open("data/references.json", "r", encoding="utf-8") as f:
        return json.load(f)

refs = load_refs()

# --- Liste (kompakt) ---------------------------------------------------------
st.subheader("Kurzübersicht (fürs Poster)")
compact_lines = [f"[{r['id']}] {r['short']}" for r in refs]
compact_block = "\n".join(compact_lines)
st.code(compact_block, language="text")
st.download_button("⬇️ Kurzübersicht als TXT", compact_block.encode("utf-8"), file_name="poster_shortlist.txt")

# --- Vollständige Nachweise --------------------------------------------------
st.divider()
st.subheader("Vollständige Nachweise mit DOI/Links")
for r in refs:
    with st.expander(f"[{r['id']}] {r['short']}"):
        st.write(r["full"])
        if r.get("url"):
            st.write(f"**DOI/Link:** {r['url']}")
            st.link_button("Aufrufen", r["url"], use_container_width=True)
        else:
            st.info("Kein DOI/Link angegeben.")
