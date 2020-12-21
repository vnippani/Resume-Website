from django.shortcuts import render,get_object_or_404
from .models import Project
from django.http import HttpResponse

# Create your views here.
def home(request):
	projects = Project.objects.all() #grabs all objects from the database that are project objects
	return render(request,'rWebsite/home.html',{'projects':projects})

def detail(request, proj_id):
	project = get_object_or_404(Project,pk=proj_id) #returns 404 if can't grab id
	return render(request,'rWebsite/detail.html',{'project':project})