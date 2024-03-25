from django.contrib import admin
from modelManagement.models import Person


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname",)

admin.site.register(Person)
