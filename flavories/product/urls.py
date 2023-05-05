from django.urls import path
from.import views
urlpatterns = [
    path('',views.product),
    path('cmt/',views.comment),
    path('like/',views.like)
]
   