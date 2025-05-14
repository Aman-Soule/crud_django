from django.shortcuts import redirect, render
from .models import Medecin
# Create your views here.
#page permettant de créer nos fonctions (ex: ajout, supressions, ...)
def index(request):
    med = Medecin.objects.all()
    return render(request, 'index.html',{'med':med})

def add(request):
    return render(request, 'add.html')

def addMedecin(request):
    x = request.POST['nom']
    y = request.POST['prenom']
    z = request.POST['service']
    
    med = Medecin(nom=x, prenom = y, service = z)
    med.save()
    return redirect("/")

def delete(request, id):
    med = Medecin.objects.get(id=id)
    med.delete()
    return redirect("/")

def modifier(request, id):
    med = Medecin.objects.get(id = id)
    return render(request,'modifier.html', {'med':med})
def modifierMed(request,id):
    x = request.POST['nom']
    y = request.POST['prenom']
    z = request.POST['service']
    med = Medecin.objects.get(id = id)
    med.nom = x
    med.prenom = y
    med.service = z
    med.save()
    
    return redirect("/")