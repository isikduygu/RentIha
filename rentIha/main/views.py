from django.shortcuts import render, redirect,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsAdminUserOrReadOnly
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Iha, Rent
from .serializers import IhaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import IhaForm, RentIhaForm
from rest_framework.response import Response


@login_required(login_url="/login") #eger login olmadıysa kullanıcıyı logine yönlendirir. login olmadan home sayfasına gidemez
def home(request):
    return render(request, 'main/home.html') #home.html template'ini render ediyor.

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) # eger post request ise formun içini o data ile doldur.
        if form.is_valid():
            user = form.save() #eger form valid ise kullanıcı kaydını kaydedip database gönderir
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm() # değilse boş form oluştur

    return render(request, 'registration/sign_up.html', {"form" : form})

# get isteği atarak tüm ihaları listeler ayrıca search işlemi bu kısımda yapılmıştır.
@api_view(['GET'])
def iha_list(request):
    search_query = request.GET.get('search') # urlden datayı alır
    category_filter = request.GET.get('category')
    iha = Iha.objects.all()
    if search_query:
        iha = iha.filter(brand__icontains=search_query)
    if category_filter:
        iha = iha.filter(category=category_filter)
    serializer = IhaSerializer(iha, many=True)

    return render(request, 'main/iha_list.html', {'iha_list': serializer.data})

# iha kaydı oluşturur sadece superadmin yapabilir
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUserOrReadOnly])  # Sadece süper kullanıcılar veya okuma/oluşturma izni
def iha_create(request):
    if request.method == 'POST':
        form = IhaForm(request.POST)
        if form.is_valid():
            iha = form.save()
            serializer = IhaSerializer(iha)
            return redirect('iha_list')  # veya istediğiniz bir URL'ye yönlendirme yapabilirsiniz
    else:
        form = IhaForm()
    
    return render(request, 'main/iha_create.html', {'form': form})

# iha ile ilgili işlemler burada yapılır id ile iha detayları görülür, silme ve düzenleme işlemleri yapılmıştır.
@permission_classes([IsAdminUserOrReadOnly])
@api_view(['GET', 'POST', 'DELETE','PUT'])
def iha_detail(request, id, format=None):
    try:
        iha = Iha.objects.get(pk=id)
    except Iha.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = IhaSerializer(iha)
        return render(request, 'main/iha_detail.html', {'iha': iha, 'serializer': serializer})
    
    elif request.method == 'PUT':
        serializer = IhaSerializer(iha, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        iha.delete()

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# kiralama işlemi gerçekleşir.
def rent_create(request):
    form = RentIhaForm()
    if request.method == 'POST':
        form = RentIhaForm(request.POST)
        if form.is_valid():
            # Form geçerliyse;
            user_id = request.user.id
            # Formu kaydetmeden önce kullanıcı kimlik bilgisini set eder. Hangi kullanıcı login ise onu alır.
            form.instance.user_id = user_id
            form.save()

    return render(request, 'main/rent_iha.html', {'form': form})

# kiralama detayları görülür. burada user sadece kendi kiraladığı ihaları görür.
def rent_detail(request):
    user_id = request.user.id
    rents = Rent.objects.filter(user_id=user_id)
    return render(request, 'main/my_iha.html', {'rents': rents})

# kiralama siler bu arayüze konulmadı
def rent_delete(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)
    if request.method == 'DELETE':
        rent.delete()
        return redirect('rent-list')
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# bütün kiralamaları görür. normalde sadece superuserın erişimi olması lazım. ama ayarlanmadı.
def rent_iha_list(request):
    rents = Rent.objects.all()
    return render(request, 'main/rent_iha_list.html', {'rents': rents})


