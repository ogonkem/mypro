from django.contrib import admin
from .models import TargetAudience, ProjectRequirements

# Register your models here.
class TargetAudienceAdmin(admin.ModelAdmin):
    list_display = ('target_name',)
    list_per_page = 20

class ProjectRequirementsAdmin(admin.ModelAdmin):
    list_display = ('product', 'code_language', 'have_buildups', 'have_design_elements')
    list_filter = ['have_buildups', 'have_design_elements']
    list_per_page = 20

admin.site.register(TargetAudience, TargetAudienceAdmin)
admin.site.register(ProjectRequirements, ProjectRequirementsAdmin)
