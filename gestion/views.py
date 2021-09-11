from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound

from .models import Product
from .forms import ProductForm


# Create your views here.+

def index(request):

    page_number = request.GET.get('page')

    products_page = Paginator(Product.objects.all(),2)

    try:
        products = products_page.page(page_number) #get_page
    except PageNotAnInteger:
        products = products_page.page(1)
    except EmptyPage:
        products = products_page.page(1)

    return render(request, 'index.html', { 'products' : products })

def show(request,pk):

    product = get_object_or_404(Product, id=pk)
    
    """try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        #return HttpResponse(status=404)
        return HttpResponseNotFound()"""


    return render(request, 'show.html', { 'product' : product })

def create(request):

    form = ProductForm()

    if request.method == "POST":
        #print(request.POST['title'])
        form = ProductForm(request.POST)

        if form.is_valid():
            print("Valido")
            #form.save()

            product = Product()

            product.title = form.cleaned_data['title']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']

            product.save()

            return redirect('gestion:update', pk=product.id)

        else:
            print("Invalido")

    return render(request, 'save.html', { 'form' : form })

def update(request,pk):

    product = get_object_or_404(Product, id=pk)

    form = ProductForm(initial={'title':product.title,'description':product.description,'price':product.price,'category':product.category,} )

    if request.method == "POST":
        #print(request.POST['title'])
        form = ProductForm(request.POST)

        if form.is_valid():
            print("Valido")
            #form.save()

            product.title = form.cleaned_data['title']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']

            product.save()

            return redirect('gestion:index')

        else:
            print("Invalido")

    return render(request, 'save.html', { 'form' : form })

def delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()

    return redirect('gestion:index')