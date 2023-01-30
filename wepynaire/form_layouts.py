from crispy_forms.layout import Layout, Row, Column, Fieldset, Field


class UserCreationLayout(Layout):
    """Mise en page pour le formulaire de création
    d'utisateur."""

    def __init__(self):
        super().__init__(
            Fieldset(
                "Données de connexion",
                Row(
                    Column(Field("name", placeholder="Votre nom")),
                    Column(Field("username", placeholder="Votre username")),
                ),
                Row(
                    Column(
                        Field("password1", placeholder="Votre mot de passe")
                    ),
                    Column(
                        Field(
                            "password2", placeholder="Répétez le mot de passe"
                        )
                    ),
                ),
                # Utilisez des classes css pour le style
                style="""
                    border: 1px black solid; 
                    border-radius: 10px; 
                    margin-bottom: 1rem;
                """,
            ),
        )


class AddressCreationLayout(Layout):
    """Mise en page pour le formulaire de création
    d'adresse."""

    def __init__(self):
        super().__init__(
            Fieldset(
                "Adresse",
                Row(
                    Column(
                        Field("street", placeholder="Votre rue"),
                        css_class="col-md-10",
                    ),
                    Column(
                        Field("street_number", placeholder="N°"),
                        css_class="col-md-2",
                    ),
                ),
                Row(
                    Field(
                        "address_complement",
                        placeholder="Votre complément d'adresse",
                    ),
                ),
                Row(
                    Column(
                        Field("zip_code", placeholder="Code postal"),
                        css_class="col-md-4",
                    ),
                    Column(Field("city", placeholder="Votre ville")),
                ),
                Row("country", placeholder="Votre pays"),
                # Utilisez des classes css pour le style
                style="""
                        border: 1px black solid; 
                        border-radius: 10px; 
                        margin-bottom: 1rem;
                    """,
            ),
        )
