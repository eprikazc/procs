from django.contrib import admin

from .models import Proc, Bread, Hat, Money, Doc, Person


class BreadInline(admin.TabularInline):
    model = Bread
    extra = 1


class HatInline(admin.TabularInline):
    model = Hat
    extra = 1


class MoneyInline(admin.TabularInline):
    model = Money
    extra = 1


class DocInline(admin.TabularInline):
    model = Doc
    extra = 1


class ProcAdmin(admin.ModelAdmin):
    inlines = [
        BreadInline, HatInline, MoneyInline
    ]
    actions_on_top = False


admin.site.register(Proc, ProcAdmin)
admin.site.register([Bread, Hat, Money, Doc, Person])
