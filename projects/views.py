from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import ProjectForm


def home(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'projects/home.html', {"projects": projects})
def project(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'projects/project.html', {"project": project})
def submit_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            saved_project = form.save()
            return redirect(f"/project/{saved_project.id}")
    return render(request, 'projects/submit_project.html', {'form': form})
