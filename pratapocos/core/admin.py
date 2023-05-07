from django.contrib import admin

from .models import ActivityLog, Cadastro


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class CadastroAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Cadastro, CadastroAdmin)
