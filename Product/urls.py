from django.urls import path
from Product.views import detail,detail2,allhot,packages
app_name = "product"
urlpatterns = [
    path('<str:string>',detail,name="detail"),
    path('<int:id>/',detail2,name="detail2"),
    path('packeages/',packages,name="packages"),
    path('hot/',allhot,name="hot"),
]
