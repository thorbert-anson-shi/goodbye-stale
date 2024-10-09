import datetime
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils.html import strip_tags
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import ProductCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import *


def register(request: HttpRequest):
    # Create empty form to return during initial render
    form = UserCreationForm()

    if request.method == "POST":
        # Create user if request is a POST request
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "register.html", {"form": form})


def login_user(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("all_recipes"))
            response.set_cookie(
                "last_login", str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
            )
            return response
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})


def logout_user(request: HttpRequest):
    logout(request)
    response = HttpResponseRedirect(reverse("all_recipes"))
    response.delete_cookie("last_login")
    return response


@login_required(login_url="login")
def all_recipes(request: HttpRequest):
    if Product.objects.filter(creator=request.user).exists():
        empty = False
    else:
        empty = True

    context = {
        "product_categories": Product.Category.choices,
        "empty": empty,
        "user": request.user or None,
        "last_login": (
            request.COOKIES["last_login"] if "last_login" in request.COOKIES else None
        ),
    }

    return render(request, "main.html", context)


@require_POST
@csrf_protect
def add_suggestion(request: HttpRequest):
    request_obj = request.POST
    try:
        ps = ProductSuggestion(
            name=request_obj.get("name"), description=request_obj.get("description")
        )
    except:
        pass
    ps.save()

    return HttpResponse({"message": "Object successfully created!"}, status=201)


@login_required(login_url="login")
def create_product(request: HttpRequest):
    form = ProductCreationForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.creator = request.user
        product.save()
        return redirect("all_recipes")

    return render(request, "product_creation.html", {"form": form})


@require_POST
def create_product_ajax(request: HttpRequest):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    ingredients = strip_tags(request.POST.get("ingredients"))
    category = strip_tags(request.POST.get("category"))

    new_product = Product(
        name=name,
        price=price,
        description=description,
        ingredients=ingredients,
        category=category,
        creator=request.user,
    )
    new_product.save()

    return HttpResponse("Created", status=201)


@login_required(login_url="login")
def edit_product(request: HttpRequest, id: uuid.UUID):
    product = Product.objects.get(pk=id)

    form = ProductCreationForm(request.POST or None, instance=product)

    if form.is_valid() and product.creator == request.user and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("all_recipes"))

    return render(request, "product_creation.html", {"form": form})


@login_required(login_url="login")
def delete_product(request: HttpRequest, id=uuid.UUID):
    product = Product.objects.get(pk=id)

    if product.creator == request.user:
        product.delete()

    return redirect("all_recipes")


# fetch all products in json
def fetch_products_json(request: HttpRequest):
    queryset = Product.objects.filter(creator=request.user)

    return HttpResponse(
        serializers.serialize("json", queryset), content_type="application/json"
    )


# fetch all products in xml
def fetch_products_xml(request: HttpRequest):
    queryset = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", queryset), content_type="application/xml"
    )


# fetch product json by id
def fetch_product_json_by_id(request: HttpRequest, id):
    queryset = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", queryset), content_type="application/json"
    )


# fetch product xml by id
def fetch_product_xml_by_id(request: HttpRequest, id):
    queryset = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", queryset), content_type="application/xml"
    )


def create_order(request: HttpRequest):
    return HttpResponse("No response yet")
