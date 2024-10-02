from django.urls import path

from .views import *

urlpatterns = [
    path("", all_recipes, name="all_recipes"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("create_product/", create_product, name="create_product"),
    path("edit_product/<uuid:id>", edit_product, name="edit_product"),
    path("delete_product/<uuid:id>", delete_product, name="delete_product"),
    path("add_suggestion/", add_suggestion, name="add_suggestion"),
    path("create_order/", create_order, name="create_order"),
    path("json/", fetch_products_json, name="fetch_products_json"),
    path("xml/", fetch_products_xml, name="fetch_products_xml"),
    path(
        "json/<str:id>/",
        fetch_product_json_by_id,
        name="fetch_product_json_by_id",
    ),
    path(
        "xml/<str:id>/",
        fetch_product_xml_by_id,
        name="fetch_product_xml_by_id",
    ),
]
