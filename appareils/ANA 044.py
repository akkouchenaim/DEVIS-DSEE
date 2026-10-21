
"""Fiche technique de l'analyseur élémentaire Thermo Finnigan FLASH EA 1112."""

FICHE = {
    "nom": "Analyseur élémentaire — CHNS",

    "description": (
        "L'analyseur élémentaire Thermo Finnigan FLASH EA 1112 est un "
        "équipement analytique destiné à la détermination quantitative "
        "de la composition élémentaire des matériaux solides et liquides, "
        "notamment les teneurs massiques en carbone (C), hydrogène (H), "
        "azote (N) et soufre (S). Selon la configuration instrumentale, "
        "il permet également la détermination directe de l'oxygène (O) "
        "par pyrolyse.\n\n"

        "L'analyse CHNS repose sur le principe de la combustion éclair "
        "(Flash Combustion). Un échantillon de faible masse est introduit "
        "dans un réacteur à haute température sous apport contrôlé "
        "d'oxygène. Les gaz formés sont ensuite traités, séparés par "
        "chromatographie gazeuse et quantifiés à l'aide d'un détecteur "
        "à conductivité thermique (TCD).\n\n"

        "La détermination directe de l'oxygène nécessite une configuration "
        "spécifique fonctionnant par pyrolyse sous atmosphère inerte. "
        "En l'absence de cette configuration, la teneur en oxygène peut "
        "être estimée par différence en tenant compte des autres "
        "constituants du matériau.\n\n"

        "Cet équipement permet notamment :\n"
        "• La caractérisation élémentaire des biomasses, biochars, "
        "hydrochars, biohuiles et combustibles alternatifs.\n"
        "• L'étude des transformations chimiques induites par la pyrolyse, "
        "la torréfaction et la carbonisation hydrothermale.\n"
        "• La détermination des rapports atomiques H/C et O/C pour "
        "l'analyse du degré de carbonisation.\n"
        "• L'évaluation de la composition chimique de combustibles "
        "et de matières premières.\n"
        "• L'exploitation des résultats pour les bilans de matière, "
        "les études de combustion et les procédés de valorisation énergétique."
    ),

    "utilisation": (
        "1. PRÉPARATION DE L'APPAREIL\n"
        "Vérifier l'état général du système, les alimentations en gaz, "
        "les températures de fonctionnement, les réacteurs, le détecteur "
        "et la validité de l'étalonnage.\n\n"

        "2. PRÉPARATION DE L'ÉCHANTILLON\n"
        "Homogénéiser puis peser précisément une faible quantité de matériau, "
        "généralement de l'ordre de 0,5 à 1 mg pour la méthode CHNS "
        "considérée, dans une capsule en étain adaptée.\n\n"

        "3. COMBUSTION ÉCLAIR\n"
        "Introduire automatiquement l'échantillon dans le réacteur "
        "porté à environ 900 °C. L'apport d'oxygène déclenche une "
        "combustion rapide dans les conditions de la méthode analytique.\n\n"

        "4. SÉPARATION ET DÉTECTION\n"
        "Traiter et séparer les gaz produits par la combustion, "
        "puis mesurer leur réponse à l'aide du détecteur "
        "à conductivité thermique (TCD).\n\n"

        "5. DÉTERMINATION DE L'OXYGÈNE\n"
        "Lorsque l'appareil dispose du module approprié, réaliser "
        "une analyse spécifique par pyrolyse sous atmosphère inerte, "
        "avec une capsule en argent et une température voisine "
        "de 1 070 °C, conformément à la méthode validée.\n\n"

        "6. VALIDATION DES RÉSULTATS\n"
        "Contrôler les blancs, les matériaux de référence, "
        "la répétabilité des mesures et la cohérence "
        "des résultats analytiques.\n\n"

        "7. EXPLOITATION DES DONNÉES\n"
        "Déterminer les teneurs massiques des éléments analysés, "
        "calculer éventuellement les rapports atomiques H/C et O/C, "
        "puis exporter les résultats."
    ),

    "protocole": (
        "PROTOCOLE EXPÉRIMENTAL ET TEMPS INDICATIFS\n\n"

        "1. Maintenance courante et préparation de l'appareil : 60 minutes pour une série de 30 échantillons.\n"
        "2. Préparation et pesée de l'échantillon : 5 minutes par échantillon.\n"
        "3. Analyse CHNS automatisée : 10 minutes par échantillon.\n"
        "4. Traitement et validation des résultats : 5 minutes par échantillon.\n\n"

        "DURÉE TOTALE ESTIMÉE : 20 minutes par essai, hors maintenance mutualisée.\n"
        "MAINTENANCE : 2 minute par essai (60 minutes réparties sur 30 échantillon).\n\n"

        "CONSOMMATIONS INDICATIVES\n\n"
        "• Consommation électrique : 0,5 kWh par essai.\n"
        "• Consommation de gaz : 500 mL par essai (valeur à confirmer selon le gaz et la configuration).\n\n"
    ),

    # ======================================================
    # DURÉES DE RÉFÉRENCE
    # ======================================================

    # 20 minutes = 0,33 heure
    "duree_essai_h": 20/60,

    # Temps opérateur à adapter aux pratiques du laboratoire.
    # Valeur indicative : 10 minutes
    "presence_operateur_h": 10/60,

    # ======================================================
    # PHOTOGRAPHIES DE L'APPAREIL
    # ======================================================

    "photos_fichiers": [
        "images/ANA 044.jpg",
        "images/ANA 044 (1).jpg",
        "images/ANA 044 (2).jpg",
        "images/ANA 044 (3).jpg"
    ],

    # ======================================================
    # COÛTS DE RÉFÉRENCE PAR ESSAI
    # ======================================================

    "couts_defaut": {
        "ingenieur_h": 10/60,

        # Temps indicatif, maintenance comprise si approprié
        "technicien_h": 2/60,

        "consommables_eur": 0.0,

        # Consommation énergétique par essai
        "energie_kwh": 0.5,
    },
}
