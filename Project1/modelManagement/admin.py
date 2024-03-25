from django.contrib import admin
from modelManagement.models import Politic, PartitPolitic, Reunio


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname",)

admin.site.register(Politic)
admin.site.register(PartitPolitic)
admin.site.register(Reunio)
