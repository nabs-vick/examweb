from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, ServiceForm
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Service, Category, Customer,Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    services = Service.objects.all()
    return render (request,'index.html',{'services':services})

@user_passes_test(lambda user: user.is_superuser)
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('examapp:index')
    else:
        form = ServiceForm()
    return render(request, 'add_product.html', {'form': form})


@user_passes_test(lambda user: user.is_superuser)
# Remove a product
def remove_product(request, product_id):
    product = get_object_or_404(Service, id=product_id)
    product.delete()
    return redirect('service_list')


@user_passes_test(lambda user: user.is_superuser)
# Update a product picture
def update_product_picture(request, product_id):
    product = get_object_or_404(Service, id=product_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def about(request):
    return render(request,'about.html')



# def shop(request):
#     services = Service.objects.all()
    



def index(request):
    return render(request,'book.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('welcome back'))
            return redirect('examapp:home')
        else:
            messages.success(request,('something went wrong'))
            return redirect('examapp:login')
    else:
        return render(request,"auth/login.html")
    


def logout_view(request):
    logout(request)
    messages.success(request, ('you have logged out successfully'))
    return redirect('examapp:home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('welcome to nursing exams experts'))
            return redirect('examapp:home')
        else:
            messages.error(request, ('error in account creation'))
            return render(request,'auth/register.html')
    else:
        return render(request,'auth/register.html',{'form':form})
    

def service(request, pk):
    service = Service.objects.get(id=pk)
    return render(request,'service.html',{'service':service})


def shop(request, foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name=foo)
        services = Service.objects.filter(category=category)
        return render(request,'shop.html',{'services':services , 'category':category})
    except:
        messages.success(request,"the category does not exist")
        return redirect('examapp:home')
    
    


@user_passes_test(lambda user: user.is_superuser)
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('examapp:home')
    else:
        form = ServiceForm()
    return render(request, 'crud_for_services/add_services.html', {'form': form})





@user_passes_test(lambda user: user.is_superuser)
# Remove a service
def remove_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('examapp:home')



@user_passes_test(lambda user: user.is_superuser)
# Update a services
def update_service(request, service_id):
    product = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=Service)
        if form.is_valid():
            form.save()
            return redirect('examapp:home')
    else:
        form = ServiceForm(instance=Service)
    return render(request, 'crud_for_services/update_services.html', {'form': form})