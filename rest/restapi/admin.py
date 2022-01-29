from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import *
from .models import User


class UserAdminNew(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_photo')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'photo', 'date_of_birth', 'gender'),
        }),
    )

    def get_photo(self, obj):   # вывод картинки новости в админке джанго
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')  # mark_safe помечает строку как хтмл_код и не экранирует
        else:   # не обязательно
            return 'Фото не установлено'

    get_photo.short_description = 'photo_view'

admin.site.register(User, UserAdminNew)
admin.site.register(Like)