from django.shortcuts import render,get_object_or_404,redirect
from Product.forms import CommentForms
from Product.models import Product,Comment
from category.models import Category,Languages
from home.models import informationSite
from django.http import HttpResponse
def detail(request,string):
    Prod = get_object_or_404(Product,slug=string)
    rec = Product.objects.filter(language=Prod.language.first())
    languagess = Languages.objects.all()
    category = Category.objects.all()
    siteData = informationSite.objects.first()
    comment = Comment.objects.filter(product__slug=string)
    
    if request.method == "POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            ex = Comment()
            ex.text = form.cleaned_data.get('text')
            ex.user = request.user
            ex.product = Product.objects.get(slug=string)
            ex.save()
            return redirect(f"/{string}")
    else:
        form = CommentForms()

    context ={
        "string":Prod,
        "form":form,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "co":comment,
        "rec":rec,
    }
    return render(request,"detail/course-detail.html",context)
def detail2(request,id):
    Prod = get_object_or_404(Product,id=id)
    rec = Product.objects.filter(language=Prod.language.first())
  
    if request.method == "POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            ex = Comment()
            ex.text = form.cleaned_data.get('text')
            ex.user = request.user
            ex.product = Product.objects.get(id=id)
            ex.save()
            return redirect(f"/{id}")
    else:
        form = CommentForms()

    languagess = Languages.objects.all()
    category = Category.objects.all()
    comment = Comment.objects.filter(product__id=id)
    siteData = informationSite.objects.first()
    context ={
        "string":Prod,
        'form':form,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "co":comment,
        "rec":rec,

    }
    return render(request,"detail/course-detail.html",context)
def allhot(request):
    return HttpResponse("hot tutorials")
def packages(request):
    return HttpResponse("packages")

def like(request,id):
    comid = Comment.objects.get(id=id)
    for a in comid.like.all():
        if a == request.user:
            comid.like.remove(request.user)
            break
    else:
        comid.like.add(request.user)
            
    
    
    return redirect('/yacn')
def dislike(request,id):
    comid = Comment.objects.get(id=id)
    for a in comid.dislike.all():
        if a == request.user:
            comid.dislike.remove(request.user)
            break
    else:
        comid.dislike.add(request.user)
    
    
    
    return redirect('/yacn')