"""Application Streamlit de chiffrage de prestations expérimentales DSEE.
Lancer : streamlit run app.py
Tarifs et équipements fournis à titre d'exemple et modifiables.
"""
from __future__ import annotations

from datetime import date
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from pathlib import Path
from html import escape
import importlib
import pkgutil
import sys
import appareils
import json
import re
import unicodedata

import pandas as pd
import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

st.set_page_config(page_title="DSEE | Chiffrage des essais", page_icon="🧪", layout="wide")

# Chaque appareil est défini exclusivement dans appareils/*.py.
# Ajouter un fichier contenant FICHE suffit à enrichir le catalogue.
def charger_appareils() -> dict:
    catalogue = {}
    for info in pkgutil.iter_modules(appareils.__path__):
        if info.name.startswith("_"):
            continue
        nom_module = f"appareils.{info.name}"
        try:
            if nom_module in sys.modules:
                module = importlib.reload(sys.modules[nom_module])
            else:
                module = importlib.import_module(nom_module)
        except Exception as exc:
            st.warning(f"Impossible de charger {info.name}.py : {exc}")
            continue
        fiche = getattr(module, "FICHE", None)
        if not isinstance(fiche, dict):
            continue
        nom = fiche.get("nom")
        if not nom:
            st.warning(f"Fiche ignorée : {info.name}.py (nom manquant).")
            continue
        if nom in catalogue:
            st.warning(f"Nom d'appareil en double : {nom}")
            continue
        catalogue[nom] = {**fiche, "_module_path": str(Path(module.__file__).resolve())}
    return catalogue


def trouver_photo(chemin: str, fiche: dict) -> Path:
    """Résout les photos depuis la racine du projet ou le dossier de l'appareil."""
    fichier = Path(str(chemin))
    if fichier.is_absolute():
        return fichier
    racine = Path(__file__).resolve().parent
    module = Path(fiche.get("_module_path", racine / "appareils" / "__init__.py"))
    candidats = [racine / fichier, module.parent / fichier]
    if fichier.parts and fichier.parts[0] == "images":
        candidats.append(module.parent / fichier.name)
    candidats.append(racine / "images" / fichier.name)
    return next((p for p in candidats if p.is_file()), candidats[0])


CATALOGUE = charger_appareils()
DOCUMENTATION = CATALOGUE
EXEMPLES = {
    nom: {
        cle: float(fiche.get("couts_defaut", {}).get(cle, 0.0))
        for cle in ("ingenieur_h", "technicien_h", "consommables_eur", "energie_kwh")
    }
    for nom, fiche in CATALOGUE.items()
}

DEFAULTS = {"tarif_ingenieur": 85.0, "tarif_technicien": 55.0, "tarif_kwh": 0.22, "frais_generaux_pct": 15.0, "marge_pct": 20.0, "tva_pct": 20.0}


def euros(x: float) -> str:
    return f"{x:,.2f}".replace(",", " ").replace(".", ",") + " €"


def safe_filename(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", s).strip("_") or "devis"


def pdf_devis(meta: dict, df: pd.DataFrame, totaux: dict) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=18*mm, bottomMargin=16*mm)
    styles = getSampleStyleSheet()
    story = [Paragraph("DSEE - Devis de prestations experimentales", styles["Title"]), Spacer(1, 8*mm)]
    for key, value in [("Reference", meta["reference"]), ("Date", meta["date"]), ("Client", meta["client"]), ("Projet", meta["projet"])]:
        story.append(Paragraph(f"<b>{key} :</b> {str(value).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')}", styles["Normal"]))
    story.append(Spacer(1, 8*mm))
    rows = [["Essai / appareil", "Qte", "Cout unitaire HT", "Total direct HT"]]
    for _, r in df.iterrows():
        rows.append([Paragraph(escape(str(r["Essai / appareil"])), styles["BodyText"]), str(int(r["Quantité"])), euros(r["Coût direct unitaire HT (€)"]), euros(r["Coût direct total HT (€)"])])
    table = Table(rows, colWidths=[73*mm, 14*mm, 44*mm, 47*mm], repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([("BACKGROUND", (0,0),(-1,0),colors.HexColor("#183153")), ("TEXTCOLOR",(0,0),(-1,0),colors.white), ("VALIGN",(0,0),(-1,-1),"TOP"), ("GRID",(0,0),(-1,-1),0.3,colors.HexColor("#cbd5e1")), ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#f1f5f9")]), ("BOTTOMPADDING",(0,0),(-1,-1),7), ("TOPPADDING",(0,0),(-1,-1),7)]))
    story.extend([table, Spacer(1, 7*mm)])
    for label, key in [("Couts directs", "direct"), ("Frais generaux", "frais"), ("Prix de revient", "revient"), ("Marge commerciale", "marge"), ("Prix de vente HT", "ht"), ("TVA", "tva"), ("Prix TTC", "ttc")]:
        story.append(Paragraph(f"<b>{label} :</b> {euros(totaux[key])}", styles["Normal"]))
        story.append(Spacer(1, 2*mm))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Document de simulation. Validation et conditions commerciales a confirmer avant emission officielle.", styles["Italic"]))
    doc.build(story)
    return buffer.getvalue()


st.title("🧪 DSEE — Chiffrage des essais et devis")
st.caption("Outil de simulation pour laboratoire de recherche : les tarifs et temps préchargés sont fictifs et entièrement modifiables.")

# Réinitialiser uniquement les anciennes sélections devenues invalides.
# Les données techniques sont toujours relues depuis les modules Python.
if "selection" not in st.session_state:
    st.session_state.selection = []
else:
    st.session_state.selection = [
        nom for nom in st.session_state.selection if nom in CATALOGUE
    ]

with st.sidebar:
    st.header("⚙️ Paramètres économiques")
    tarif_ing = st.number_input("Coût horaire ingénieur (€/h)", min_value=0.0, value=DEFAULTS["tarif_ingenieur"], step=5.0)
    tarif_tech = st.number_input("Coût horaire technicien (€/h)", min_value=0.0, value=DEFAULTS["tarif_technicien"], step=5.0)
    tarif_kwh = st.number_input("Coût de l'énergie (€/kWh)", min_value=0.0, value=DEFAULTS["tarif_kwh"], step=0.01, format="%.3f")
    frais_pct = st.number_input("Frais généraux (%)", min_value=0.0, max_value=500.0, value=DEFAULTS["frais_generaux_pct"], step=1.0)
    marge_pct = st.number_input("Marge sur prix de revient (%)", min_value=0.0, max_value=500.0, value=DEFAULTS["marge_pct"], step=1.0)
    tva_pct = st.number_input("TVA (%)", min_value=0.0, max_value=100.0, value=DEFAULTS["tva_pct"], step=1.0)
    st.info("La marge est ici une majoration du prix de revient (markup), pas un taux de marque sur le prix de vente.")

st.subheader("1. Informations du devis")
c1, c2, c3 = st.columns(3)
with c1:
    client = st.text_input("Client", placeholder="Nom du client")
with c2:
    projet = st.text_input("Projet / objet du devis", placeholder="Campagne d'essais")
with c3:
    reference = st.text_input("Référence", value=f"DSEE-{date.today():%Y%m%d}-001")

if "message_creation" in st.session_state:
    st.success(st.session_state.pop("message_creation"))

st.subheader("2. Sélection des appareils et bancs")

# ==========================================================
# CRÉATION D'UNE NOUVELLE FICHE APPAREIL
# Chaque création écrit un module .py dans appareils/.
# ==========================================================

def nom_fichier_appareil(nom: str) -> str:
    ascii_nom = unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "_", ascii_nom.lower()).strip("_")
    return (slug[:70] or "appareil") + ".py"

# Appliquer la sélection au début de l'exécution, avant le multiselect.
if "selection_a_appliquer" in st.session_state:
    st.session_state.selection = [
        nom for nom in st.session_state.pop("selection_a_appliquer")
        if nom in CATALOGUE
    ]

col_selection, col_creation = st.columns([4, 1], gap="medium", vertical_alignment="top")

with col_selection:
    selection = st.multiselect(
        "Sélectionner un ou plusieurs essais",
        options=list(CATALOGUE),
        key="selection",
    )

with col_creation:
    st.markdown("Créer un nouvel appareil / essai")
    with st.popover("➕ Nouvel appareil", use_container_width=True):
        st.caption("Crée une fiche technique avec sa photo et ses coûts de référence. Elle sera ajoutée au catalogue.")
        with st.form("creation_appareil", clear_on_submit=False):
            nouveau_nom = st.text_input("Nom de l'appareil / essai *")
            nouveau_description = st.text_area("Description de l'appareil *", height=100)
            nouveau_utilisation = st.text_area("Mode d'utilisation", height=110)
            nouveau_protocole = st.text_area("Protocole / étapes de l'essai", height=100)
            nouvelles_photos = st.file_uploader("Photos de l'appareil (JPG ou PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=True, help="Sélectionnez plusieurs images (5 Mo maximum par photo).")
            d1, d2 = st.columns(2)
            with d1:
                nouveau_duree = st.number_input("Durée totale d'un essai (h)", min_value=0.0, value=1.0, step=0.25)
            with d2:
                nouveau_presence = st.number_input("Présence de l'opérateur (h)", min_value=0.0, value=0.5, step=0.25)
            st.markdown("**Coûts de référence par essai**")
            n1, n2 = st.columns(2)
            with n1:
                nouveau_ing = st.number_input("Temps ingénieur (h)", min_value=0.0, value=0.0, step=0.25)
                nouveau_cons = st.number_input("Consommables (€)", min_value=0.0, value=0.0, step=1.0)
            with n2:
                nouveau_tech = st.number_input("Temps technicien (h)", min_value=0.0, value=0.0, step=0.25)
                nouveau_energie = st.number_input("Énergie (kWh)", min_value=0.0, value=0.0, step=1.0)
            enregistrer = st.form_submit_button("💾 Créer l'appareil", type="primary")

        if enregistrer:
            nouveau_nom = nouveau_nom.strip()
            chemin_module = Path(__file__).resolve().parent / "appareils" / nom_fichier_appareil(nouveau_nom)
            if not nouveau_nom or not nouveau_description.strip():
                st.error("Le nom et la description sont obligatoires.")
            elif nouveau_nom.casefold() in {n.casefold() for n in CATALOGUE} or chemin_module.exists():
                st.error("Cet appareil ou ce nom de fichier existe déjà.")
            elif nouveau_presence > nouveau_duree:
                st.error("La présence de l'opérateur ne peut pas dépasser la durée totale de l'essai.")
            else:
                dossier_base = Path(__file__).resolve().parent
                photos_a_enregistrer = []
                erreur_photo = None
                for numero, photo in enumerate(nouvelles_photos or [], start=1):
                    donnees = photo.getvalue()
                    if len(donnees) > 5 * 1024 * 1024:
                        erreur_photo = f"La photo {photo.name} dépasse 5 Mo."
                        break
                    try:
                        with Image.open(BytesIO(donnees)) as img:
                            img.verify()
                        with Image.open(BytesIO(donnees)) as img:
                            format_image = img.format
                            img.load()
                    except (UnidentifiedImageError, OSError, ValueError):
                        erreur_photo = f"Image invalide : {photo.name}"
                        break
                    if format_image not in ("JPEG", "PNG"):
                        erreur_photo = f"Format non autorisé : {photo.name}"
                        break
                    extension = ".jpg" if format_image == "JPEG" else ".png"
                    chemin_relatif = f"images/{chemin_module.stem}_{numero:02d}{extension}"
                    photos_a_enregistrer.append((chemin_relatif, donnees))

                if erreur_photo:
                    st.error(erreur_photo)
                    st.stop()

                chemins_photos = [chemin for chemin, _ in photos_a_enregistrer]
                fiche_nouvelle = {
                    "nom": nouveau_nom,
                    "description": nouveau_description.strip(),
                    "utilisation": nouveau_utilisation.strip(),
                    "protocole": nouveau_protocole.strip(),
                    "duree_essai_h": float(nouveau_duree),
                    "presence_operateur_h": float(nouveau_presence),
                    "photos_fichiers": chemins_photos,
                    "photo_fichier": chemins_photos[0] if chemins_photos else "",
                    "couts_defaut": {
                        "ingenieur_h": float(nouveau_ing),
                        "technicien_h": float(nouveau_tech),
                        "consommables_eur": float(nouveau_cons),
                        "energie_kwh": float(nouveau_energie),
                    },
                }
                try:
                    chemin_module.parent.mkdir(parents=True, exist_ok=True)
                    for chemin_relatif, donnees in photos_a_enregistrer:
                        destination = dossier_base / chemin_relatif
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        destination.write_bytes(donnees)
                    # repr() crée un littéral Python sûr, sans exécuter le texte utilisateur.
                    chemin_module.write_text(
                        '# Fiche appareil générée depuis Streamlit.\nFICHE = ' + repr(fiche_nouvelle) + '\n',
                        encoding="utf-8"
                    )
                except OSError as exc:
                    st.error(f"Enregistrement impossible : {exc}")
                else:
                    importlib.invalidate_caches()
                    st.session_state.selection_a_appliquer = [nouveau_nom]
                    st.session_state.message_creation = (
                        f"Appareil créé avec succès : {nouveau_nom}"
                    )
                    st.rerun()

st.caption("Sur Streamlit Community Cloud, les fichiers créés sur le serveur peuvent disparaître au redéploiement : ajoute les nouveaux modules et photos à GitHub pour les conserver.")
if not CATALOGUE:
    st.info("Aucun appareil enregistré. Utilisez le formulaire de création ci-dessus.")

lignes = []
for idx, nom in enumerate(selection):
    defaults = EXEMPLES[nom]
    with st.expander(f"🔬 {nom}", expanded=True):
        fiche = DOCUMENTATION[nom]
        with st.expander("📖 Description de l'appareil / fiche d'essai"):
            st.subheader(nom)
            chemins_photos = fiche.get("photos_fichiers") or []
            if isinstance(chemins_photos, str):
                chemins_photos = [chemins_photos] if chemins_photos else []
            if not chemins_photos:
                ancien_chemin = fiche.get("photo_fichier") or fiche.get("image")
                chemins_photos = [ancien_chemin] if ancien_chemin else []

            if chemins_photos:
                for debut in range(0, len(chemins_photos), 3):
                    colonnes_photos = st.columns(3)
                    for colonne, chemin_photo in zip(colonnes_photos, chemins_photos[debut:debut + 3]):
                        with colonne:
                            image_path = trouver_photo(chemin_photo, fiche)
                            if not image_path.is_file():
                                st.info(f"Photo absente : {chemin_photo} — vérifier le chemin indiqué dans appareils/{Path(fiche.get('_module_path', "appareil.py")).name}")
                                continue
                            try:
                                with Image.open(image_path) as img:
                                    img.load()
                                    image_valide = img.copy()
                                st.image(image_valide, caption=nom, use_container_width=True)
                            except (UnidentifiedImageError, OSError, ValueError):
                                st.warning(f"Photo illisible : {chemin_photo}")
            else:
                st.info("Aucune photo renseignée dans la fiche Python.")

            st.markdown("**Description de l'appareil**")
            st.write(fiche.get("description", "Description non renseignée."))
            st.markdown("**Mode d'utilisation**")
            st.text(fiche.get("utilisation") or fiche.get("protocole", "Non renseigné."))
            if fiche.get("utilisation") and fiche.get("protocole"):
                st.markdown("**Protocole et temps indicatifs**")
                texte = fiche["protocole"].replace("\n", "  \n")
                st.markdown(texte)
            d1, d2 = st.columns(2)
            d1.metric("Durée totale d'un essai", f'{float(fiche.get("duree_essai_h", 0)):g} h')
            d2.metric("Présence devant l'appareil", f'{float(fiche.get("presence_operateur_h", 0)):g} h')
            st.caption("Durée de l'essai, présence opérateur et temps facturés sont distincts.")

        st.caption(f'Durée de référence : {float(fiche.get("duree_essai_h", 0)):g} h par essai · Présence devant l’appareil : {float(fiche.get("presence_operateur_h", 0)):g} h par essai')
        a, b, c = st.columns(3)
        with a:
            qte = st.number_input("Nombre d'essais", min_value=1, value=1, step=1, key=f"qte_{nom}")
            h_ing = st.number_input("Temps ingénieur par essai (h)", min_value=0.0, value=float(defaults["ingenieur_h"]), step=0.5, key=f"ing_{nom}")
        with b:
            h_tech = st.number_input("Temps technicien par essai (h)", min_value=0.0, value=float(defaults["technicien_h"]), step=0.5, key=f"tech_{nom}")
            consommables = st.number_input("Consommables par essai (€)", min_value=0.0, value=float(defaults["consommables_eur"]), step=10.0, key=f"cons_{nom}")
        with c:
            kwh = st.number_input("Énergie par essai (kWh)", min_value=0.0, value=float(defaults["energie_kwh"]), step=10.0, key=f"kwh_{nom}")
            tarif_equipement = st.number_input("Autres coûts appareil / essai (€)", min_value=0.0, value=0.0, step=10.0, key=f"equip_{nom}")
        cout_ing = h_ing * tarif_ing
        cout_tech = h_tech * tarif_tech
        cout_energie = kwh * tarif_kwh
        direct_unitaire = cout_ing + cout_tech + consommables + cout_energie + tarif_equipement
        st.caption(f"Coût direct unitaire : ingénieur {euros(cout_ing)} + technicien {euros(cout_tech)} + consommables {euros(consommables)} + énergie {euros(cout_energie)} + autres {euros(tarif_equipement)} = **{euros(direct_unitaire)}**")
        lignes.append({"Essai / appareil": nom, "Quantité": qte, "Durée essai (h/essai)": float(fiche.get("duree_essai_h", 0)), "Présence devant appareil (h/essai)": float(fiche.get("presence_operateur_h", 0)), "Ingénieur (h/essai)": h_ing, "Technicien (h/essai)": h_tech, "Ingénieur (€ / essai)": cout_ing, "Technicien (€ / essai)": cout_tech, "Consommables (€ / essai)": consommables, "Énergie (kWh / essai)": kwh, "Énergie (€ / essai)": cout_energie, "Autres coûts (€ / essai)": tarif_equipement, "Coût direct unitaire HT (€)": direct_unitaire, "Coût direct total HT (€)": direct_unitaire*qte})

st.subheader("3. Synthèse financière")
if not lignes:
    st.warning("Sélectionnez au moins un essai pour établir un devis.")
    st.stop()

df = pd.DataFrame(lignes)
direct = float(df["Coût direct total HT (€)"].sum())
frais = direct * frais_pct / 100
revient = direct + frais
marge = revient * marge_pct / 100
ht = revient + marge
tva = ht * tva_pct / 100
ttc = ht + tva
totaux = {"direct": direct, "frais": frais, "revient": revient, "marge": marge, "ht": ht, "tva": tva, "ttc": ttc}

m1,m2,m3,m4 = st.columns(4)
m1.metric("Coûts direct", euros(direct))
m2.metric("Prix de revient", euros(revient))
m3.metric("Prix de vente HT", euros(ht))
m4.metric("Prix TTC", euros(ttc))

st.dataframe(df, use_container_width=True, hide_index=True)
resume = pd.DataFrame([{"Poste": "Coûts directs", "Montant (€)": direct}, {"Poste": f"Frais généraux ({frais_pct:g} %)", "Montant (€)": frais}, {"Poste": "Prix de revient", "Montant (€)": revient}, {"Poste": f"Marge ({marge_pct:g} %)", "Montant (€)": marge}, {"Poste": "Prix de vente HT", "Montant (€)": ht}, {"Poste": f"TVA ({tva_pct:g} %)", "Montant (€)": tva}, {"Poste": "Prix TTC", "Montant (€)": ttc}])
st.dataframe(resume, use_container_width=True, hide_index=True)

st.subheader("4. Exporter le devis")
meta = {"reference": reference, "date": date.today().strftime("%d/%m/%Y"), "client": client or "Non renseigné", "projet": projet or "Non renseigné"}
col_pdf, col_csv, col_json = st.columns(3)
with col_pdf:
    st.download_button("📄 Télécharger le devis PDF", data=pdf_devis(meta, df, totaux), file_name=f"{safe_filename(reference)}.pdf", mime="application/pdf", use_container_width=True)
with col_csv:
    st.download_button("📊 Télécharger le détail CSV", data=df.to_csv(index=False, sep=";", decimal=",").encode("utf-8-sig"), file_name=f"{safe_filename(reference)}_detail.csv", mime="text/csv", use_container_width=True)
with col_json:
    payload = {"devis": meta, "parametres": {"tarif_ingenieur": tarif_ing, "tarif_technicien": tarif_tech, "tarif_kwh": tarif_kwh, "frais_pct": frais_pct, "marge_pct": marge_pct, "tva_pct": tva_pct}, "lignes": lignes, "documentation": {nom: {k: v for k, v in DOCUMENTATION[nom].items() if not k.startswith("_")} for nom in selection}, "totaux": totaux}
    st.download_button("💾 Télécharger les données JSON", data=json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8"), file_name=f"{safe_filename(reference)}.json", mime="application/json", use_container_width=True)

st.caption("Application de chiffrage indicative : vérifier les règles de facturation, de TVA et les tarifs internes avant d'envoyer un devis contractuel.")

# Les fiches sont en lecture seule et proviennent exclusivement de appareils/*.py.
# Modifier les fiches directement dans leurs modules, puis redémarrer Streamlit.
