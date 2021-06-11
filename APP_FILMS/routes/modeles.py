from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from APP_FILMS import obj_mon_application
from APP_FILMS.database.connect_db_context_manager import MaBaseDeDonnee
from APP_FILMS.erreurs.exceptions import *
from APP_FILMS.erreurs.msg_erreurs import *
from APP_FILMS.genres.class_forms import *


@obj_mon_application.route("/modele_afficher/<string:order_by>/<int:id_modele>", methods=['GET', 'POST'])
def modele_afficher(order_by, id_modele):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                if id_modele == 0:
                    strsql_genres_afficher = f"""SELECT id_model, name_model , name_sector, bought_date_model, guarantee_date_model, description_model, quantite_model 
                                                    FROM t_model 
                                                        LEFT JOIN t_sector ON id_sector = fk_sector
                                                ORDER BY id_model {order_by}"""
                    mc_afficher.execute(strsql_genres_afficher)

                elif order_by == "ASC":
                    strsql_genres_afficher = f"""SELECT id_model, name_model, name_sector, bought_date_model, guarantee_date_model, description_model, quantite_model   
                                                    FROM t_model  
                                                        LEFT JOIN t_sector ON id_sector = fk_sector
                                                WHERE id_model = {id_modele}
                                                ORDER BY id_model {order_by}"""
                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                if not data_genres and id_modele == 0:
                    flash("""La table est vide. !!""", "warning")

                elif not data_genres and id_modele > 0:
                    flash(f"L'enregistrement demandé n'existe pas !!", "warning")

                else:
                    flash(f"Données affichées !!", "success")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/modeles_afficher.html", data=data_genres)


@obj_mon_application.route("/modele_ajouter", methods=['GET', 'POST'])
def modele_ajouter():
    form = FormModels()
    if request.method == "POST":
        if form.validate_on_submit() and request.form.getlist('secteur')[0] != 'placeholder':
            try:
                try:
                    MaBaseDeDonnee().connexion_bd.ping(False)

                except Exception as erreur:
                    flash("Il faut connecter une base de données", "danger")
                    raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

                strsql_insert_genre = f"""INSERT INTO t_model (id_model, name_model, fk_sector, bought_date_model, guarantee_date_model, description_model, quantite_model) VALUES (NULL,"{form.name.data.lower()}", "{int(request.form.getlist('secteur')[0])}", "{form.bought_date_model.data}", "{form.guarantee_date_model.data}", "{form.description_model.data.lower()}", 0)"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('modele_afficher', order_by='DESC', id_modele=0))

            except pymysql.err.IntegrityError as erreur_genre_doublon:
                code, msg = erreur_genre_doublon.args
                flash(f"{error_codes.get(code, msg)} ", "warning")

            except (pymysql.err.OperationalError,
                    pymysql.ProgrammingError,
                    pymysql.InternalError,
                    TypeError) as erreur_gest_genr_crud:
                code, msg = erreur_gest_genr_crud.args
                code, msg = erreur_gest_genr_crud.args
                flash(f"{error_codes.get(code, msg)} ", "danger")
                flash(f"Erreur dans Gestion genres CRUD : {sys.exc_info()[0]} "
                      f"{erreur_gest_genr_crud.args[0]} , "
                      f"{erreur_gest_genr_crud}", "danger")

    strsql_insert_genre = f"""SELECT id_sector, name_sector FROM t_sector """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        secteurs = mc_afficher.fetchall()

    return render_template("genres/modele_ajouter.html", form=form, secteurs=secteurs)


@obj_mon_application.route('/model_delete/<int:id>', methods=['GET', 'POST'])
def model_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mconn_bd:
                sql = f"""
                        select id_model, name_model, serial_number_device 
                            from t_model
                                INNER join t_device ON fk_model = id_model

                            Where id_model = {id}"""

                mconn_bd.execute(sql)
                data = mconn_bd.fetchall()

            return render_template('genres/modele_delete.html', data=data, id=id)

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    elif request.method == "POST":
        try:
            with MaBaseDeDonnee() as mconn_bd:
                trsql_genres_afficher = f"""DELETE FROM t_model WHERE id_model = {id}"""
                mconn_bd.mabd_execute(trsql_genres_afficher)

            flash(f"Données supprimées !!", "success")
            print(f"Données supprimées !!")

            return redirect(url_for('modele_afficher', order_by='ASC', id_modele=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")


@obj_mon_application.route('/model_edit/<int:id>', methods=['GET', 'POST'])
def model_edit(id):
    form = FormModels()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""UPDATE t_model SET name_model = "{form.name.data.lower()}", fk_sector = {int(request.form.getlist('secteur')[0])}, bought_date_model = "{form.bought_date_model.data}", guarantee_date_model = "{form.guarantee_date_model.data}", description_model = "{form.description_model.data.lower()}" WHERE id_model = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('modele_afficher', order_by='ASC', id_modele=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    elif request.method == "GET":
        strsql_insert_genre = f"""SELECT * FROM t_model WHERE id_model = {id}"""
        with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
            mc_afficher.execute(strsql_insert_genre)
            data = mc_afficher.fetchone()

        form.description_model.data = data.get("description_model")
        form.name.data = data.get("name_model")
        form.bought_date_model.data = data.get("bought_date_model")
        form.guarantee_date_model.data = data.get("guarantee_date_model")

    strsql_insert_genre = f"""SELECT id_sector, name_sector FROM t_sector """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        secteurs = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT fk_sector FROM t_model WHERE id_model = {id} """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        used_secteurs = mc_afficher.fetchone()

    print(used_secteurs, secteurs)

    return render_template("genres/modele_edit.html", form=form, secteurs=secteurs, used_secteurs=used_secteurs, id=id)
