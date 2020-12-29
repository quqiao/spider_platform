from django.contrib import admin
from demo.models import Test, Contact, User, Tag

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'age')
    inlines = [TagInline]
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
