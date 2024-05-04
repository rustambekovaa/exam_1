from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404


from moobile.models import Product, Category
from moobile.filters import ProductFilter

def index(request):
    products = Product.objects.all()  
    # if request.user.is_authenticated:
    #     products = Product.objects.filter(author=request.user)   
    search = request.GET.get('search')

    if search:
        products = products.filter(title__icontains=search)

    filter_set = ProductFilter(request.GET, queryset=products)

    paginator = Paginator(filter_set.qs,8) 
    page = request.GET.get('page', 1) 

    products = paginator.get_page(page)

    cats = Category.objects.all()
    context = {
        
        'products':products,
        'cats':cats,
    }
    return render(request, 'index.html',{'context':context,'products': products,'filter': filter_set})


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