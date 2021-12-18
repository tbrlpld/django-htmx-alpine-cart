from django.shortcuts import render


PRODUCTS = [
    "Some item",
]

def list(request):
    count = 3
    cart_items = ["Cart item" for _ in range(count)]
    return render(
        request=request,
        template_name="list_page.html",
        context={"cart_items": cart_items}
    )


