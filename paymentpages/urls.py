from django.urls import include, path

from . import views

app_name = "paymentpages"

urlpatterns = [
    path('', views.initialize_payments, name="initialize_payment"),
    path('<str:reference>/', views.payments_verify, name="payments-verify"),
    
    path('pagelist/', views.page_list, name="pagelist"),
    path('page/<int:id>/', views.page, name='page'),
    path('updatepage/<int:id>/', views.updatepage, name='updatepage'),
    path('slugavailability/<str:slug>/', views.slug_availability, name='slug_availability'),
    path('addproduct/', views.add_product, name='add_product')
]