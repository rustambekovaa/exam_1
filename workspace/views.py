from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404


from moobile.models import Product, Category, Tag,ProductImage
 


def workspace(request):
    products = Product.objects.all().order_by('-date', 'title')  
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
    return render(request, 'workspace/index.html', {'products': products})



def create_products(request):
    if request.method == 'POST':
        category_id = int(request.POST.get('category'))
        tag_ids = list(map(int, request.POST.getlist('tags')))
        tags = Tag.objects.filter(id__in=tag_ids)
        image = request.FILES.get('image')
        data = {
            'title': request.POST.get('title'),
            'price': request.POST.get('price'),
            'content': request.POST.get('content'),
            'is_published': request.POST.get('is_published', False) == 'on',
            'category': Category.objects.get(id=category_id)
        }

        product = Product.objects.create(**data) 
        product.tags.add(*tags)
        if image: 
            product_image = ProductImage.objects.create(product=product, image=image)
            product_image.save()
     
        return redirect('/workspace/')

    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'workspace/create_products.html', {
        'categories': categories,
        'tags': tags,
    })


def update_product(request,id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        category_id = int(request.POST.get('category'))
        tag_ids = list(map(int, request.POST.getlist('tags')))
        tags = Tag.objects.filter(id__in=tag_ids)
        image = request.FILES.get('image')

        if image: 
            product_image = ProductImage.objects.create(product=product, image=image)
            product_image.save()

        product.tags.clear()
        product.tags.add(*tags)

        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.content = request.POST.get('content')
        product.is_published = request.POST.get('is_published', False) == 'on'
        product.category = Category.objects.get(id=category_id)
        product.save()

        return redirect('/workspace/')

    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'workspace/update_product.html', {
        'product': product,
        'categories': categories,
        'tags': tags,
    })



def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/workspace/')