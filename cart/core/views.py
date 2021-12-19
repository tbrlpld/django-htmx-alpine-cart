from http import HTTPStatus
import json

from django import http
from django import shortcuts
from django import urls
from django.template import response


PRODUCTS = {
    123: {
        "id": 123,
        "name": "Some item",
    },
}

def list(request):
    cart_items = request.session.get("cart_items", [])
    if not cart_items:
        request.session["cart_items"] = cart_items

    return shortcuts.render(
        request=request,
        template_name="list_page.html",
        context={
            "product": PRODUCTS[123],
        }

    )

def add_item(request):
    product_id = request.POST.get("product_id")
    if not product_id:
        return http.HttpResponseBadRequest()
    else:
        product_id = int(product_id)

    product = PRODUCTS.get(product_id)
    if not product:
        return http.HttpResponseBadRequest()

    cart_items = request.session.get("cart_items")
    cart_items.append(product)
    request.session["cart_items"] = cart_items

    hx_trigger_data = {
        "cart-update": {
            "message": "Cart items have changed.",
            "items": cart_items,
        }
    }
    return response.TemplateResponse(
        request=request,
        template="list.html",
        context={"items": cart_items},
        headers={"HX-Trigger": json.dumps(hx_trigger_data)},
    )

def cart_indicator(request):
    return shortcuts.render(request=request, template_name="cart-indicator-htmx.html")
