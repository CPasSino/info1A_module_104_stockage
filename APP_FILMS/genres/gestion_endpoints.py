from flask import flash
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

from APP_FILMS import obj_mon_application
from APP_FILMS.database.connect_db_context_manager import MaBaseDeDonnee
from APP_FILMS.erreurs.msg_erreurs import *
from APP_FILMS.erreurs.exceptions import *
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
                    strsql_genres_afficher = """SELECT id_device, serial_number_device, fk_model, fk_status FROM t_device ORDER BY id_device ASC"""
                    mc_afficher.execute(strsql_genres_afficher)

                elif order_by == "ASC":
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_device}
                    strsql_genres_afficher = """SELECT id_device, serial_number_device, fk_model, fk_status FROM t_device  WHERE id_device = %(value_id_genre_selected)s"""
                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)

                else:
                    strsql_genres_afficher = """SELECT id_device, serial_number_device, fk_model, fk_status FROM t_device ORDER BY id_device DESC"""
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


@obj_mon_application.route("/sector_afficher/<string:order_by>/<int:id_sector>", methods=['GET', 'POST'])
def sector_afficher(order_by, id_sector):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                if id_sector == 0:
                    strsql_genres_afficher = """SELECT id_sector, name_sector FROM t_sector ORDER BY id_sector ASC"""
                    mc_afficher.execute(strsql_genres_afficher)

                elif order_by == "ASC":
                    strsql_genres_afficher = f"""SELECT id_sector, name_sector FROM t_sector  WHERE id_sector = {id_sector}"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = """SELECT id_sector, name_sector FROM t_sector ORDER BY id_sector DESC"""
                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                if not data_genres and id_sector == 0:
                    flash("""La table est vide. !!""", "warning")

                elif not data_genres and id_sector > 0:
                    flash(f"L'enregistrement demandé n'existe pas !!", "warning")

                else:
                    flash(f"Données affichées !!", "success")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/sector_afficher.html", data=data_genres)


@obj_mon_application.route("/statut_afficher/<string:order_by>/<int:id_status>", methods=['GET', 'POST'])
def status_afficher(order_by, id_status):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                if id_status == 0:
                    strsql_genres_afficher = """SELECT id_status, name_status FROM t_status ORDER BY id_status ASC"""
                    mc_afficher.execute(strsql_genres_afficher)

                elif order_by == "ASC":
                    strsql_genres_afficher = f"""SELECT id_status, name_status FROM t_status  WHERE id_status = {id_status}"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = """SELECT id_status, name_status FROM t_status ORDER BY id_status DESC"""
                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                if not data_genres and id_status == 0:
                    flash("""La table est vide. !!""", "warning")

                elif not data_genres and id_status > 0:
                    flash(f"L'enregistrement demandé n'existe pas !!", "warning")

                else:
                    flash(f"Données affichées !!", "success")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/statut_afficher.html", data=data_genres)


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
                    strsql_genres_afficher = """SELECT id_model, name_model , fk_sector, bought_date_model, guarantee_date_model, description_model FROM t_model ORDER BY id_model ASC"""
                    mc_afficher.execute(strsql_genres_afficher)

                elif order_by == "ASC":
                    strsql_genres_afficher = f"""SELECT id_model, name_model, fk_sector, bought_date_model, guarantee_date_model, description_model  FROM t_model  WHERE id_model = {id_modele}"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = """SELECT id_model, name_model, fk_sector, bought_date_model, guarantee_date_model, description_model  FROM t_model ORDER BY id_model DESC"""
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
                    strsql_genres_afficher = """SELECT id_start_use, fk_device, fk_customer, date_start_use, date_end_use, reason_end_use FROM t_use ORDER BY id_start_use ASC"""
                    mc_afficher.execute(strsql_genres_afficher)

                elif order_by == "ASC":
                    strsql_genres_afficher = f"""SELECT id_start_use, fk_device, fk_customer, date_start_use, date_end_use, reason_end_use  FROM t_use  WHERE id_start_use = {id_use}"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = """SELECT id_start_use, fk_device, fk_customer, date_start_use, date_end_use, reason_end_use  FROM t_use ORDER BY id_start_use DESC"""
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


@obj_mon_application.route("/customers_afficher/<string:order_by>/<int:id_customer>", methods=['GET', 'POST'])
def customers_afficher(order_by, id_customer):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                if order_by == "ASC" and id_customer == 0:
                    strsql_genres_afficher = """SELECT id_customer, first_name_customer, last_name_customer, fk_sector, phone_customer, personal_number_customer, location_customer FROM t_customer ORDER BY id_customer ASC"""
                    mc_afficher.execute(strsql_genres_afficher)

                elif order_by == "ASC":
                    strsql_genres_afficher = f"""SELECT id_customer, first_name_customer, last_name_customer, fk_sector, phone_customer, personal_number_customer, location_customer FROM t_customer  WHERE id_customer = {id_customer}"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = """SELECT id_customer, first_name_customer, last_name_customer, fk_sector, phone_customer, personal_number_customer, location_customer FROM t_customer ORDER BY id_customer DESC"""
                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                if not data_genres and id_customer == 0:
                    flash("""La table est vide. !!""", "warning")

                elif not data_genres and id_customer > 0:
                    flash(f"L'enregistrement demandé n'existe pas !!", "warning")

                else:
                    flash(f"Données affichées !!", "success")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/customers_afficher.html", data=data_genres)


@obj_mon_application.route("/genre_ajouter", methods=['GET', 'POST'])
def genre_ajouter():
    form = FormDevices()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""INSERT INTO t_device (id_device,serial_number_device, fk_model, fk_status) VALUES (NULL,"{form.sn.data.lower()}", {int(form.fk_model.data)}, {int(form.fk_status.data)})"""
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

    strsql_getfk = f"""SELECT id_model, name_model FROM t_model"""
    with MaBaseDeDonnee().connexion_bd.cursor() as mconn_bd:
        mconn_bd.execute(strsql_getfk)

    choices = []

    for dict in reversed(mconn_bd.fetchall()):
        choices.append((dict['id_model'], dict['name_model']))

    models = SelectField(u'Selectionner un modèle', choices=choices)
    print(type(SelectField()))

    return render_template("genres/genres_ajouter_wtf.html", form=form, models=models)


@obj_mon_application.route("/customer_ajouter", methods=['GET', 'POST'])
def customer_ajouter():
    form = FormCustomers()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""INSERT INTO t_customer (id_customer, first_name_customer, last_name_customer, fk_sector, phone_customer, personal_number_customer, location_customer) 
                                         VALUES (NULL,"{form.first_name.data.lower()}", "{form.last_name.data.lower()}", "{int(form.sector.data)}", "{int(form.location.data)}", "{int(form.phone_customer.data)}", "{int(form.personal_number_customer.data)}")"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('customers_afficher', order_by='DESC', id_customer=0))

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

    return render_template("genres/customers_ajouter.html", form=form)


@obj_mon_application.route("/modele_ajouter", methods=['GET', 'POST'])
def modele_ajouter():
    form = FormModels()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""INSERT INTO t_model (id_model, name_model, fk_sector, bought_date_model, guarantee_date_model, description_model) VALUES (NULL,"{form.name.data.lower()}", "{int(form.fk_sector.data.lower())}", "{form.bought_date_model.data}", "{form.guarantee_date_model.data}", "{form.description_model.data.lower()}")"""
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

    return render_template("genres/modele_ajouter.html", form=form)


@obj_mon_application.route("/use_ajouter", methods=['GET', 'POST'])
def use_ajouter():
    form = FormUse()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""INSERT INTO t_use (id_start_use, fk_device, fk_customer, date_start_use, date_end_use, reason_end_use) 
                                        VALUES (NULL,{int(form.fk_device.data)}, {int(form.fk_customer.data)}, "{form.date_start_use.data}", "{form.date_end_use.data}", "{form.reason_end_use.data.lower()}")"""
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

    return render_template("genres/use_ajouter.html", form=form)


@obj_mon_application.route("/sector_ajouter", methods=['GET', 'POST'])
def sector_ajouter():
    form = FormSectors()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""INSERT INTO t_sector (id_sector, name_sector) VALUES (NULL,"{form.name.data.lower()}")"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('sector_afficher', order_by='DESC', id_sector=0))

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

    return render_template("genres/sector_ajouter.html", form=form)


@obj_mon_application.route("/statut_ajouter", methods=['GET', 'POST'])
def status_ajouter():
    form = FormStatus()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""INSERT INTO t_status (id_status, name_status) VALUES (NULL,"{form.name.data.lower()}")"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('status_afficher', order_by='DESC', id_status=0))

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

    return render_template("genres/statut_ajouter.html", form=form)


@obj_mon_application.route('/genre_delete/<int:id>', methods=['GET', 'POST'])
def genre_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

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


@obj_mon_application.route('/customer_delete/<int:id>', methods=['GET', 'POST'])
def customer_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee() as mconn_bd:
                trsql_genres_afficher = f"""DELETE FROM t_customer WHERE id_customer = {id}"""
                mconn_bd.mabd_execute(trsql_genres_afficher)

            flash(f"Données supprimées !!", "success")
            print(f"Données supprimées !!")

            return redirect(url_for('customers_afficher', order_by='ASC', id_customer=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")


@obj_mon_application.route('/model_delete/<int:id>', methods=['GET', 'POST'])
def model_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

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


@obj_mon_application.route('/use_delete/<int:id>', methods=['GET', 'POST'])
def use_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

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


@obj_mon_application.route('/sector_delete/<int:id>', methods=['GET', 'POST'])
def sector_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee() as mconn_bd:
                trsql_genres_afficher = f"""DELETE FROM t_sector WHERE id_sector = {id}"""
                mconn_bd.mabd_execute(trsql_genres_afficher)

            flash(f"Données supprimées !!", "success")
            print(f"Données supprimées !!")

            return redirect(url_for('sector_afficher', order_by='ASC', id_sector=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")


@obj_mon_application.route('/status_delete/<int:id>', methods=['GET', 'POST'])
def status_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee() as mconn_bd:
                trsql_genres_afficher = f"""DELETE FROM t_status WHERE id_status = {id}"""
                mconn_bd.mabd_execute(trsql_genres_afficher)

            flash(f"Données supprimées !!", "success")
            print(f"Données supprimées !!")

            return redirect(url_for('status_afficher', order_by='ASC', id_status=0))

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
                strsql_insert_genre = f"""UPDATE t_device SET serial_number_device = "{form.sn.data.lower()}", fk_model = {(int(form.fk_model.data))}, fk_status = {(int(form.fk_status.data))} WHERE id_device = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")


                return redirect(url_for('device_afficher', order_by='ASC', id_device=0))
        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)


@obj_mon_application.route('/customer_edit/<int:id>', methods=['GET', 'POST'])
def customer_edit(id):
    form = FormCustomers()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""UPDATE t_customer SET first_name_customer = "{form.first_name.data.lower()}", last_name_customer = "{form.last_name.data.lower()}", fk_sector = "{int(form.sector.data)}", phone_customer = "{int(form.phone_customer.data)}", personal_number_customer = "{int(form.personal_number_customer.data)}", location_customer = "{int(form.location.data)}" WHERE id_customer = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('customers_afficher', order_by='ASC', id_customer=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/customers_ajouter.html", form=form)


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
                strsql_insert_genre = f"""UPDATE t_model SET name_model = "{form.name.data.lower()}", fk_sector = "{int(form.fk_sector.data)}", bought_date_model = "{(form.bought_date_model.data)}", guarantee_date_model = "{(form.guarantee_date_model.data)}", description_model = "{(form.description_model.data.lower())}" WHERE id_model = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('modele_afficher', order_by='ASC', id_modele=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/modele_ajouter.html", form=form)


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
                strsql_insert_genre = f"""UPDATE t_use SET fk_device = "{form.fk_device.data.lower()}", fk_customer = "{(form.fk_customer.data.lower())}", date_start_use = "{(form.date_start_use.data)}", date_end_use = "{(form.date_end_use.data)}", reason_end_use = "{(form.reason_end_use.data.lower())}" WHERE id_start_use = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('use_afficher', order_by='ASC', id_use=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/use_ajouter.html", form=form)


@obj_mon_application.route('/sector_edit/<int:id>', methods=['GET', 'POST'])
def sector_edit(id):
    form = FormSectors()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""UPDATE t_sector SET name_sector = "{form.name.data.lower()}" WHERE id_sector = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('sector_afficher', order_by='ASC', id_sector=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/sector_ajouter.html", form=form)


@obj_mon_application.route('/status_edit/<int:id>', methods=['GET', 'POST'])
def status_edit(id):
    form = FormStatus()
    if request.method == "POST":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                strsql_insert_genre = f"""UPDATE t_status SET name_status = "{form.name.data.lower()}" WHERE id_status = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('status_afficher', order_by='ASC', id_status=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    return render_template("genres/statut_ajouter.html", form=form)
