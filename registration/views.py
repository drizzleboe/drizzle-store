from audioop import reverse
import datetime
from email import message
import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from hamcrest import instance_of
from sqlalchemy import desc
from .models import address, profession,contact as db_contact,product as db_user,staff,order,comment,user as subscriber,subscriber as email_subscriber,faq as faqs, about as abouts, top_image as top
from .form import sign_in,registerForm, other_details, profession_form, contact_form, otherproduct,order_form, comments,subscriberForm,cartForm,contact_us_form
from .filters import productFilter
from django.contrib import messages
from django import forms
import smtplib
from django.core.mail import send_mail

# Create your views here.
now = datetime.datetime.now()
def index(request):
    _top = top.objects.all()
    _user =  db_user.objects.all()
    otherdetails = other_details()
    
    _staff = staff.objects.all()
    _address =   address.objects.all()
    _contact = db_contact.objects.all()
    #check = db_user.objects.filter(prfssn = None)
    _otherproduct =  otherproduct()
    _comments = comments()
    _subscriberForm = subscriberForm()
    
    
    
    #if check:
    #    for i in check:
    #        db_username = i.username
    #        rcheck = User.objects.filter(username = db_username)
    #        rcheck.delete()
    #        check.delete()

    prdctFilter = productFilter(request.GET, queryset=_user)
    if 'searchbutton' in request.GET:
        prdctFilter = productFilter(request.GET, queryset=_user)
        _user = prdctFilter.qs
    if request.method == 'POST':
        if 'otherBut' in request.POST:
            otherdetails = other_details(request.POST  or None)
            if otherdetails.is_valid():
                foo = otherdetails.cleaned_data.get('addres')
                selected_users = db_user.objects.filter(addres = foo)
                #print(selected_users)
                return render(request, 'registration/index.html',{
                'filtered':True,
                'selected_users':selected_users,
                'form':otherdetails,

                })
            ## taking the otherproducts form input values
            _otherproduct = otherproduct(request.POST or None)
            if _otherproduct.is_valid():
                _title = _otherproduct.cleaned_data.get('title')
                _desc = _otherproduct.cleaned_data.get('desc')
                _phone = _otherproduct.cleaned_data.get('phone')
                _email = _otherproduct.cleaned_data.get('email')
                db = order.objects.create(
                    s_title = _title,
                    desc = _desc,
                    phone = _phone,
                    email = _email
                )

                #if db:
                 #   s = smtplib.SMTP('smtp.gmail.com', 58)
                  #  s.starttls()
                   # s.login("drizzle.services","StoreThis2017**")
                    #message = 'Order have placed: ' + _title+ " "+_desc + " " + _phone + " "+ _email 
                    #s.sendmail("drizzle.services@gmail.com","drizle.services@gmail.com", message)
                    #s.quite()
                messages.success(request,f'Ahsante! order yako imepokelewa, drizzle store tutawasiliana na wewe kupitia email {_email} au namba yako {_phone} ')
                return redirect('success')

        elif 'commentBut' in request.POST:
            _comments = comments(request.POST)
            if _comments.is_valid():
                _text = _comments.cleaned_data.get("comment")
                db = comment.objects.create(
                    text = _text
                )
                messages.success(request,f'Ahsante! umefanikiwa kutuma maoni yako, drizzle store tumepokea na tunaahidi kuyafanyia kazi.')
                return redirect('success')

        elif 'subBut' in request.POST:
            _subscriberForm = subscriberForm(request.POST or None)
            if _subscriberForm.is_valid():
                email = _subscriberForm.cleaned_data.get('email')
                email_subscriber.objects.create(
                    emails = email
                )
                messages.success(request,'Asante kwa ku-subscribe tovuti yetu!, utakuwa wakwanza kupata taarifa zote, ofa na coupon za punguzo la bei kutoka drizzle store. ')
                return redirect('success')

        else:
            ButtonInjection = True 

    return render(request, 'registration/index.html',{
        'normal':True,
        'prdctFilter':prdctFilter,
        'user': _user,
        'staff': _staff,
        'address': _address,
        'contact':_contact,
        'form':otherdetails,
        'otherproduct': _otherproduct,
        'comments': _comments,
        'year': now.year,
        'subscriberForm':_subscriberForm,
        'images': _top,
        
        })
def details(request, slug_field):
    if 'cartbutton' in request.GET:
        p_slug = request.GET.get('cartproduct')
    if 'buybutton' in request.GET:
        title = request.GET.get('title') 
        desc = request.GET.get('desc')
        username = request.GET.get('username')
        phone = request.GET.get('phone')
        email = request.GET.get('email')
        db_order = order.objects.create(
            s_title = title,
            desc = desc,
            usernames = username,
            phone = phone,
            email = email,
        )
        if db_order:
            messages.success(request,f'Ahsante! order yako imepokelewa, drizzle store tutawasiliana na wewe kupitia email {email} au namba yako {phone} ')
            return redirect('success')
    detail = db_user.objects.get(slug = slug_field)
    signed_in = False
    if 'user_id' in request.session:
        signed_in = subscriber.objects.get(id = request.session['user_id'])

    if detail.image1:
        _image1 = detail.image1
    else:
        _image1 = False
    if detail.image2:
        _image2 = detail.image2
    else:
        _image2 = False
    if detail.image3:
        _image3 = detail.image3
    else:
        _image3 = False
    if detail.image4:
        _image4 = detail.image4
    else:
        _image4 = False
    if detail.image5:
        _image5 = detail.image5
    else:
        _image5 = False
    if detail.image6:
        _image6 = detail.image6
    else:
        _image6 = False
    if detail.image7:
        _image7 = detail.image7
    else:
        _image7 = False
    if detail.image8:
        _image8 = detail.image8
    else:
        _image8 = False
    if detail.image9:
        _image9 = detail.image9
    else:
        _image9 = False
    if detail.image10:
        _image10 = detail.image10
    else:
        _image10 = False
    if detail.image11:
        _image11 = detail.image11
    else:
        _image11 = False
    if detail.image12:
        _image12 = detail.image12
    else:
        _image12 = False
    request.session['detail']=detail.id
    return render(request, 'registration/details.html',{
    'available':True,
    'user':detail,
    'signed_in':signed_in,
    'image1': _image1,
    'image2': _image2,
    'image3': _image3,
    'image4': _image4,
    'image5': _image5,
    'image6': _image6,
    'image7': _image7,
    'image8': _image8,
    'image9': _image9,
    'image10': _image10,
    'image11': _image11,
    'image12': _image12,
    'year': now.year,     
    })
   
def subs(request):
    _subscriberForm = subscriberForm()
    if request.method == 'POST':
        _subscriberForm = subscriberForm(request.POST or None)
        if _subscriberForm.is_valid():
            email = _subscriberForm.cleaned_data.get('email')
            email_subscriber.objects.create(
                emails = email
            )
            messages.success(request,'Asante kwa ku-subscribe tovuti yetu! ')
            return redirect('success')
    return render(request, 'registration/subscribe.html',{
        'subscriberForm':_subscriberForm,
        'year': now.year,
    })

def success(request):
    return render(request, 'registration/success.html', {
        'year': now.year,
    })

def products(request):
    _user =  db_user.objects.all()
    prdctFilter = productFilter(request.GET, queryset=_user)
    _user = prdctFilter.qs
    print('The prodcut is ',_user)
    return render(request, 'registration/products.html',{
                'products': _user,
        'prdctFilter':prdctFilter,
        'year': now.year,
    })

def register(request):
    form = registerForm()
    if request.method == 'POST':
        request.session['alive']= 'submitting'
        form = registerForm(request.POST or None)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('passwd')
            _user = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname, 
                    username=email,
                    password=password
                )
            
            visible_user = subscriber.objects.create(
               first_name=firstname,
               last_name=lastname,
               email=email,
               password = password
               )
            logout(request)
            messages.success(request, '''Hongera akaunti yako imetengenezwa, 
            tumia email yako na password ulizotumia kujisajili ili kuingia!''')
            return redirect('login') #/Means login page
            
           #password2 = form.cleaned_data.get('password2')                
            #try:
                
                #return redirect('login') #/Means home page
               # redirected = 1
   
    #            
    #            request.session['user_id']=_user_id
    #                                               
            #except:
            #    user = None
            #if _user != None:
            #login(user)
                
            #else:
            #request.session('registration_error') = 1
                #redirected = 0                    
    return render(request, 'registration/register.html',{
        #'username_exist':username_exists,
        #'passwordnotmatch':passwordnotmatch,
        'form':form,
        'year': now.year,    
    })
def signup(request):
    otherdetails = other_details()
    contactForm = contact_form()
    professionForm = profession_form()
    if request.method == 'POST':
        otherdetails = other_details(request.POST, request.FILES)
        contactForm = contact_form(request.POST)
        thesession = request.session.get('alive')
        
        if thesession:
            if otherdetails.is_valid():
                address = otherdetails.cleaned_data.get('addres')
                profession= otherdetails.cleaned_data.get('prfssn')
                description = otherdetails.cleaned_data.get('description')
                gender = otherdetails.cleaned_data.get('gend')
                _image = otherdetails.cleaned_data.get('image')
                contact = contactForm.save()

                try:
                    user_id = request.session.get('user_id')
                    current_user        = db_user.objects.get(id = user_id)
                    current_user.addres = address 
                    current_user.prfssn = profession
                    current_user.cont   = contact
                    current_user.image  = _image
                    current_user.description = description
                    current_user.gend = gender
                    current_user.save()

                    del request.session['user_id']
                    del request.session['alive']
                    return redirect('login')
                except:
                    print('the contact field is ',contact)
                else:
                    print('The fields are not valid')
        else:
            messages.warning(request, 'Fill these field first')
            return redirect('register')        
    return render(request, 'registration/signups.html',{
        'otherDetails':otherdetails,
        'contactform':contactForm,
        'professionform':professionForm,
        'year': now.year,
    })
@login_required(login_url='login')
def myaccount(request,user_id):
    #user_id = request.session.get('this_id')
    current_user = subscriber.objects.get(id = user_id)
    request.session['email'] = current_user.email
    user_orders = order.objects.filter(email = current_user.email).count()
    #otherdetails = other_details(request.POST or None, instance=current_user)
    contactForm = contact_form()
    professionForm = profession_form()
    _cartForm = cartForm()
    if current_user.id != request.session['user_id']:
        return redirect('login')
     #   return redirect('login')
    #if otherdetails.is_valid():
    #    otherdetails.save()
    #if request.user.is_authenticated:    
        
            #del request.session['this_id']
    return render(request, 'registration/myaccount.html',{
        'userfound':True,
        'user':current_user,
        'cartform':_cartForm,
        'user_orders':user_orders,
        #'otherdetails':otherdetails,
        #'contactForm':contactForm,
        #'professionForm':professionForm,
        'year': now.year,
    })

        #except:
        #    return render(request, 'registration/myaccount.html',{
        #        'userfound':False,
        #    })
@login_required(login_url='login')
def settings(request):
    _user_id = request.session.get('user_id')
    the_user = subscriber.objects.filter(id = _user_id)
    _form = registerForm()
    
    
    #otherdetails = other_details(instance=the_user)
    #if request.method == 'POST' or None:
        
    
    #    otherdetails = other_details(request.POST, request.FILES, instance=the_user)
    #    if otherdetails.is_valid():
    #        otherdetails.save()
    #        del request.session['user_username']
    #        messages.success(request,'saved')
    #        return redirect(f'myaccount/{the_user.id}')
    
    return render(request, 'registration/settings.html',{
        'form':_form,
        'year': now.year,
    })

def userlist(request):
    user_  = user.objects.all()
    addre = region.objects.all()
    return render(request, 'registration/userlist.html',{
        'users':user_,
        'addre':addre,
        'year': now.year,
    })
    
def login_view(request):
    User = subscriber.objects.all()
    signin_form = sign_in(request.POST or None)
    if 'user_id' in request.session:
        signed_in = subscriber.objects.get(id = request.session['user_id'])
        if signed_in:
            return redirect(f'myaccount/{signed_in.id}')
    if signin_form.is_valid():
        email = signin_form.cleaned_data.get('username')
        password = signin_form.cleaned_data.get('passwd')

        authenticated = authenticate(request, username = email, password = password)           
        if authenticated:
            login(request, authenticated)
            _this_user = subscriber.objects.get(email = email)
            request.session['user_id'] = _this_user.id
            return redirect(f'myaccount/{_this_user.id}')
           
        else:
            #raise forms.ValidationError('password uliyoingiza sio sahihi') 
            print('not authenticated') 
        #else:     
        
        #print(authenticated)
        
        #    #raise forms.ValidationError('invalid username or password') 
        #    Failed = 1  
        #    request.session['attempts'] = 1 
        #    return render(request, 'registration/login.html',{
        #    'signin_form':signin_form,
        #    'failed': Failed,   
        #    })           
    return render(request, 'registration/login.html',{
        'signin_form':signin_form,
        'year': now.year,  
    })
def logout_view(request):
    logout(request)
    messages.warning(request,'Umefanikiwa kutoka nje ya akaunti yako!')
    return redirect('login')
 
def wellcome(request):
    user_  =  User.objects.get_username();
    return render(request, 'registration/wellcome.html',{

    "user":user_,
    'year': now.year,
    })





def cookie_session(request):
    request.session['name']= 'ismail'
    return HttpResponse("<h1>creating a session</h1>")
def cookie_delete(request):
    if request.session.get('name'):
        yourname = request.session.get('name')
        response = HttpResponse("dataflair<br> cookie was created and deleted",yourname)
        print(yourname)
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response

def placed_order(request):
    _order_form = order_form()
    service_slug = request.GET.get('slug',None)

    if request.method ==  'POST':
        found = db_user.objects.get(slug = service_slug)
        form = order_form(request.POST or None)
        if form.is_valid():
            _usernames = form.cleaned_data.get('usernames')
            _email = form.cleaned_data.get('email')
            _phone = form.cleaned_data.get('phone')
            #_title = detail
        _title = found.title
        _desc = found.description
        _date = found.date
        db_order = order.objects.create(
            s_title = _title,
            desc = _desc,
            usernames = _usernames,
            phone = _phone,
            email = _email
        )

        #subject = _title
        #message = _desc
        #from_email = 'drizzle.services@gmail.com'
        #to_email = 'drizzleboe@gmail.com'
#
        messages.success(request,f'Ahsante! order yako imepokelewa, drizzle store tutawasiliana na wewe kupitia email {_email} au namba yako {_phone} ')
        return redirect('success')
        #send_mail(
        #subject,
        #message,
        #from_email,
        #[to_email],
        #fail_silently=False,
        #)
    return render(request, 'registration/order.html',{
    'available':True,
    'form': _order_form,
    'year': now.year,
    })        
   

def tester(request):
    return render(request, 'registration/index.html',{
        'year': now.year,
    })
            
def about(request):
    _about_us = abouts.objects.all()
    return render(request, 'registration/about.html',{ 
        'about_us':_about_us,
        'year': now.year,
    })

def faq(request):
    _faqs=faqs.objects.all()
    return render(request, 'registration/faqs.html',{
        'faqs': _faqs,
        'year': now.year,
    })

def cart(request):
    return render(request, 'registration/cart.html',{
        'vailabel': True,
    })
def contact(request):
    _contact_us_form = contact_us_form()
    return render(request, 'registration/contacts.html',{
        'available':True,
        'form': _contact_us_form,
    })
    

###########################################################
###########################################################

def admin_login(request):
    Usr = User.objects.all()
    signin_form = sign_in(request.POST or None)
    #if 'user_id' in request.session:
    #    signed_in = subscriber.objects.get(id = request.session['user_id'])
    #    if signed_in:
    #        return redirect(f'myaccount/{signed_in.id}')
    if signin_form.is_valid():
        email = signin_form.cleaned_data.get('username')
        password = signin_form.cleaned_data.get('passwd')

        authenticated = authenticate(request, username = email, password = password)           
        if authenticated:
            #### getting a user from db
            if Usr.objects.get(email=email).is_staff:
                print('THIS IS A STAFF USER')
            else:
                print('THIS IS NOT A STAFF USER ')
            # login(request, authenticated)
            # _this_user = subscriber.objects.get(email = email)
            # request.session['user_id'] = _this_user.id
            # return redirect(f'myaccount/{_this_user.id}')
           
        else:
            #raise forms.ValidationError('password uliyoingiza sio sahihi') 
            print('not authenticated') 
        #else:     
        
        #print(authenticated)
        
        #    #raise forms.ValidationError('invalid username or password') 
        #    Failed = 1  
        #    request.session['attempts'] = 1 
        #    return render(request, 'registration/login.html',{
        #    'signin_form':signin_form,
        #    'failed': Failed,   
        #    })           
    return render(request, 'registration/admins/index.html', {
        'signin_form':signin_form,
        'year': now.year,
    })
