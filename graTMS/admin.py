from django.contrib import admin
from graTMS.models import *
from graTMS.forms import ComplaintForm
# Register your models here.


class ComplaintAdmin(admin.ModelAdmin):
    form = ComplaintForm

    list_display = ('complaint', 'date', 'user')
    prepopulated_fields = {'slug': ['complaint']}
    readonly_fields = ('last_modified', 'last_modified_by',)
    fieldsets = ((
        None, {
            'fields': ('complaint', 'office', 'date')
        }), (
        'Other Information', {
            'fields': ('last_modified', 'last_modified_by', 'slug'),
            'classes': ('collapse',)
        })
    )

    def save_model(self, request, obj, form, change):
        if not obj.user.id:
            obj.user = request.user
        obj.last_modified_by = request.user
        obj.save()


class Complaint_Admin(admin.ModelAdmin):
    list_display = ['user', 'office', 'room', 'complaint', 'solution',
                    'status', 'additional_Info', 'date', 'signatory', 'signature']


admin.site.register(Complaint, Complaint_Admin)
