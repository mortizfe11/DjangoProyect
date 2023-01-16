from django.contrib import admin
from .models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("id","firstname", "lastname", "phone", "joined_date", "slug")
    prepopulated_fields = {"slug": ("firstname", "lastname", "slugh_hash")} #auto-rellena el campo slug con firstname-lastname

admin.site.register(Member, MemberAdmin)