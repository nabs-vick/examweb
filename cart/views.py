from django.shortcuts import render, get_object_or_404
from .cart import Cart
from examapp.models import Service
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.


def cart_summary(request):
    # get the cart 
    cart = Cart(request)
    
    cart_services = cart.get_service
    quantities = cart.get_quants
    
    return render(request,'cart/cart.html',{'cart_services':cart_services, "quantities":quantities})

def cart_add(request):
    # get cart
    cart = Cart(request)
    
    # test post
    if request.POST.get('action') == 'post':
        service_id = int(request.POST.get('service_id'))
        service_qty = int(request.POST.get('service_qty'))
        
        
        # lookup product in db
        service = get_object_or_404(Service, id=service_id)
        
        # save to a session
        cart.add(service=service, quantity=service_qty)
        
        # get quantity
        cart_quantity = cart.__len__()
        # return response 
        # response = JsonResponse({ 'Service Name: ': service.name })
        response = JsonResponse({ 'qty': cart_quantity })
        return response
        

def cart_delete(request):
    pass

def cart_update(request):
    pass

# @user_passes_test(lambda user: user.is_superuser)
# # here will be the code for the admin to check orders made from the different users