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
    sector = StringField("Clavioter le secteur ", validators=Validators().fk)
    location = StringField("Clavioter la localisation ", validators=Validators().fk)
    phone_customer = StringField("Clavioter le numéro de l'employé ", validators=Validators().fk)
    personal_number_customer = StringField("Clavioter le numéro privé de l'employé ", validators=Validators().fk)


class FormDevices(Form):
    fk_model = StringField("Clavioter le model de l'appareil ", validators=Validators().fk)
    sn = StringField("Clavioter le numéro de série ", validators=Validators().sn)
    fk_status = StringField("Clavioter le status de l'appareil ", validators=Validators().fk)


class FormModels(Form):
    name = StringField("Clavioter le modèle ", validators=Validators().name)
    fk_sector = StringField("Clavioter le secteur ", validators=Validators().fk)
    bought_date_model = DateField("écris la date de l'achat")
    guarantee_date_model = DateField("écris la date de fin garantit")
    description_model = StringField("Clavioter la description ", validators=Validators().name)


class FormSectors(Form):
    name = StringField("Clavioter le secteur ", validators=Validators().name)


class FormLocations(Form):
    name = StringField("Clavioter la location de ski ", validators=Validators().name)


class FormStatus(Form):
    name = StringField("Clavioter le secteur ", validators=Validators().name)


class FormUse(Form):
    fk_device = StringField("Clavioter le secteur ", validators=Validators().fk)
    fk_customer = StringField("Clavioter le client  ", validators=Validators().fk)
    date_start_use = DateField("écris la date d'utilisation")
    date_end_use = DateField("écris la date de fin d'utilisation")
    reason_end_use = StringField("Clavioter la raison ", validators=Validators().name)
    # id_start_use = StringField("ça ne sert a rien ", validators=Validators().fk)
