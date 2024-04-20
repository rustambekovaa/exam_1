from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404


from moobile.models import Product, Category,ProductImage
from workspace.forms import ProductForm,Tag,UpdateForm


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



# def create_products(request):
#     if request.method == 'POST':
#         category_id = int(request.POST.get('category'))
#         tag_ids = list(map(int, request.POST.getlist('tags')))
#         tags = Tag.objects.filter(id__in=tag_ids)
#         images = request.FILES.getlist('image')
#         data = {
#             'title': request.POST.get('title'),
#             'price': request.POST.get('price'),
#             'content': request.POST.get('content'),
#             'is_published': request.POST.get('is_published', False) == 'on',
#             'category': Category.objects.get(id=category_id)
#         }

#         product = Product.objects.create(**data) 
#         product.tags.add(*tags)
#         if images:
#             for image in images:
#                 product_image = ProductImage.objects.create(product=product, image=image)
#                 product_image.save()
     
#         return redirect('/workspace/')

#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     return render(request, 'workspace/create_products.html', {
#         'categories': categories,
#         'tags': tags,
#     })


def create_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)    
        if form.is_valid():
            tags = form.cleaned_data['tags']
            image = form.cleaned_data['image']
            data = {
                'title': form.cleaned_data.get('title'),
                'price': form.cleaned_data.get('price'),
                'content': form.cleaned_data.get('content'),
                'is_published': form.cleaned_data.get('is_published'),
                'category': form.cleaned_data.get('category')
            }
            product = Product.objects.create(**data) 
            product.tags.add(*tags)
            if image:
                product_image = ProductImage.objects.create(product=product, image=image)
                product_image.save()
           
            return redirect('/workspace/')
    else:
        form = ProductForm()

    return render(request, 'workspace/create_products.html', {'form': form})




# def create_products(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():

#             product = form.save()

#             images = request.FILES.getlist('image')
#             for img in images:
#                 product_image = ProductImage(product=product, image=img)
#                 product_image.save()
            
#             return redirect('/workspace/')
#     else:
#         form = ProductForm()
    
#     return render(request, 'workspace/create_products.html', {'form': form})




# def update_product(request,id):
#     product = get_object_or_404(Product, id=id)

#     if request.method == 'POST':
#         category_id = int(request.POST.get('category'))
#         tag_ids = list(map(int, request.POST.getlist('tags')))
#         tags = Tag.objects.filter(id__in=tag_ids)
#         image = request.FILES.get('image')

#         if image: 
#             product_image = ProductImage.objects.create(product=product, image=image)
#             product_image.save()

#         product.tags.clear()
#         product.tags.add(*tags)

#         product.title = request.POST.get('title')
#         product.price = request.POST.get('price')
#         product.content = request.POST.get('content')
#         product.is_published = request.POST.get('is_published', False) == 'on'
#         product.category = Category.objects.get(id=category_id)
#         product.save()

#         return redirect('/workspace/')

#     tags = Tag.objects.all()
#     categories = Category.objects.all()
#     return render(request, 'workspace/update_product.html', {
#         'product': product,
#         'categories': categories,
#         'tags': tags,
#     })













def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    
    form = UpdateForm(initial={
        'title': product.title,
        'price': product.price,
        'is_published': product.is_published,
        'content': product.content,
        'category': product.category,
        'tags': product.tags.all(),
    })

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            product.title = form.cleaned_data['title']
            product.price = form.cleaned_data['price']
            product.is_published = form.cleaned_data['is_published']
            product.content = form.cleaned_data['content']
            product.category = form.cleaned_data['category']
            product.tags.set(form.cleaned_data['tags']) 
            product.save()

         
            image = form.cleaned_data['image']
            if image:
                product_image = ProductImage.objects.create(product=product, image=image)
                product_image.save()

            return redirect('/workspace/')

    return render(request, 'workspace/update_product.html', {'form': form, 'product': product})




def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/workspace/')

