from django.shortcuts import render, redirect
from warehouseapp.models import Item

def home(request):
    if request.method == 'GET':
        products = Item.objects.all()
        return render(request, 'index.html')
    
def base(request):
    return render(request, "base.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def search(request):
    return render(request, "search.html")

def cart(request):
    return render(request, "cart.html")

def add_products(request):
    if request.method == 'GET':
        return render(request, 'add_products.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        state = request.POST.get('state')
        quantity = request.POST.get('quantity')
        warehouse = request.POST.get('warehouse')
    

        Item.objects.create(
            name=name, 
            description=description, 
            price=price, 
            state=state, 
            quantity=quantity,
            warehouse_id=warehouse
        )
        return redirect ('index')

def edit_products(request):
    if request.method == 'GET':
        return render(request, 'add_products.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        state = request.POST.get('state')
        quantity = request.POST.get('quantity')
        warehouse = request.POST.get('warehouse')
    

        Item.objects.update(
            name=name, 
            description=description, 
            price=price, 
            state=state, 
            quantity=quantity,
            warehouse_id=warehouse
        )
        return render(request, "edit_products.html")
    

def search_all(request):
    if request.method == 'GET':
        products = Item.objects.all()
        return render(request, "allproducts.html", {"product": products})

