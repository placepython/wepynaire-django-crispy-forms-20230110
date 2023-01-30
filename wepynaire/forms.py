from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from .models import UserAddress, Address

User = get_user_model()


class UserCreationForm(auth_forms.UserCreationForm):
    """Formulaire de souscription pour les utilisateurs."""

    class Meta(auth_forms.UserCreationForm):
        model = User
        fields = ("name", "username")


class AddressCreationForm(forms.ModelForm):
    """Formulaire de création pour une adresse."""

    address_type = forms.ChoiceField(label="type de l'adresse")

    class Meta:
        model = Address
        fields = (
            "street",
            "street_number",
            "address_complement",
            "city",
            "zip_code",
            "country",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address_type"].choices = UserAddress.AdresseRoles.choices
