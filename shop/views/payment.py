from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from shop.models import User, Product


#id: rzp_test_kKk5Q3ZiV0TNcq
#secret: RNTiugpyqblS8cRHxeULFJzw
def createPayment(request, product_id):
    if request.method == "POST":
        name = request.POST.get('name')
        product = Product.objects.get(id=product_id)

        name = product.name
        price = product.price + (product.price * product.discount)
        amount = 5000

        client = razorpay.Client(
            auth=("rzp_test_kKk5Q3ZiV0TNcq", "RNTiugpyqblS8cRHxeULFJzw"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})

    return render(request, 'payment.html')


@csrf_exempt
def success(request):
    return render(request, "success.html")

















