from django.shortcuts import render
from Family.models import Miembro

def create_member (request):
    miembro_1 = Miembro.objects.create (name="Daniel", gender = "Male", birth = 1980-1-14, age = 42)
    miembro_2 = Miembro.objects.create (name="Laura", gender = "Female", birth = 1984-6-27, age = 38)
    miembro_3 = Miembro.objects.create (name="Agustin", gender = "Male", birth = 2002-1-19, age = 20)
    miembro_4 = Miembro.objects.create (name="Catalina", gender = "Female", birth = 2012-10-5, age = 9)

    context = {
        "new_member_1" : miembro_1,
        "new_member_2" : miembro_2,
        "new_member_3" : miembro_3,
        "new_member_4" : miembro_4
    }
    return render (request, "familia.html", context=context)

def list_miembros(request):
    miembro = Miembro.objects.all()
    context = {
        'miembro' : miembro
    }
    return render(request, 'lista_familia.html', context=context) #Creamos otro html 




