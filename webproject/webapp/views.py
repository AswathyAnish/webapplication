from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductsForm


# Create your views here.
def index(request):
    product = Products.objects.all()
    context = {
        'product_list': product
    }
    return render(request, 'index.html', context)


def detail(request, product_id):
    product=Products.objects.get(id=product_id)
    return render(request,'detail.html',{'products':product})

def addtodb(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        year = request.POST['year']
        img = request.FILES['img']
        product=Products(name=name,desc=desc,year=year,img=img)
        product.save()

    return render(request, 'addDB.html')
def update(request,id):
    product=Products.objects.get(id=id)
    form=ProductsForm(request.POST or None,request.FILES,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'product':product})
def delete(request,id):
    if request.method == 'POST':
        product=Products.objects.get(id=id)
        product.delete()
        return redirect('/')
    return render(request, 'delete.html')


