from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # صفحات سبد خرید و پرداخت
    path('cart/', views.cart_view, name='cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment/', views.payment_view, name='payment'),
    path('success/', views.payment_success, name='success'),

    # صفحه اصلی
    path('', views.index, name='index'),

    # صفحه محصولات
    path('products/', views.products, name='products'),

    # صفحات محصولات خاص
   path('products/product1/', views.product_humic, name='product_humic'),
path('products/product2/', views.product_apartment, name='product_apartment'),

    # نظرات و ارتباط با ما
    path('comments/', views.comments, name='comments'),
    path('contact/', views.contact, name='contact'),
]

# اضافه کردن media و static فقط در حالت توسعه (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
