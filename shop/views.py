from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def catalog(request):
    products = Product.objects.filter(active=True).select_related('category')
    categories = Category.objects.all()
    slug = request.GET.get('category')
    if slug:
        products = products.filter(category__slug=slug)
    return render(request, 'shop/catalog.html', {
        'products': products,
        'categories': categories,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, active=True)
    return render(request, 'shop/detail.html', {'product': product})
