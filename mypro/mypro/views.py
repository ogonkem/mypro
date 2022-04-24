from django.shortcuts import render, redirect
from project.models import ProjectRequirements, TargetAudience
from project.forms import ProjectForm
from django.contrib import messages

# Create your views here.
def project(request):
    target_audience = TargetAudience.objects.all()
    if request.method == 'POST':
        form = ProjectForm(target_audience, request.POST, request.FILES)
        if form.is_valid():
            data = ProjectRequirements()
            data.product = form.cleaned_data['product']
            data.solution_description = form.cleaned_data['solution_description']
            data.code_language_preference = form.cleaned_data['code_language_preference']
            data.code_language = form.cleaned_data['code_language']
            data.have_buildups = form.cleaned_data['have_buildups']
            data.buildups = form.cleaned_data['buildups']
            data.have_design_elements = form.cleaned_data['have_design_elements']
            data.design_elements = form.cleaned_data['design_elements']
            data.save()

            ta = TargetAudience.objects.filter(id__in = form.cleaned_data['project_target'])
            data.project_target.add(*ta)

            messages.success(request, 'Thank you! Your Service has been created.')
            return redirect('project')
    else:
        form = ProjectForm(target_audience)

    context = {
        'form': form,
    }

    return render(request, 'requirements_form.html', context)
