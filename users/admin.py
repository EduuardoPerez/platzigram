""" User admin classes """

# Django:
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models:
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): # Por convención se coloca el nombre del modelo seguido de la palabra Admin

    # Variable con los campos a mostrar en el dashboard.
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture',
    )

    # Variable con los campos que serán links.
    list_display_links = (
        'pk',
        'user',
    )

    # Variable con los campos editables desde dashboard| Nota: No puede haber campos link y editables a la vez.
    list_editable = (
        'phone_number',
        'website',
        'picture',
    )

    # Variable con los campos por los que podemos realizar una busqueda.
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )

    # Variable que añade un campo por el cual filtrar los datos.
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )

    # Set fieldsets to control the layout of admin “add” and “change” pages. fieldsets is a list of two-tuples, in which each two-tuple represents a <fieldset> on the admin form page. (A <fieldset> is a “section” of the form.)
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )

    readonly_fields = ('created', 'modified')


"""
Une los modelos de usuario y perfil para no tener que crear un usuario para asociarlo con un perfil
"""
class ProfileInLine(admin.StackedInline):
    """ Profile in-line admin for users """

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin """

    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User,UserAdmin)