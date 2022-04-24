from django import forms
from project.models import ProjectRequirements, TargetAudience

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectRequirements
        fields = [
            'product',
            'solution_description',
            'project_target',
            'code_language_preference',
            'code_language',
            'have_buildups',
            'buildups',
            'have_design_elements',
            'design_elements']

    # function to loop through form fields and initiat form-control class
    def __init__(self, target_audience, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs) # modify what django is giving
        self.fields['product'].widget.attrs['placeholder'] = 'Choose your product'

        self.fields['solution_description'].widget.attrs['placeholder'] = 'Solution description'
        self.fields['solution_description'].widget.attrs['rows'] = 3

        self.fields['project_target'].widget.attrs['placeholder'] = 'Target Audience'
        self.fields['project_target'].queryset = TargetAudience.objects.filter(id__in=target_audience)

        self.fields['code_language_preference'].widget.attrs['placeholder'] = 'Do you have a coding language preference?'
        self.fields['code_language_preference'].widget.attrs['class'] = 'form-check-input form-control'
        self.fields['code_language'].widget.attrs['placeholder'] = 'If yes, what would it be?'

        self.fields['have_buildups'].widget.attrs['placeholder'] = 'Do you hae a map of your software build up?'
        self.fields['have_buildups'].widget.attrs['class'] = 'form-check-input form-control'
        self.fields['buildups'].widget.attrs['placeholder'] = 'If yes (please upload it)'

        self.fields['have_design_elements'].widget.attrs['placeholder'] = 'Do you hae a map of your software design elements?'
        self.fields['have_design_elements'].widget.attrs['class'] = 'form-check-input form-control'
        self.fields['design_elements'].widget.attrs['placeholder'] = 'If yes (please upload it)'

        for field in ('product', 'solution_description', 'project_target', 'code_language', 'buildups', 'design_elements'):
            self.fields[field].widget.attrs['oninput'] = "this.className = ''"
            self.fields[field].widget.attrs['class'] = 'form-control'
