from django.shortcuts import render,redirect
from category.models import Category,Languages
from home.models import informationSite
from django.contrib.auth.decorators import login_required
from Product.models import teachers,Product
from account.models import sabad
# Create your views here.
@login_required
def bought(request,id):
    product = Product.objects.get(id=id)
    sabad.objects.get_or_create(user=request.user,product=product)
    return redirect('/sabad')

@login_required
def Sabad(request):
    siteData = informationSite.objects.first()
    language = Languages.objects.all()
    category = Category.objects.all()
    pr = sabad.objects.filter(user__username=request.user.username)
    teacher = teachers.objects.all()
    return render(request,"buy/manage-course.html",{
    "category":category,
    "lang":language,
    "siteData":siteData,
    "product":pr,
    "teacher":teacher,
    })
@login_required
def delete(request,id):
    sabad.objects.get(product__id=id,user=request.user).delete()
    return redirect('/sabad')