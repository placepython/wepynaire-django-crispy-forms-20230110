from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from crispy_forms.helper import FormHelper

from .models import UserAddress, Address
from .form_layouts import UserCreationLayout, AddressCreationLayout

User = get_user_model()


class UserCreationForm(auth_forms.UserCreationForm):
    """Formulaire de souscription pour les utilisateurs."""

    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ("name", "username")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = UserCreationLayout()


class AddressCreationForm(forms.ModelForm):
    """Formulaire de création pour une adresse."""

    address_type = forms.ChoiceField(label="Type de l'adresse")

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

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = AddressCreationLayout()
