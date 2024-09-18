from django.http import HttpResponse, HttpRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import ProductCreationForm
from .models import *


def all_recipes(request: HttpRequest):
    recipes = Product.objects.all()
    recipe_list = [recipe for recipe in recipes]

    return render(request, "main.html", {"recipes": recipe_list})


@require_POST
@csrf_protect
def add_suggestion(request):
    request_obj = request.POST
    try:
        ps = ProductSuggestion(
            name=request_obj.get("name"), description=request_obj.get("description")
        )
    except:
        pass
    ps.save()

    return HttpResponse({"message": "Object successfully created!"}, status=201)


def create_product(request):
    form = ProductCreationForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("all_recipes")

    return render(request, "product-creation.html", {"form": form})


# fetch all products in json
def fetch_products_json(request):
    queryset = Product.objects.all()
    return HttpResponse(
        serializers.serialize("json", queryset), content_type="application/json"
    )


# fetch all products in xml
def fetch_products_xml(request):
    queryset = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", queryset), content_type="application/xml"
    )


# fetch product json by id
def fetch_product_json_by_id(request, id):
    queryset = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", queryset), content_type="application/json"
    )


# fetch product xml by id
def fetch_product_xml_by_id(request, id):
    queryset = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", queryset), content_type="application/xml"
    )


def create_order(request):
    return HttpResponse("No response yet")
