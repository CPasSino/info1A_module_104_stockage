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


@obj_mon_application.route("/device_afficher/<string:order_by>/<int:id_device>", methods=['GET', 'POST'])
def device_afficher(order_by, id_device):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)
            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                if id_device == 0:
                    strsql_genres_afficher = f"""SELECT id_device, serial_number_device, name_model, name_status
                                                    FROM t_device 
                                                        LEFT JOIN t_model ON id_model = fk_model
                                                        LEFT JOIN t_status ON id_status = fk_status 
                                                ORDER BY id_device {order_by}"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = f"""SELECT id_device, serial_number_device, name_model, name_status
                                                    FROM t_device  
                                                        LEFT JOIN t_model ON id_model = fk_model
                                                        LEFT JOIN t_status ON id_status = fk_status                                                        
                                                WHERE id_device = {id_device}
                                                ORDER BY id_device {order_by}"""
                    mc_afficher.execute(strsql_genres_afficher)

                print(type(mc_afficher))
                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                if not data_genres and id_device == 0:
                    flash("""La table est vide. !!""", "warning")

                elif not data_genres and id_device > 0:
                    flash(f"L'enregistrement demandé n'existe pas !!", "warning")

                else:
                    flash(f"Données affichées !!", "success")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/devices_afficher.html", data=data_genres)


@obj_mon_application.route("/genre_ajouter", methods=['GET', 'POST'])
def genre_ajouter():
    form = FormDevices()
    if request.method == "POST":
        if form.validate_on_submit() and request.form.getlist('modeles')[0] and request.form.getlist('status')[0] != 'placeholder':
            try:
                try:
                    MaBaseDeDonnee().connexion_bd.ping(False)

                except Exception as erreur:
                    flash("Il faut connecter une base de données", "danger")
                    raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

                if form.validate_on_submit():
                    strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model + 1 WHERE id_model = {request.form.getlist('modeles')[0]}"""
                    with MaBaseDeDonnee() as mconn_bd:
                        mconn_bd.mabd_execute(strsql_insert_genre)

                    strsql_insert_genre = f"""INSERT INTO t_device (id_device,serial_number_device, fk_model, fk_status) VALUES (NULL,"{form.sn.data.lower()}", "{request.form.getlist('modeles')[0]}", "{request.form.getlist('status')[0]}")"""
                    with MaBaseDeDonnee() as mconn_bd:
                        mconn_bd.mabd_execute(strsql_insert_genre)

                    flash(f"Données insérées !!", "success")
                    print(f"Données insérées !!")

                    return redirect(url_for('device_afficher', order_by='DESC', id_device=0))

            except pymysql.err.IntegrityError as erreur_genre_doublon:
                code, msg = erreur_genre_doublon.args
                flash(f"{error_codes.get(code, msg)} ", "warning")

            except (pymysql.err.OperationalError,
                    pymysql.ProgrammingError,
                    pymysql.InternalError,
                    TypeError) as erreur_gest_genr_crud:
                code, msg = erreur_gest_genr_crud.args

                flash(f"{error_codes.get(code, msg)} ", "danger")
                flash(f"Erreur dans Gestion genres CRUD : {sys.exc_info()[0]} "
                      f"{erreur_gest_genr_crud.args[0]} , "
                      f"{erreur_gest_genr_crud}", "danger")

                try:
                    MaBaseDeDonnee().connexion_bd.ping(False)

                except Exception as erreur:
                    flash("Il faut connecter une base de données", "danger")
                    raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

    strsql_insert_genre = f"""SELECT id_model, name_model FROM t_model """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        modeles = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT id_status, name_status FROM t_status """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        status = mc_afficher.fetchall()

    return render_template("genres/genres_ajouter_wtf.html", form=form, modeles=modeles, status=status)


@obj_mon_application.route('/genre_delete/<int:id>', methods=['GET', 'POST'])
def genre_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model - 1 WHERE id_model = (SELECT fk_model FROM t_device WHERE id_device = {id})"""
            with MaBaseDeDonnee() as mconn_bd:
                mconn_bd.mabd_execute(strsql_insert_genre)

            with MaBaseDeDonnee().connexion_bd.cursor() as mconn_bd:
                sql = f"""
                        select id_device, name_model, serial_number_device 
                            from t_device
                                INNER join t_model ON id_device

                            Where id_device = {id}"""

                mconn_bd.execute(sql)
                data = mconn_bd.fetchall()

            return render_template('genres/device_delete.html', data=data, id=id)

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    elif request.method == "POST":
        try:
            with MaBaseDeDonnee() as mconn_bd:
                trsql_genres_afficher = f"""DELETE FROM t_device WHERE id_device = {id}"""
                mconn_bd.mabd_execute(trsql_genres_afficher)

            flash(f"Données supprimées !!", "success")
            print(f"Données supprimées !!")

            return redirect(url_for('device_afficher', order_by='ASC', id_device=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")


@obj_mon_application.route('/genre_edit/<int:id>', methods=['GET', 'POST'])
def genre_edit(id):
    form = FormDevices()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model + 1 WHERE id_model = (SELECT fk_model FROM t_device WHERE id_device = {id})"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                strsql_insert_genre = f"""UPDATE t_model SET quantite_model = quantite_model - 1 WHERE id_model = {request.form.getlist('modeles')[0]}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)
                strsql_insert_genre = f"""UPDATE t_device SET serial_number_device = "{form.sn.data.lower()}", fk_model = {request.form.getlist('modeles')[0]}, fk_status = {request.form.getlist('status')[0]} WHERE id_device = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('device_afficher', order_by='ASC', id_device=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    elif request.method == "GET":
        strsql_insert_genre = f"""SELECT * FROM t_device WHERE id_device = {id}"""
        with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
            mc_afficher.execute(strsql_insert_genre)
            data = mc_afficher.fetchone()

        form.sn.data = data.get("serial_number_device")

    strsql_insert_genre = f"""SELECT id_model, name_model FROM t_model """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        modeles = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT fk_model FROM t_device WHERE id_device = {id} """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        used_modeles = mc_afficher.fetchone()

    strsql_insert_genre = f"""SELECT id_status, name_status FROM t_status """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        status = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT fk_status FROM t_device WHERE id_device = {id} """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        used_status = mc_afficher.fetchone()

    return render_template("genres/device_edit.html", form=form, modeles=modeles, status=status,
                           used_modeles=used_modeles, used_status=used_status, id=id)
