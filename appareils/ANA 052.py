
"""Fiche technique du calorimètre à bombe à oxygène Parr 6200."""

FICHE = {
    "nom": "Calorimètre à bombe — Parr 6200",

    "description": (
        "Le Parr 6200 est un calorimètre à bombe à oxygène destiné "
        "à la détermination expérimentale du pouvoir calorifique "
        "supérieur (PCS/HHV) de combustibles solides et liquides, "
        "notamment les biomasses, les hydrochars, les biochars, "
        "les biohuiles et les combustibles issus de la valorisation "
        "des déchets.\n\n"

        "Son principe de fonctionnement repose sur la combustion "
        "complète d'un échantillon placé dans une bombe calorimétrique "
        "étanche sous atmosphère d'oxygène pressurisé. L'énergie "
        "thermique libérée est déterminée à partir de l'élévation "
        "de température du système calorimétrique, en tenant compte "
        "de sa capacité calorifique préalablement étalonnée et "
        "des corrections expérimentales nécessaires.\n\n"

        "Cet équipement permet notamment :\n"
        "• La caractérisation énergétique des combustibles conventionnels et alternatifs.\n"
        "• L'évaluation du potentiel énergétique des biomasses brutes et prétraitées.\n"
        "• L'analyse des produits issus de la pyrolyse, de la torréfaction et de la carbonisation hydrothermale.\n"
        "• La comparaison des propriétés énergétiques des matériaux "
        "issus de différents procédés de valorisation.\n"
        "• La détermination du PCS et l'estimation du pouvoir calorifique inférieur (PCI/LHV) à partir de la composition "
        "élémentaire, notamment de la teneur en hydrogène, en tenant compte de l'humidité et de la base de calcul retenue."
    ),

    "utilisation": (
        "1. PRÉPARATION DE L'ÉCHANTILLON :"
        "Homogénéiser si nécessaire le matériau à analyser, "
        "puis prélever et peser avec précision une quantité "
        "représentative dans un creuset adapté.\n"

        "2. PRÉPARATION DE LA BOMBE CALORIMÉTRIQUE :"
        "Installer le creuset, mettre en place le dispositif "
        "d'allumage et vérifier la propreté ainsi que "
        "l'étanchéité des composants.\n"

        "3. MISE SOUS OXYGÈNE :"
        "Fermer hermétiquement la bombe et procéder au "
        "remplissage en oxygène selon les prescriptions "
        "du constructeur et les consignes de sécurité.\n"

        "4. INSTALLATION ET LANCEMENT DE L'ESSAI :"
        "Positionner la bombe dans le calorimètre, configurer "
        "les paramètres de mesure et démarrer le cycle d'analyse.\n"

        "5. COMBUSTION ET ACQUISITION :"
        "Réaliser l'allumage de l'échantillon et enregistrer "
        "l'évolution de la température jusqu'à la fin du cycle "
        "de mesure.\n"

        "6. TRAITEMENT DES RÉSULTATS :"
        "Déterminer le PCS à partir des données calorimétriques, "
        "de l'étalonnage et des corrections applicables.\n"

        "7. FIN D'ESSAI ET CONTRÔLE :"
        "Retirer la bombe, dépressuriser conformément aux "
        "consignes de sécurité, inspecter les résidus de "
        "combustion, nettoyer les composants et vérifier "
        "la validité de l'essai.\n"

        "8. EXPLOITATION DES DONNÉES :"
        "Exprimer le PCS dans l'unité et sur la base massique "
        "appropriées, par exemple en MJ/kg sur brut ou sur sec. "
        "Calculer le PCI lorsque les données de composition "
        "nécessaires sont disponibles."
    ),

    "protocole": (
        "1. Préparation et pesée de l'échantillon : 5 min.\n"
        "2. Préparation, fermeture et installation de la bombe : 5 min.\n"
        "3. Combustion et acquisition des données : 5 min.\n"
        "4. Dépressurisation, inspection et nettoyage : 5 min.\n"
        "5. Traitement et validation des résultats : 5 min.\n\n"

        "DURÉE TOTALE ESTIMÉE : 25 minutes.\n"
        "DURÉE DE RÉFÉRENCE : 25 minutes par essai.\n"
        "PRÉSENCE OPÉRATEUR : 25 minutes par essai (valeur indicative).\n"
        "INTERVENTION TECHNICIEN : maintenance 1 heure pour environ 60 essai (donc 1 min/essai).\n\n"

        "Les durées peuvent varier selon la nature, la préparation et le comportement à la combustion de l'échantillon.\n\n"

        "Les temps indiqués ne comprennent pas les opérations complémentaires éventuelles : séchage, broyage, étalonnage initial, répétitions ou préparations "
        "spécifiques.\n\n"

        "Les essais doivent être réalisés conformément "
        "aux procédures internes du laboratoire, aux "
        "prescriptions du fabricant et aux méthodes "
        "normalisées applicables au combustible analysé."
    ),

    # Durées de référence utilisées pour le chiffrage
    "duree_essai_h": 0.42,
    "presence_operateur_h": 0.42,

    # Photographies de l'appareil
    # Chemins relatifs au dossier principal de l'application
    "photos_fichiers": [
        "images/ANA 052.jpg",
        "images/ANA 052 (1).jpg",
        "images/ANA 052 (2).jpg",
    ],

    # Coûts de référence par essai
    "couts_defaut": {
        "ingenieur_h": 0.42,
        "technicien_h": 0.02,
        "consommables_eur": 0.0,
        "energie_kwh": 0.0,
    },
}
