from django.urls import path
from . import views

urlpatterns = [
    path('addGroup/',views.AddGroup.as_view(),name='addGroup'),
    path('<int:pk>/addItem/',views.AddItem.as_view(),name='addItem'),
    path('<int:pk>/addFoundAddress/',views.AddFoundAddress.as_view(),name='addFoundAddress'),
    path('<int:pk>/addFoundLocation/',views.AddFoundLocation.as_view(),name='addFoundLocation'),
    path('<int:pk>/addressOrLocation/',views.AddressOrLocation.as_view(),name='addressOrLocation'),
    path('<int:pk>/detail/',views.Detail.as_view(),name='detail'),
    path('<int:pk>/manage/',views.Manage.as_view(),name='manage'),
    path('<int:pk>/addOwner/',views.AddOwner.as_view(),name='addOwner'),
    path('<int:pk>/addImage/',views.AddImage.as_view(),name='addImage'),
    path('<int:pk>/itemDetail',views.ItemDetail.as_view(),name='itemDetail'),
    path('addRandom/',views.AddRandom.as_view(),name='addRandom'),
    path('',views.Index.as_view(),name='index'),
]
