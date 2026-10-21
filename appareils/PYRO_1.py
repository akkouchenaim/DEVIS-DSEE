
"""Fiche technique du pyrolyseur discontinu (Batch) à 700 °C."""

FICHE = {
    "nom": "Pyrolyseur PYRO 1 — Pyrolyse lente",

    "description": (
        "Le pyrolyseur PYRO 1 est un pyrolyseur discontinu (Batch) "
        "destinée à l'étude de la décomposition thermochimique des matières "
        "organiques, notamment les biomasses et les résidus issus de leur "
        "valorisation, sous atmosphère contrôlée et en absence d'oxygène.\n\n"

        "L'appareil est constitué d'un réacteur cylindrique de 10 cm de "
        "diamètre et de 24 cm de hauteur, correspondant à un volume "
        "géométrique théorique d'environ 1,9 litres. Il est équipé "
        "d'un système de chauffage électrique permettant d'atteindre "
        "une température maximale de 700 °C.\n\n"

        "Le système de régulation thermique permet de programmer "
        "la vitesse de montée en température (°C/min), de fixer "
        "une température cible et de maintenir le réacteur à "
        "une température constante pendant une durée définie. "
        "Cette flexibilité permet d'étudier l'influence des paramètres "
        "thermiques sur la décomposition de la matière et sur "
        "la distribution des produits de pyrolyse.\n\n"

        "La partie supérieure du réacteur, destinée à l'évacuation "
        "des vapeurs de pyrolyse, est équipée de résistances "
        "électriques assurant un chauffage indépendant. "
        "Ce dispositif permet de limiter la condensation prématurée "
        "des vapeurs et leur dépôt dans la conduite de sortie.\n\n"

        "Cette zone chauffée peut également recevoir un lit catalytique "
        "destiné au craquage secondaire des vapeurs de pyrolyse. "
        "L'utilisation de différents matériaux catalytiques permet "
        "d'étudier leur influence sur la conversion des composés "
        "organiques lourds, la formation de gaz légers et "
        "l'amélioration de la qualité des produits obtenus.\n\n"

        "À la sortie du réacteur, les vapeurs traversent deux "
        "condenseurs montés en série permettant leur refroidissement "
        "progressif. La température du second condenseur peut être "
        "abaissée jusqu'à 5 °C afin de favoriser la récupération "
        "des fractions condensables.\n\n"

        "Les liquides condensés, constitués notamment de biohuiles "
        "et de fractions aqueuses, sont collectés séparément "
        "pour leur quantification et leur caractérisation "
        "physico-chimique.\n\n"

        "Les gaz non condensables sont dirigés vers un "
        "microchromatographe en phase gazeuse (micro-GC) afin "
        "d'analyser leur composition, ou vers un réservoir "
        "de collecte permettant leur stockage temporaire et "
        "leur quantification à l'aide d'un dispositif adapté.\n\n"

        "Cet équipement permet notamment :\n"
        "• L'étude de la pyrolyse thermique de différentes biomasses.\n"
        "• L'évaluation de l'influence de la température finale de pyrolyse.\n"
        "• L'étude de l'effet de la vitesse de chauffage sur les rendements.\n"
        "• L'analyse de l'influence du temps de maintien isotherme.\n"
        "• La réalisation d'essais de pyrolyse catalytique.\n"
        "• L'étude du craquage secondaire des vapeurs de pyrolyse.\n"
        "• La production et la caractérisation de biochars et de biohuiles.\n"
        "• La détermination des rendements en solides, liquides et gaz.\n"
        "• L'analyse de la composition des gaz non condensables par micro-GC.\n"
        "• L'établissement de bilans matière et l'évaluation "
        "des performances du procédé."
    ),

    "utilisation": (
        "1. PRÉPARATION DE L'ÉCHANTILLON :\n"
        "Préparer et homogénéiser la biomasse à étudier. "
        "Déterminer si nécessaire sa teneur en humidité, "
        "puis peser une quantité représentative adaptée "
        "à la capacité utile du réacteur.\n\n"

        "2. CHARGEMENT DU RÉACTEUR :\n"
        "Introduire l'échantillon dans le réacteur cylindrique. "
        "Vérifier le positionnement des composants internes, "
        "la propreté des conduites et l'étanchéité "
        "des raccordements avant fermeture.\n\n"

        "3. INSTALLATION ÉVENTUELLE DU LIT CATALYTIQUE :\n"
        "Pour les essais catalytiques, introduire une quantité "
        "définie de catalyseur dans la zone chauffée de sortie "
        "des vapeurs. Vérifier la fixation du lit catalytique "
        "et la libre circulation des gaz.\n\n"

        "4. PRÉPARATION DU CIRCUIT DE CONDENSATION :\n"
        "Vérifier les connexions des deux condenseurs montés "
        "en série, installer les récipients de récupération "
        "des liquides et régler le système de refroidissement. "
        "La température du second condenseur peut être "
        "abaissée jusqu'à 5 °C.\n\n"

        "5. MISE SOUS ATMOSPHÈRE INERTE :\n"
        "Effectuer une purge du réacteur et du circuit gazeux "
        "à l'aide d'un gaz inerte adapté (azote), selon la procédure "
        "du laboratoire, afin d'éliminer l'oxygène présent "
        "avant le démarrage de la pyrolyse.\n\n"

        "6. PROGRAMMATION DU PROFIL THERMIQUE :\n"
        "Définir la température finale de pyrolyse, "
        "dans la limite de 700 °C, la vitesse de montée "
        "en température (°C/min) et la durée du palier "
        "isotherme. Régler indépendamment la température "
        "de la zone chauffée de sortie des vapeurs "
        "en fonction des objectifs expérimentaux.\n\n"

        "7. LANCEMENT DE LA PYROLYSE :\n"
        "Démarrer le programme de chauffage et suivre "
        "l'évolution de la température du réacteur. "
        "Maintenir les conditions thermiques définies "
        "pendant toute la durée de l'essai et surveiller "
        "les paramètres de sécurité.\n\n"

        "8. CONDENSATION ET RÉCUPÉRATION DES LIQUIDES :\n"
        "Acheminer les vapeurs produites vers les deux "
        "condenseurs en série. Récupérer les fractions "
        "liquides condensées dans des récipients adaptés "
        "et mesurer leur masse après l'essai.\n\n"

        "9. ANALYSE ET QUANTIFICATION DES GAZ :\n"
        "Diriger les gaz non condensables vers le micro-GC "
        "pour l'analyse de leur composition, ou vers "
        "le système de collecte et de quantification "
        "des gaz selon le protocole expérimental retenu.\n\n"

        "10. REFROIDISSEMENT DU RÉACTEUR :\n"
        "À la fin du programme thermique, arrêter le chauffage "
        "et laisser refroidir le réacteur dans des conditions "
        "contrôlées, en maintenant les dispositions "
        "nécessaires pour éviter toute entrée d'air "
        "dans l'enceinte encore chaude.\n\n"

        "11. RÉCUPÉRATION DU BIOCHAR :\n"
        "Après refroidissement à une température compatible "
        "avec une ouverture sécurisée, récupérer le résidu "
        "solide de pyrolyse, le peser et le conserver "
        "dans un contenant approprié pour les analyses.\n\n"

        "12. TRAITEMENT ET EXPLOITATION DES RÉSULTATS :\n"
        "Déterminer les rendements massiques en char, "
        "liquides et gaz, établir le bilan matière "
        "et analyser l'influence des paramètres "
        "opératoires sur les produits obtenus. "
        "Comparer les résultats des essais thermiques "
        "et catalytiques lorsque cela est applicable."
    ),

    "protocole": (
        "PROTOCOLE EXPÉRIMENTAL DE RÉFÉRENCE :\n\n"

        "1. Préparation et pesée de la biomasse : 5 min.\n"
        "2. Chargement du réacteur et vérification des raccordements : 15 min.\n"
        "3. Installation éventuelle du catalyseur : 10 min.\n"
        "4. Préparation des condenseurs et du circuit gazeux : 5 min.\n"
        "5. Purge sous atmosphère inerte et contrôles : 10 min.\n"
        "6. Programmation et vérification du profil thermique : 5 min.\n"
        "7. Montée en température (10 °C/min) : 70 min.\n"
        "8. Maintien de température isotherme : 30 min.\n"
        "9. Refroidissement du réacteur : 120 min.\n"
        "10. Récupération et pesée des produits : 20 min.\n"
        "11. Nettoyage et remise en état de l'installation : 20 min.\n"
        "12. Traitement et validation des résultats : 15 min.\n\n"

        "DURÉE TOTALE ESTIMÉE : 325 minutes, soit environ 5 h 25 min (5,42 h).\n"
        "PRÉSENCE OPÉRATEUR : 3,42 heures par essai.\n"
        "INTERVENTION TECHNICIEN : 60 minutes par 30 essais (0.03 h) pour la réparation, les contrôles et la maintenance courante.\n\n"

        "La durée réelle de la phase de chauffage dépend "
        "de la température initiale, de la température finale, "
        "de la vitesse de montée en température et "
        "du temps de maintien isotherme programmé.\n\n"

        "Le temps de refroidissement dépend notamment des conditions de refroidissement.\n\n"

        "Les essais avec lit catalytique peuvent nécessiter "
        "des opérations supplémentaires de préparation, "
        "de conditionnement et de récupération du catalyseur.\n\n"

        "Les temps indiqués ne comprennent pas les éventuelles "
        "opérations complémentaires de séchage, broyage, "
        "tamisage, caractérisation des produits, "
        "régénération des catalyseurs ou maintenance approfondie.\n\n"
    ),

    # Durées de référence utilisées pour le chiffrage
    "duree_essai_h": 5.42,
    "presence_operateur_h": 3.42,

    # Photographies de l'appareil
    # Chemins relatifs au dossier principal de l'application
    # À remplacer par les noms réels des fichiers
    "photos_fichiers": [
        "images/PYRO 1.jpg",
        "images/PYRO 1 (1).jpg",
        "images/PYRO 1 (11).jpg",
        "images/PYRO 1 (3).jpg",
        "images/PYRO 1 (4).jpg",
        "images/PYRO 1 (5).jpg",
        "images/PYRO 1 (7).jpg",
        "images/PYRO 1 (8).jpg",
        "images/PYRO 1 (9).jpg",
        "images/PYRO 1 (11).jpg",
        "images/PYRO 1 (10).jpg",
    ],

    # Coûts de référence par essai
    "couts_defaut": {
        "ingenieur_h": 3.42,
        "technicien_h": 0.03,
        "consommables_eur": 0.0,
        "energie_kwh": 2.5,
    },
}
