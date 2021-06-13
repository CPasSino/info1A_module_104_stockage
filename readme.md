Mon Projet
---


# Faire fonctionner mon projet :
####Faire très attention :
* Démarrer le serveur MySql (uwamp ou xamp ou mamp, etc)
* Dans PyCharm, importer la BD grâce à un "run" du fichier "zzzdemos/1_ImportationDumpSql.py".
  * En cas d'erreur ouvrir le fichier ".env" à la racine du projet, contrôler les indications de connexion pour la bd.
* ouvrir le fichier "1_run_server_flask.py" et faire un "run" ensuite.

## CONSEILS
* Pour ne pas avoir de problème je vous conseil d'abord de faire les enregistrement dans l'ordre suivant :
  * Status
  * Secteur
  * Modèles
  * Customers
  * Devices
  * Puis empreint
* Comme ça vous aurez la belle barre animé sur la page Home (et surtout ne pas oublier la fameuse page 404 que j'ai faites)  
* Pour que la barre animé change il faut que dans le device vous séléctionner des modèles et c'est a ce moment la ou il y'aura plus de quantité dans les modèle et ensuite dans les empreints vous pourrez empreinter un modèle. si vous ne voyez pas de modèle c'est parce qu'il y'en a plus de quantité.


