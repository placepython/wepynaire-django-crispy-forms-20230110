from django.shortcuts import render, redirect

from django.views.generic import View

from .forms import UserCreationForm, AddressCreationForm
from .models import UserAddress

# Création d'une CBV simpliste pour gérer plusieurs formulaires
class MultiFormsView(View):
    """Vue générique simple gérant plusieurs formulaires."""

    template_name = None
    form_classes = None
    success_url = None

    def get_forms(self):
        return [form(self.request.POST or None) for form in self.form_classes]

    def render_to_response(self, **context):
        """Retourne le template avec le contexte."""
        return render(
            self.request,
            self.template_name,
            context,
        )

    def all_valid(self):
        """Retourne True si tous les formulaires sont valides."""
        if all(form.is_valid() for form in self.forms):
            return True
        return False

    def form_valid(self):
        """Actions à entreprendre si tous les formulaires sont valides."""
        return redirect(str(self.success_url))

    def form_invalid(self):
        """Actions à entreprendre si un formulaire est invalide."""
        return self.render_to_response(forms=self.forms)

    def get(self, request, *args, **kwargs):
        """Réponds à l'affichage du formulaire."""
        self.forms = self.get_forms()
        return self.render_to_response(forms=self.forms)

    def post(self, request, *args, **kwargs):
        """Réponds à la soumission du formulaire."""
        self.forms = self.get_forms()
        if self.all_valid():
            return self.form_valid()
        else:
            return self.form_invalid()


# Création de notre HomeView à l'aide de la CBV réutilisable
class HomeView(MultiFormsView):
    """Vue gérant la page d'accueil du site."""

    template_name = "wepynaire/home.html"
    form_classes = [UserCreationForm, AddressCreationForm]
    success_url = "wepynaire:home"

    def form_valid(self):
        user_form, address_form = self.forms
        user = user_form.save()
        address = address_form.save()
        address_type = address_form.cleaned_data.get("address_type")
        UserAddress.objects.create(
            user=user,
            address=address,
            address_role=address_type,
        )
        return super().form_valid()


home_view = HomeView.as_view()
