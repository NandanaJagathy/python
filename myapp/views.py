from django.db.models.query_utils import RegisterLookupMixin

from django.shortcuts import render ,redirect
from .models import Card,Register
from django.contrib import messages

# Create your views here.



def home(request):
    if 'email' in request.session:
        user = Register.objects.get(email=request.session['email'])
        print(user.email)
        book_obj = Card.objects.all()  # Fetch all cards
        return render(request, 'home1.html', {'data': book_obj, 'obj': user})
    else:
        return redirect('/')


def add(request):
    if request.method == 'POST':
        print(request.POST)
        book_obj = Card()
        book_obj.book_name = request.POST.get('book_name')
        book_obj.author = request.POST.get('author')
        book_obj.price = request.POST.get('price')
        book_obj.image = request.FILES.get('image')
        book_obj.save()
        return redirect('/home')
    return render(request,'content.html')
def delete(request,id):
    obj=Card.objects.get(id=id)
    obj.delete()
    return redirect('/home/')

def update(request,id):
    obj= Card.objects.get(id=id)
    if request.method =='POST':
        print(request.POST)
        book_obj = Card.objects.get(id=id)
        book_obj.book_name = request.POST.get('book_name')
        book_obj.author = request.POST.get('author')
        book_obj.price = request.POST.get('price')
        book_obj.save()
        return redirect('/')
    return render(request, 'update.html',{'data':obj})

def view(request,id):
    obj = Card.objects.get(id=id)
    return render(request, 'view.html',{'data':obj})

def register(request):
    if request.method=='POST':
        obj = Register()
        obj.email = request.POST.get('email')
        obj.password= request.POST.get('psw')
        obj.image = request.FILES.get('image')
        obj.save()

        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')
        user = Register.objects.filter(email=email,password=password)
        if user:
           request.session['email']= email
           messages.success(request,'you have succesfully logged in')
           return redirect('/home/')
    return render(request, 'login.html')
def logout(request):
    if 'email' in request.session:
      del request.session['email']
      return redirect('/')
