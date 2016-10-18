from django.contrib.auth.models import Group
from registration.backends.default.views import RegistrationView


class CustomRegistrationView(RegistrationView):
    success_url = '/admin/'

    def register(self, form):
        user = super().register(form)
        user.is_staff = True
        user.is_active = True
        proc_editors_group = Group.objects.filter(name='proc_editors').first()
        if proc_editors_group:
            user.groups.add(proc_editors_group)
        user.save()
        return user
