from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product

# Create your views here.

def index(req):
    products = Product.objects.all()
    return render(req, "index.html", {"products": products})

@require_POST
def create(req):
    if req.method == "POST":
        product = Product(
            title=req.POST.get("title"),  # 使用 get() 來安全地獲取 POST 資料
            price=req.POST.get("price"),
            description=req.POST.get("description"),
        )
        product.save()
       
    return  redirect("products:index")

def read(req, id):
    product = get_object_or_404(Product, pk=id)
    return render(req, "read.html", {"product": product})


def update(req, id):
    product = get_object_or_404(Product, pk=id)  # 使用 get_object_or_404 來取得單一物件
    if req.method == "POST":
        product.title = req.POST.get("title")
        product.price = req.POST.get("price")
        product.description = req.POST.get("description")
        product.save()
        return redirect("products:read", id=product.id)
    return render(req, "update.html", {"product": product})

@require_POST
def delete(req, id):
    product = get_object_or_404(Product, pk=id)  # 使用 get_object_or_404 來取得單一物件
    product.delete()
    return redirect("products:index")
