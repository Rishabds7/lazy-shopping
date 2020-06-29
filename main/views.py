import os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from main.models import Products , selling




def product():

    p1 = Products()
    p1.name = 'Tank Top'
    p1.img = 'cloth_1.jpg'
    p1.desc = 'Super Dry'
    p1.price = 5000

    p2 = Products()
    p2.name = 'Corater'
    p2.img = 'shoe_1.jpg'
    p2.desc = ' Dry'
    p2.price = 4000

    p3 = Products()
    p3.name = 'Polo Shirt'
    p3.img = 'cloth_2.jpg'
    p3.desc = ' Finding perfect products'
    p3.price = 3000

    p4 = Products()
    p4.name = 'T-Shirt Mockup'
    p4.img = 'cloth_3.jpg'
    p4.desc = ' Finding perfect products'
    p4.price = 2000

    prods = [p1, p2, p3, p4]

    return prods

def Main(request):

    prods = product()

    return render(request ,'index.html', {'prods' : prods})

def collection(request):

    return render(request, 'products.html')

def sell(request):

    if request.method == 'POST':
        pname = request.POST['pname']
        price = request.POST['price']
        #des = request.POST['des']
        print(pname, price )


        try:
                folder = 'media/images/'
                uploaded_image = request.FILES['prod']
                print("Name is:", uploaded_image.name)

                # if not uploaded_image:
                # return Response({"error": "Choose file"}, status=status.HTTP_400_BAD_REQUEST)
                # for f in myfiles:
                filename = str(uploaded_image.name)
                fs = FileSystemStorage(location=folder)  # defaults to DATASTORE
                name = fs.save(uploaded_image.name, uploaded_image)
                mediapath = folder + "{}"
                filepath = os.path.join(mediapath).format(name)
                print(filepath)

                product = selling()
                product.price = price
                product.product_name = pname
                product.product_image = filepath
                product.save()


        except Exception as e :
                print("Error is :",e)

        return HttpResponseRedirect(reverse('main'))

    else:

        return render(request, 'sell.html')