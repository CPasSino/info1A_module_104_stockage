"""
    Fichier : msg_erreurs.py
    Auteur : OM 2021.03.16
    Erreurs particulières (personnalisées), qui n'existent que dans mon projet à moi.
    Quand il y a une erreur on doit définir des messages "clairs" sur un affichage à destination des "personnes".
    On ne doit pas les laisser devant des erreurs incompréhensibles.

"""
from pymysql.constants import ER

msg_erreurs = {
    "ErreurConnexionBD": {
        "message": "Pas de connexion à la BD ! Il faut démarrer un serveur MySql",
        "status": 400
    },
    "ErreurDoublonValue": {
        "message": "Cette valeur existe déjà.",
        "status": 400
    },
    "ErreurDictionnaire": {
        "message": "Une valeur du dictionnaire n'existe pas !!!",
        "status": 400
    },
    "ErreurStructureTable": {
        "message": "Il y a un problème dans la structure des genres",
        "status": 400
    },
    "ErreurNomBD": {
        "message": "Problème avec le nom de la base de donnée",
        "status": 400
    },
    "ErreurPyMySql": {
        "message": "Problème en relation avec la BD",
        "status": 400
    },
    "ErreurDeleteContrainte": {
        "message": "Impossible d'effacer, car cette valeur est référencée ailleurs",
        "status": 400
    },
    "ErreurDeSyntaxeMySql": {
        "message": "Une erreur de syntaxe en MySql s'est glissée dans les requêtes",
        "status": 400
    },
}

error_codes = {
    ER.DUP_ENTRY: "Cette valeur existe déjà !!",
    ER.PARSE_ERROR: "Ooouh là une très vilaine erreur de syntaxe en MySql"
}
