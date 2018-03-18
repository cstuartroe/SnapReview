from django.shortcuts import render

def install(request):
    return render(request, 'shopify_install/install.php')

def generate_token(request):
    return render(request, 'shopify_install/generate_token.php')

def functions(request):
    return render(request, 'shopify_install/functions.php')

def api_call_write_products(request):
    return render(request, 'shopify_install/api_call_write_products.php')
