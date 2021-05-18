from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


class Validators:
    name = [Length(min=2, max=20, message='Entre 2 et 20 caractères'),
            Regexp(regex="^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$",
                   message="Pas de chiffres, de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")]

    sn = [Length(min=2, max=50, message='Entre 2 et 50 caractères'),
          Regexp(regex="([0-9]1?[a-z]?[A-Z]?)*",
                 message="Pense à mettre un message")]

    fk = [Regexp(regex="^[1-9]\\d*$",
                 message="Pense à mettre un message")]


class Form(Validators, FlaskForm):
    submit = SubmitField("Enregistrer")


class FormCustomers(Form):
    first_name = StringField("Clavioter le prénom ", validators=Validators().name)
    last_name = StringField("Clavioter le nom de famille ", validators=Validators().name)
    phone_customer = StringField("Clavioter le numéro de l'employé ", validators=Validators().fk)
    personal_number_customer = StringField("Clavioter le numéro privé de l'employé ", validators=Validators().fk)
    location = StringField("Clavioter la localisation ", validators=Validators().name)


class FormDevices(Form):
    sn = StringField("Clavioter le numéro de série ", validators=Validators().sn)


class FormModels(Form):
    name = StringField("Clavioter le modèle ", validators=Validators().name)
    bought_date_model = DateField("Écris la date de l'achat")
    guarantee_date_model = DateField("Écris la date de fin garantit")
    description_model = StringField("Clavioter la description ", validators=Validators().name)


class FormSectors(Form):
    name = StringField("Clavioter le Secteur ", validators=Validators().name)


class FormLocations(Form):
    name = StringField("Clavioter la localisation ", validators=Validators().name)


class FormStatus(Form):
    name = StringField("Clavioter le Status ", validators=Validators().name)


class FormUse(Form):
    date_start_use = DateField("Écris la date d'utilisation")
    date_end_use = DateField("Écris la date de fin d'utilisation")
    reason_end_use = StringField("Clavioter la raison ", validators=Validators().name)
    # id_start_use = StringField("ça ne sert a rien ", validators=Validators().fk)
