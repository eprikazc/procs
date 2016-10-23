from django.contrib.auth.models import Group
from registration.backends.default.views import RegistrationView
from rest_framework import routers, viewsets

from .models import Proc, Bread, Hat, Money, Doc, Person
from .serializers import (
    ProcSerializer, BreadSerializer, HatSerializer, MoneySerializer,
    DocSerializer, PersonSerializer)


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


router = routers.DefaultRouter()


class HatViewSet(viewsets.ModelViewSet):
    queryset = Hat.objects.all()
    serializer_class = HatSerializer


class BreadViewSet(viewsets.ModelViewSet):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer


class ProcViewSet(viewsets.ModelViewSet):
    queryset = Proc.objects.all()
    serializer_class = ProcSerializer


class MoneyViewSet(viewsets.ModelViewSet):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer


class DocViewSet(viewsets.ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


router.register('hats', HatViewSet)
router.register('breads', BreadViewSet)
router.register('procs', ProcViewSet)
router.register('money', MoneyViewSet)
router.register('docs', DocViewSet)
router.register('people', PersonViewSet)
