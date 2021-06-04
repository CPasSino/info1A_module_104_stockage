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


@obj_mon_application.route("/use_afficher/<string:order_by>/<int:id_use>", methods=['GET', 'POST'])
def use_afficher(order_by, id_use):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                if id_use == 0:
                    strsql_genres_afficher = f"""SELECT id_start_use, serial_number_device, first_name_customer, last_name_customer, date_start_use, date_end_use, reason_end_use, name_model
                                                    FROM t_use 
                                                        LEFT JOIN t_customer ON id_customer = fk_customer 
                                                        LEFT JOIN t_device ON id_device = fk_device
                                                        LEFT JOIN t_model on id_model = fk_model
                                                ORDER BY id_start_use {order_by}"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = f"""SELECT id_start_use, serial_number_device, first_name_customer, last_name_customer, date_start_use, date_end_use, reason_end_use, name_model
                                                    FROM t_use 
                                                        LEFT JOIN t_customer ON id_customer = fk_customer 
                                                        LEFT JOIN t_device ON id_device = fk_device
                                                        LEFT JOIN t_model on id_model = fk_model
                                                WHERE id_start_use = {id_use}
                                                ORDER BY id_start_use {order_by}"""
                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                if not data_genres and id_use == 0:
                    flash("""La table est vide. !!""", "warning")

                elif not data_genres and id_use > 0:
                    flash(f"L'enregistrement demandé n'existe pas !!", "warning")

                else:
                    flash(f"Données affichées !!", "success")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/use_afficher.html", data=data_genres)


@obj_mon_application.route("/use_ajouter", methods=['GET', 'POST'])
def use_ajouter():
    form = FormUse()
    if request.method == "POST":
        if form.validate_on_submit() and request.form.getlist('device')[0] and request.form.getlist('customer')[0] != 'placeholder':
            try:
                try:
                    MaBaseDeDonnee().connexion_bd.ping(False)

                except Exception as erreur:
                    flash("Il faut connecter une base de données", "danger")
                    raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

                if form.validate_on_submit():
                    strsql_insert_genre = f"""INSERT INTO t_use (id_start_use, fk_device, fk_customer, date_start_use, date_end_use, reason_end_use) 
                                            VALUES (NULL,(SELECT id_device FROM t_device WHERE fk_model = {int(request.form.getlist('device')[0])} LIMIT 1), "{int(request.form.getlist('customer')[0])}", "{form.date_start_use.data}", "{form.date_end_use.data}", "{form.reason_end_use.data}")"""
                    with MaBaseDeDonnee() as mconn_bd:
                        mconn_bd.mabd_execute(strsql_insert_genre)

                    strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model - 1 WHERE id_model = {request.form.getlist('device')[0]}"""
                    with MaBaseDeDonnee() as mconn_bd:
                        mconn_bd.mabd_execute(strsql_insert_genre)

                    flash(f"Données insérées !!", "success")
                    print(f"Données insérées !!")

                    return redirect(url_for('use_afficher', order_by='DESC', id_use=0))

            except pymysql.err.IntegrityError as erreur_genre_doublon:
                code, msg = erreur_genre_doublon.args
                flash(f"{error_codes.get(code, msg)} ", "warning")

            except (pymysql.err.OperationalError,
                    pymysql.ProgrammingError,
                    pymysql.InternalError,
                    TypeError) as erreur_gest_genr_crud:
                msg = erreur_gest_genr_crud.args
                flash(f"{error_codes.get(msg)} ", "danger")
                flash(f"Erreur dans Gestion genres CRUD "
                      f"{erreur_gest_genr_crud.args[0]} , "
                      f"{erreur_gest_genr_crud}", "danger")

    strsql_insert_genre = f"""SELECT id_model, name_model FROM t_model WHERE quantite_model > 0 """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        device = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT id_customer, first_name_customer, last_name_customer FROM t_customer """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        customer = mc_afficher.fetchall()

    return render_template("genres/use_ajouter.html", form=form, device=device, customer=customer)


@obj_mon_application.route('/use_delete/<int:id>', methods=['GET', 'POST'])
def use_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model + 1 WHERE id_model = (SELECT fk_model FROM t_device WHERE id_device = (SELECT fk_device FROM t_use WHERE id_start_use = {id}))"""

            print(strsql_insert_genre)
            with MaBaseDeDonnee() as mconn_bd:
                mconn_bd.mabd_execute(strsql_insert_genre)

            with MaBaseDeDonnee() as mconn_bd:
                trsql_genres_afficher = f"""DELETE FROM t_use WHERE id_start_use = {id}"""
                mconn_bd.mabd_execute(trsql_genres_afficher)

            flash(f"Données supprimées !!", "success")
            print(f"Données supprimées !!")

            return redirect(url_for('use_afficher', order_by='ASC', id_use=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")


@obj_mon_application.route('/use_edit/<int:id>', methods=['GET', 'POST'])
def use_edit(id):
    form = FormUse()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model + 1 WHERE id_model = (SELECT fk_model FROM t_device WHERE id_device = (SELECT fk_device FROM t_use WHERE id_start_use = {id}))"""

                print(strsql_insert_genre)
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                strsql_insert_genre = f"""UPDATE t_use SET fk_device = "{request.form.getlist('device')[0]}", fk_customer = "{request.form.getlist('customer')[0]}", date_start_use = "{(form.date_start_use.data)}", date_end_use = "{(form.date_end_use.data)}", reason_end_use = "{(form.reason_end_use.data.lower())}" WHERE id_start_use = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model - 1 WHERE id_model = (SELECT fk_model FROM t_device WHERE id_device = {request.form.getlist('device')[0]})"""

                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('use_afficher', order_by='ASC', id_use=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    elif request.method == "GET":
        strsql_insert_genre = f"""SELECT * FROM t_use WHERE id_start_use = {id}"""
        with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
            mc_afficher.execute(strsql_insert_genre)
            data = mc_afficher.fetchone()

        form.date_start_use.data = data.get("date_start_use")
        form.date_end_use.data = data.get("date_end_use")
        form.reason_end_use.data = data.get("reason_end_use")

    strsql_insert_genre = f"""SELECT id_model, name_model FROM t_model WHERE quantite_model > 0 """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        device = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT id_model, name_model FROM t_model INNER JOIN t_use ON id_start_use = {id} INNER JOIN t_device ON id_device = fk_device WHERE id_model = fk_model """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        used_device = mc_afficher.fetchone()

    strsql_insert_genre = f"""SELECT id_customer, first_name_customer, last_name_customer FROM t_customer """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        customer = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT fk_customer FROM t_use WHERE id_start_use = {id} """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        used_customer = mc_afficher.fetchone()

    return render_template("genres/use_edit.html", form=form, device=device, used_device=used_device,
                           strsql_insert_genre=strsql_insert_genre, used_customer=used_customer, customer=customer,
                           id=id)
