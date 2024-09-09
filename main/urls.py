from django.urls import path

from .views import *

urlpatterns = [
    path("", all_recipes, name="all_recipes"),
    path("add_suggestion/", add_suggestion, name="add_suggestion"),
    path("create_order/", create_order, name="create_order"),
]
