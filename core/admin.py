from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Proc, Bread, Hat, Money, Doc, DocsNode, Person


class GridAdmin(admin.ModelAdmin):
    actions_on_top = False
    change_list_template = 'admin/grid_change_list.html'


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


class ProcAdmin(GridAdmin):
    inlines = [
        BreadInline, HatInline, MoneyInline
    ]


class DocNodeAdmin(DraggableMPTTAdmin):
    inlines = [
        DocInline,
    ]
    list_display = [
        'tree_actions',
        'indented_title',
    ]
    list_display_links = [
        'indented_title',
    ]


admin.site.register(Proc, ProcAdmin)
admin.site.register(DocsNode, DocNodeAdmin)
admin.site.register([Bread, Hat, Money, Doc, Person], GridAdmin)
