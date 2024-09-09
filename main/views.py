from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .models import *

def all_recipes(request):
    recipes = Product.objects.all()
    recipe_list = [recipe for recipe in recipes]

    return render(request, "main.html", {"recipes": recipe_list})

@require_POST
@csrf_protect 
def add_suggestion(request: HttpRequest):
    request_obj = request.POST
    try:
        ps = ProductSuggestion(name=request_obj.get("name"), description=request_obj.get("description"))
    except:
        pass
    ps.save()

    return HttpResponse("Object successfully created!", status=201)
