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

    elif request.method == "GET":
        strsql_insert_genre = f"""SELECT * FROM t_sector WHERE id_sector = {id}"""
        with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
            mc_afficher.execute(strsql_insert_genre)
            data = mc_afficher.fetchone()

        form.name.data = data.get("name_sector")





    return render_template("genres/sector_edit.html", form=form, id=id)