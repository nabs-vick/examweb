from examapp.models import Service

class Cart():
    def __init__(self,request):
        self.session = request.session
        #det session key if it exists
        cart = self.session.get('session_key')
        
        #if user is new
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        #make sure cart is available on all pages of our site
        self.cart = cart
    
    def add(self, service, quantity):
        service_id = str(service.id)
        service_qty = str(quantity)
        
        # logic
        if service_id in self.cart:
            pass
        else:
            # self.cart[service_id] = {'price':str(service.price)}
            self.cart[service_id] = int(service_qty)
        self.session.modified =True
        
        
    def __len__(self):
        return len(self.cart)
    
    def get_service(self):
        # det ids from cart
        service_ids = self.cart.keys()
        # use id to lookup 
        services = Service.objects.filter(id__in=service_ids)
        return services
    
    
    def get_quants(self):
        quantities = self.cart
        return quantities
