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
                    strsql_genres_afficher = """SELECT id_customer, first_name_customer, last_name_customer, name_sector, phone_customer, personal_number_customer, location_customer
                                                    FROM t_customer 
                                                           LEFT JOIN t_sector ON id_sector = fk_sector
                                                ORDER BY id_customer ASC"""
                    mc_afficher.execute(strsql_genres_afficher)

                else:
                    strsql_genres_afficher = """SELECT id_customer, first_name_customer, last_name_customer, name_sector, phone_customer, personal_number_customer, location_customer 
                                                    FROM t_customer 
                                                        LEFT JOIN t_sector ON id_sector = fk_sector
                                                ORDER BY id_customer DESC"""
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


@obj_mon_application.route("/customer_ajouter", methods=['GET', 'POST'])
def customer_ajouter():
    form = FormCustomers()
    if request.method == "POST":
        if form.validate_on_submit() and request.form.getlist('secteur')[0] != 'placeholder':
            print(int(request.form.getlist('secteur')[0]))
            try:
                try:
                    MaBaseDeDonnee().connexion_bd.ping(False)

                except Exception as erreur:
                    flash("Il faut connecter une base de données", "danger")
                    raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

                if form.validate_on_submit():
                    strsql_insert_genre = f"""INSERT INTO t_customer (id_customer, first_name_customer, last_name_customer, fk_sector, phone_customer, personal_number_customer, location_customer) 
                                             VALUES (NULL,"{form.first_name.data.lower()}", "{form.last_name.data.lower()}", "{int(request.form.getlist('secteur')[0])}", "{int(form.phone_customer.data)}", "{int(form.personal_number_customer.data)}", "{form.location.data}")"""
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

    strsql_insert_genre = f"""SELECT id_sector, name_sector FROM t_sector """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        secteurs = mc_afficher.fetchall()

    return render_template("genres/customers_ajouter.html", form=form, secteurs=secteurs)


@obj_mon_application.route('/customer_delete/<int:id>', methods=['GET', 'POST'])
def customer_delete(id):
    if request.method == "GET":
        try:
            try:
                MaBaseDeDonnee().connexion_bd.ping(False)

            except Exception as erreur:
                flash("Il faut connecter une base de données", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mconn_bd:
                sql = f"""
                        select id_customer, first_name_customer, last_name_customer, date_start_use, date_end_use 
                            from t_customer
                                INNER join t_use ON fk_customer = id_customer

                            Where id_customer = {id}"""

                mconn_bd.execute(sql)
                data = mconn_bd.fetchall()

            return render_template('genres/customer_delete.html', data=data, id=id)

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    elif request.method == "POST":
        try:
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
                strsql_insert_genre = f"""UPDATE t_customer SET first_name_customer = "{form.first_name.data.lower()}", last_name_customer = "{form.last_name.data.lower()}", fk_sector = {request.form.getlist('secteur')[0]}, phone_customer = "{int(form.phone_customer.data)}", personal_number_customer = "{int(form.personal_number_customer.data)}", location_customer = "{form.location.data}" WHERE id_customer = {id}"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre)

                flash(f"Données mises à jour !!", "success")
                print(f"Données mises à jour !!")

                return redirect(url_for('customers_afficher', order_by='ASC', id_customer=0))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")

    elif request.method == "GET":
        strsql_insert_genre = f"""SELECT * FROM t_customer WHERE id_customer = {id}"""
        with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
            mc_afficher.execute(strsql_insert_genre)
            data = mc_afficher.fetchone()

        form.first_name.data = data.get("first_name_customer")
        form.last_name.data = data.get("last_name_customer")
        form.phone_customer.data = data.get("phone_customer")
        form.personal_number_customer.data = data.get("personal_number_customer")
        form.location.data = data.get("location_customer")

    strsql_insert_genre = f"""SELECT id_sector, name_sector FROM t_sector """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        secteurs = mc_afficher.fetchall()

    strsql_insert_genre = f"""SELECT fk_sector FROM t_customer WHERE id_customer = {id} """
    with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
        mc_afficher.execute(strsql_insert_genre)
        used_secteurs = mc_afficher.fetchone()

    print(used_secteurs, secteurs)

    return render_template("genres/customer_edit.html", form=form, secteurs=secteurs, used_secteurs=used_secteurs, id=id)
