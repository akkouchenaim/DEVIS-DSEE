
"""Fiche technique du pyrolyseur PYRUM Innovations — 600 °C."""

FICHE = {
    "nom": "Pyrolyseur PYRUM — Pyrolyse rapide et flash",

    "description": (
        "Le pyrolyseur PYRUM Innovations est une installation expérimentale "
        "de thermolyse destinée à l'étude de la décomposition thermique "
        "des matières organiques, notamment les biomasses, les déchets "
        "organiques et autres matériaux valorisables par pyrolyse, "
        "sous atmosphère contrôlée et en absence d'oxygène.\n\n"

        "Fabriqué par Pyrum Innovations ESC GmbH, cet équipement "
        "de laboratoire (modèle PY12003, fabrication 2012) "
        "fonctionne sous une alimentation électrique de 240 V AC, "
        "avec une puissance nominale indiquée de 1,1 kW.\n\n"

        "Le réacteur est constitué d'une enceinte cylindrique "
        "de 8 cm de diamètre et de 20 cm de longueur, "
        "correspondant à un volume géométrique théorique "
        "d'environ 1 litre. Il est équipé d'un dispositif "
        "de chauffage permettant d'atteindre une température "
        "maximale de 600 °C.\n\n"

        "La particularité de cette installation réside dans "
        "son système d'alimentation en matière constitué "
        "de deux vannes montées en série, permettant "
        "l'introduction d'un échantillon dans le réacteur "
        "préalablement porté à la température souhaitée.\n\n"

        "Cette configuration permet de limiter la perturbation "
        "de l'atmosphère interne pendant le chargement "
        "et d'exposer rapidement la matière à une température "
        "élevée, favorisant ainsi la réalisation d'essais "
        "de pyrolyse rapide, voire de pyrolyse flash lorsque "
        "les conditions de transfert thermique le permettent.\n\n"

        "Contrairement à un réacteur discontinu conventionnel, "
        "dans lequel l'échantillon est généralement chauffé "
        "progressivement avec le réacteur, le système PYRUM "
        "permet d'effectuer l'introduction de la matière "
        "après stabilisation de la température du réacteur. "
        "Cette méthode facilite l'étude des phénomènes "
        "de décomposition thermique rapide et de formation "
        "des produits volatils.\n\n"

        "Les vapeurs produites lors de la pyrolyse sont "
        "évacuées du réacteur vers un système de condensation "
        "destiné à refroidir les effluents gazeux "
        "et à récupérer les composés condensables.\n\n"

        "Les produits liquides, constitués notamment "
        "de biohuiles, de fractions organiques condensables "
        "et d'une éventuelle phase aqueuse, sont collectés "
        "dans un dispositif de récupération adapté "
        "pour leur quantification et leur caractérisation.\n\n"

        "Les gaz non condensables sont dirigés vers "
        "un microchromatographe en phase gazeuse (micro-GC) "
        "pour l'analyse de leur composition ou vers "
        "un dispositif de stockage permettant "
        "leur caractérisation et leur quantification ultérieures.\n\n"

        "Le résidu solide restant dans le réacteur "
        "est récupéré après refroidissement "
        "afin de déterminer le rendement en char "
        "et de réaliser les analyses physico-chimiques "
        "complémentaires.\n\n"

        "Cet équipement permet notamment :\n"
        "• L'étude de la pyrolyse de différentes biomasses "
        "et matières organiques.\n"
        "• La réalisation d'essais de pyrolyse à des températures "
        "pouvant atteindre 600 °C.\n"
        "• L'étude de la pyrolyse rapide par introduction "
        "de l'échantillon dans un réacteur préchauffé.\n"
        "• L'exploration des conditions de pyrolyse flash.\n"
        "• L'évaluation de l'influence de la température "
        "sur la distribution des produits.\n"
        "• L'étude des phénomènes de dévolatilisation "
        "et de décomposition thermique rapide.\n"
        "• La production et la caractérisation des chars "
        "et des liquides de pyrolyse.\n"
        "• La récupération et l'analyse des gaz "
        "non condensables par micro-GC.\n"
        "• La détermination des rendements en solides, "
        "liquides et gaz.\n"
        "• L'établissement de bilans matière "
        "et l'évaluation des performances "
        "du procédé de thermolyse."
    ),

    "utilisation": (
        "1. PRÉPARATION DE L'ÉCHANTILLON :\n"
        "Préparer et homogénéiser la matière à traiter. "
        "Réaliser si nécessaire un séchage, un broyage "
        "et un tamisage afin d'obtenir une granulométrie "
        "adaptée à l'introduction dans le réacteur. "
        "Peser précisément la masse de l'échantillon.\n\n"

        "2. VÉRIFICATION DE L'INSTALLATION :\n"
        "Contrôler l'état général du réacteur, "
        "des deux vannes d'introduction, "
        "des raccordements, du système de chauffage "
        "et des dispositifs de sécurité. "
        "Vérifier l'absence d'obstruction "
        "dans le circuit d'évacuation des vapeurs.\n\n"

        "3. PRÉPARATION DU SYSTÈME DE CONDENSATION :\n"
        "Installer le récipient destiné à la récupération des liquides. "
        "Vérifier le fonctionnement du circuit "
        "de refroidissement ainsi que les raccordements "
        "vers l'analyseur micro-GC ou le système "
        "de collecte des gaz.\n\n"

        "4. MISE SOUS ATMOSPHÈRE INERTE :\n"
        "Effectuer une purge du réacteur et "
        "des conduites à l'aide d'un gaz inerte "
        "approprié afin de limiter la présence "
        "d'oxygène avant le démarrage de l'essai. "
        "Vérifier les conditions de sécurité "
        "et l'étanchéité du système.\n\n"

        "5. PRÉCHAUFFAGE DU RÉACTEUR :\n"
        "Programmer la température de pyrolyse "
        "souhaitée, dans la limite de 600 °C. "
        "Démarrer le chauffage et attendre "
        "la stabilisation thermique du réacteur "
        "avant l'introduction de la matière.\n\n"

        "6. PRÉPARATION DE L'INTRODUCTION À CHAUD :\n"
        "Placer l'échantillon dans le compartiment "
        "d'alimentation situé entre les deux vannes, "
        "selon la configuration du dispositif. "
        "Isoler ce compartiment du réacteur "
        "et préparer la séquence d'introduction "
        "conformément à la procédure de sécurité "
        "et de purge de l'installation.\n\n"

        "7. INTRODUCTION RAPIDE DE L'ÉCHANTILLON :\n"
        "Après stabilisation de la température "
        "et inertage du compartiment d'alimentation, "
        "actionner le système de double vanne "
        "selon la procédure validée afin "
        "d'introduire rapidement la matière "
        "dans le réacteur chaud, sans communication "
        "directe entre l'air ambiant et le réacteur.\n\n"

        "8. RÉALISATION DE LA PYROLYSE :\n"
        "Maintenir les conditions opératoires "
        "définies et suivre l'évolution "
        "de la température et du dégagement "
        "des vapeurs. La décomposition thermique "
        "de l'échantillon produit un résidu solide, "
        "des composés condensables "
        "et des gaz non condensables.\n\n"

        "9. CONDENSATION DES VAPEURS :\n"
        "Acheminer les vapeurs de pyrolyse "
        "vers le condenseur afin de provoquer "
        "la liquéfaction des fractions condensables. "
        "Récupérer les produits liquides "
        "dans les récipients prévus "
        "et mesurer leur masse.\n\n"

        "10. ANALYSE ET COLLECTE DES GAZ :\n"
        "Diriger les gaz non condensables "
        "vers le micro-GC pour leur caractérisation "
        "ou vers le dispositif de collecte "
        "et de stockage adapté. "
        "Déterminer leur composition "
        "et leur quantité à partir "
        "des mesures disponibles.\n\n"

        "11. FIN D'ESSAI ET REFROIDISSEMENT :\n"
        "Arrêter le chauffage et laisser "
        "refroidir le réacteur sous atmosphère "
        "contrôlée, conformément aux procédures "
        "de sécurité du laboratoire.\n\n"

        "12. RÉCUPÉRATION DU RÉSIDU SOLIDE :\n"
        "Après refroidissement suffisant, "
        "ouvrir le réacteur et récupérer "
        "le résidu solide. "
        "Peser le char obtenu et le conserver "
        "dans un contenant adapté.\n\n"

        "13. NETTOYAGE DE L'INSTALLATION :\n"
        "Nettoyer le réacteur, le système "
        "d'introduction, les conduites "
        "et les dispositifs de récupération "
        "des produits. Vérifier l'état "
        "des joints et des raccordements.\n\n"

        "14. TRAITEMENT DES RÉSULTATS :\n"
        "Déterminer les rendements en char, "
        "liquides et gaz, établir le bilan matière "
        "et analyser l'influence des paramètres "
        "opératoires sur la distribution "
        "et la composition des produits obtenus."
    ),

    "protocole": (
        "PROTOCOLE EXPÉRIMENTAL DE RÉFÉRENCE :\n\n"

        "1. Préparation et pesée de l'échantillon : 5 min.\n"
        "2. Vérification du réacteur et du système à double vanne : 5 min.\n"
        "3. Préparation du système de condensation et de collecte des gaz : 5 min.\n"
        "4. Inertage et contrôles de sécurité : 10 min.\n"
        "5. Préchauffage et stabilisation du réacteur : 60 min.\n"
        "6. Préparation et introduction de l'échantillon à chaud : 5 min.\n"
        "7. Pyrolyse et récupération des effluents : 30 min.\n"
        "8. Refroidissement contrôlé du réacteur : 60 min.\n"
        "9. Récupération et pesée des produits : 15 min.\n"
        "10. Nettoyage et remise en état de l'installation : 15 min.\n"
        "11. Traitement et validation des résultats : 15 min.\n\n"

        "DURÉE TOTALE ESTIMÉE : 225 minutes, soit environ 3,75 heures.\n"
        "PRÉSENCE OPÉRATEUR : 2,75 heure par essai.\n"
        "INTERVENTION TECHNICIEN : 60 minutes par 30 essai pour les contrôles et la maintenance courante.\n\n"

        "ESTIMATION DE LA CONSOMMATION ÉLECTRIQUE :\n"
        "La puissance nominale de l'appareil est de 1,1 kW selon la plaque constructeur. "
        "Pour une hypothèse de 1,5 heures de chauffage à puissance nominale, "
        "la consommation électrique de référence est estimée à 1,36 kWh par essai.\n"
        "Cette valeur est indicative et ne constitue pas une mesure de consommation réelle. "
        "Les équipements auxiliaires, notamment le refroidissement et l'analyse des gaz, "
        "doivent être comptabilisés séparément "
        "si leur consommation est incluse dans le chiffrage.\n\n"

        "Les temps de préchauffage, de pyrolyse "
        "et de refroidissement peuvent varier "
        "selon la température choisie, "
        "la masse de l'échantillon, "
        "ses propriétés thermiques "
        "et les conditions expérimentales.\n\n"

        "L'introduction à chaud permet d'étudier "
        "la pyrolyse rapide, mais la qualification "
        "de pyrolyse flash nécessite de vérifier "
        "la vitesse réelle de chauffage "
        "des particules et leur temps "
        "de séjour dans la zone chaude.\n\n"

        "Les durées indiquées ne comprennent pas "
        "les opérations complémentaires éventuelles "
        "de séchage, broyage, caractérisation "
        "physico-chimique approfondie, "
        "étalonnage du micro-GC ou maintenance lourde.\n\n"
    ),

    # Durées de référence utilisées pour le chiffrage
    "duree_essai_h": 3.75,
    "presence_operateur_h": 1.50,

    # Photographies de l'appareil
    # Chemins relatifs au dossier principal de l'application
    "photos_fichiers": [
        "images/PYRUM.jpg",
        "images/PYRUM (1).jpg",
        "images/PYRUM (2).jpg",
        "images/PYRUM (3).jpg",
        "images/PYRUM (5).jpg",
        "images/PYRUM (6).jpg",
        "images/PYRUM (4).jpg",
    ],

    # Coûts de référence par essai
    # Valeurs indicatives à adapter aux tarifs du laboratoire
    "couts_defaut": {
        "ingenieur_h": 1.50,
        "technicien_h": 0.033,
        "consommables_eur": 5.0,
        "energie_kwh": 1.36,
    },
}
