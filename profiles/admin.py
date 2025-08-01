from django.contrib import admin
from .models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location')
    search_fields = ('user__username', 'bio', 'location')
    ordering = ('user__username',)
    readonly_fields = ('user',)

    def has_add_permission(self, request):
        return False