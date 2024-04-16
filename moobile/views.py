from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404


from moobile.models import Product, Category

def index(request):
    products = Product.objects.all()    
    search = request.GET.get('search')

    if search:
        products = products.filter(title__icontains=search)

    paginator = Paginator(products,8) 
    page_number = request.GET.get('page', 1) 
    page = paginator.page(1) 

    page = paginator.page(page_number)

    cats = Category.objects.all()
    context = {
        
        'products':page,
        'cats':cats,
    }
    return render(request, 'index.html', context)


def addproduct(request): 
    return render(request,'addproduct.html', {'title':'Добавление статьи '})

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def datails_category(request, cat_id):
    category1 = Category.objects.get(pk=cat_id)
    product = Product.objects.filter(category=category1)
    return render(request, 'datails_category.html', {'category1': category1, 'product': product})


def consistproduct(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'consistproduct.html', {'product': product})