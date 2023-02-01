from django.shortcuts import render, redirect

from django.views.generic import View

from .forms import UserCreationForm, AddressCreationForm
from .models import UserAddress


class HomeView(View):
    """Vue gérant l'affichage de la page d'accueil."""

    form_classes = [UserCreationForm, AddressCreationForm]
    template_name = "wepynaire/home.html"
    success_url = "wepynaire:home"

    def get(self, request):
        """Réponds aux requêtes GET."""
        forms = [form() for form in self.form_classes]
        return render(
            request,
            self.template_name,
            {"forms": forms},
        )

    def post(self, request):
        """Réponds aux requêtes POST."""
        forms = [form(request.POST) for form in self.form_classes]
        if all(form.is_valid() for form in forms):
            # Tous les formulaires sont valides
            user_form, address_form = forms
            user = user_form.save()
            address = address_form.save()
            address_type = address_form.cleaned_data.get("address_type")
            UserAddress.objects.create(
                user=user,
                address=address,
                address_role=address_type,
            )
            return redirect(self.success_url)
        else:
            # au moins un formulaire est invalide
            return render(
                request,
                self.template_name,
                {"forms": forms},
            )


home_view = HomeView.as_view()
