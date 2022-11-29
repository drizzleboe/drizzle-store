    
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from numpy import True_
from sqlalchemy import null
#from matplotlib.pyplot import title

# Create your models here.
class address(models.Model):
    #address_id = models.BigAutoField(primary_key=True)
    location       = models.CharField(max_length=20, null=False)
    pobox       = models.CharField(max_length=20, null=True, blank=True)
    postalcode    =  models.CharField(max_length=20, null=True, blank=True)
    
    def get_location(self):
         return self.location
    def get_postacode(self):
        return self.postalcode
    def get_pobox(self):
        return self.pobox
    def __str__(self):
        return f'{self.location}'
        # POBox {self.pobox}: postal code{self.postalcode}

class contact(models.Model):
    email    = models.EmailField()
    phone_no = models.CharField(max_length=20)
   

    def __str__(self):
        return f'{self.email} {self.phone_no}'  

class profession(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    
    def __str__(self):
        return self.name
        
class gender(models.Model):
    type = models.CharField(max_length=10) 
    def __str__(self) -> str:
        return self.type

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class top_image(models.Model):
    image       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    desc       = models.CharField(max_length=280, null=True)
    def __str__(self):
        return f'{self.image} {self.desc}'

class product(models.Model):
    #usr = models.OneToOneField(User, blank=True,null=True, on_delete=models.CASCADE)
    #first_name  = models.CharField(max_length=20, null=True)
    title   = models.CharField(max_length=80, null=True)
    slug = models.SlugField(unique=True)
    price = models.IntegerField()
    comparable_price = models.IntegerField(null=True, blank=True)
    description =models.TextField(max_length=500, null=True, blank=True)
    more = models.TextField(max_length=20000, null=True, blank=True)
    #gend        = models.ForeignKey(gender, on_delete=models.CASCADE, default=3)
    #username    = models.CharField(max_length=30, blank=True, null=True, unique=True)
    #password   = models.CharField(max_length=50, null='False')
    #age        = models.CharField(max_length=4)
    #slug       = models.Slugfield(max_length=30, unique=True)
    time        = models.TimeField(auto_now=True)
    date        = models.DateField(auto_now=True)
    image        = models.ImageField(upload_to='uploads/%Y/%m/%d/', )
    image1        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image2        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image3        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image4        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image5        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image6        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image7        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image8        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image9        = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image10       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image11       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    image12       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True, null= True)
    #button      = models.CharField(max_length=30)
    #prfssn      = models.ForeignKey(profession, on_delete=models.CASCADE, blank=False, null=True, default=6)
    #cont        = models.ForeignKey(contact, on_delete=models.CASCADE, blank=True, null=True)
#usr = models.ManyToManyField(user, blank=True, null = True)
    def __str__(self):
    
       return f'{self.title} - {self.date}'


class user(models.Model):
    #usr = models.OneToOneField(User, blank=True,null=True, on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=20, null=True)
    last_name   = models.CharField(max_length=80, null=True)
    email       = models.EmailField()
    #more = models.TextField(max_length=2000, null=True, blank=True)
    #gend        = models.ForeignKey(gender, on_delete=models.CASCADE, default=3)
    #username    = models.CharField(max_length=30, blank=True, null=True, unique=True)
    password   = models.CharField(max_length=50, null='False')
    #age        = models.CharField(max_length=4)
    #slug       = models.Slugfield(max_length=30, unique=True)
    time        = models.TimeField(auto_now=True)
    date        = models.DateField(auto_now=True)
    image       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/default-image.webp")
    phone       = models.CharField(max_length=13,blank=True,null=True)
    #button      = models.CharField(max_length=30)
    #prfssn      = models.ForeignKey(profession, on_delete=models.CASCADE, blank=False, null=True, default=6)
    #cont        = models.ForeignKey(contact, on_delete=models.CASCADE, blank=True, null=True)
    usr_cart      = models.ForeignKey(product, on_delete=models.CASCADE, blank=True, null=True)

    
class order(models.Model):
    s_title = models.CharField(max_length = 30)
    desc = models.TextField(max_length=200, null= True, blank= True)
    usernames = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    date        = models.DateField(auto_now=True)
    time        = models.TimeField(auto_now=True)

    def __str__(self):
        return f'order from {self.usernames} requested: {self.s_title}: placed on {self.date} {self.time}'
class cart(models.Model):
    #usr = models.ManyToManyField(user, on_delete=models.CASCADE, blank=True, null = True)
    name = models.ForeignKey(product, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
        
class staff(models.Model):
    full_name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    department = models.CharField(max_length=50)
    uploaded_on = models.DateField(auto_now = True)

    def __str__(self):
        return f'{self.full_name} : {self.department}'

class comment(models.Model):
    text = models.TextField(max_length=5000)
    def __str__(self) -> str:
        return self.text
class subscriber(models.Model):
    emails = models.EmailField()
    time        = models.TimeField(auto_now=True)
    date        = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.emails}'
class faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=1000)
    def __str__(self):
        return self.question
class about(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=5000)
    date        = models.DateField(auto_now=True)
    def __str__(self):
        return self.title

