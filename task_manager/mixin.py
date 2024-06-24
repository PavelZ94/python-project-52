from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.utils.translation import gettext_lazy as _


class RulesMixin:

    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                messages.error(self.request, _('You are not authorized!'))
            )
            return redirect('login')

        elif not self.has_permission():
            messages.error(
                request,
                messages.error(self.request, _("You haven't permission!"))
            )
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
