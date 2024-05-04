from django.contrib import messages

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from moobile.models import Product, Category
from .forms import ProductForm,LoginForm,RegisterForm,ChangeProfileForm,ChangePasswordForm
from workspace.decorators import login_required,own_news
from moobile.filters import ProductFilter
from django.contrib.auth.hashers import make_password

@login_required(login_url='/auth/login/')
def workspace(request):
    products = Product.objects.all().order_by('-date', 'title')
    if request.user.is_authenticated:
        products = Product.objects.filter(author=request.user) 
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
    return render(request, 'workspace/index.html', {'context':context,'products': products,'filter':filter_set})



@login_required()
def create_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            messages.success(request, f'Товар "{product.title}" успешно создан!')
            return redirect('/workspace/')
        messages.error(request, f'Исправьте ошибки ниже')
    else:
        form = ProductForm()
    
    return render(request, 'workspace/create_products.html', {'form': form})




@login_required()
@own_news
def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.image = form.cleaned_data['image']
            product.save()
            print( product.image)
            messages.success(request, f'Товар "{product.title}"успешно обновлено!')

            return redirect('/workspace/')
        messages.error(request, f'Исправьте ошибки ниже')
        
    else:
        form = ProductForm(instance=product)

    return render(request, 'workspace/update_product.html', {
        'product': product,  
        'form': form
    })


@login_required()
@own_news
def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, f'Товар "{product.title}" успешно удалено')

    return redirect('/workspace/')




def login_profile(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    form = LoginForm()
    message = None

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username,password = password)

            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать в рабочее пространство "{user.first_name} {user.last_name}"')
                return redirect('/workspace/')

            message = 'Пользователь не существует или пароль неверен.'


    return render(request, 'auth/login.html', {'form': form, 'message': message})



def logout_profile(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect('/')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать в рабочее пространство "{user.first_name} {user.last_name}"')
            return redirect('/workspace/')

    return render(request, 'auth/register.html', {'form': form})



@login_required()
def change_profile(request):
    form = ChangeProfileForm(instance=request.user)

    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш профиль успешно изменен!')
            return redirect('/workspace/')

    return render(request, 'auth/change_profile.html', {'form': form})



@login_required()
def change_password(request):

    form = ChangePasswordForm()

    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user = request.user
            # user.password = make_password(new_password)
            user.set_password(new_password)
            user.save()

            login(request, user)

            messages.success(request, f'Your password has been changed!')
            return redirect('/workspace/')

    return render(request, 'auth/change_password.html', {'form': form})