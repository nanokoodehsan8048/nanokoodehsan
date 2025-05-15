from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.core.mail import send_mail  # برای ارسال پیام تماس با ما اگر خواستی

# صفحه اصلی
def index(request):
    return render(request, 'home/index.html')

# صفحه همه محصولات
def products(request):
    products = Product.objects.all()
    return render(request, 'home/products.html', {'products': products})

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_humic(request):
    product = get_object_or_404(Product, category='humic')
    return render(request, 'home/product_detail.html', {'product': product})

def product_apartment(request):
    product = get_object_or_404(Product, category='apartment')
    return render(request, 'home/product_detail.html', {'product': product})

# صفحه نظرات مشتریان
def comments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        phone = request.POST.get('phone')
        # می‌تونی نظر رو در دیتابیس ذخیره کنی یا برا مدیر ایمیل بزنی
        return render(request, 'home/comments.html', {'success': True})
    return render(request, 'home/comments.html')

# صفحه تماس با ما
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # send_mail یا ذخیره در DB می‌تونی بزاری اینجا
        return render(request, 'home/contact.html', {'sent': True})
    return render(request, 'home/contact.html')

# صفحه سبد خرید
def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    total_price = sum(product.price * cart[str(product.id)] for product in products)
    return render(request, 'home/cart.html', {
        'products': products,
        'cart': cart,
        'total_price': total_price
    })

# حذف محصول از سبد خرید
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')

# صفحه پرداخت
def payment_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')
    products = Product.objects.filter(id__in=cart.keys())
    total_price = sum(product.price * cart[str(product.id)] for product in products)
    
    if request.method == 'POST':
        # اینجا می‌تونی سفارش رو ذخیره کنی یا اتصال به درگاه بزاری
        request.session['cart'] = {}  # پاک کردن سبد خرید
        return redirect('success')

    return render(request, 'home/payment.html', {
        'products': products,
        'total_price': total_price
    })

# موفقیت پرداخت
def payment_success(request):
    return render(request, 'home/success.html')
