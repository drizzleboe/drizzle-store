from django.contrib import admin
from .models import top_image as top,address, profession,contact,product,gender,staff,order,comment,user,subscriber,faq,about as about_us
#.django.contrib.auth.

# Register your models here.
class admincust(admin.ModelAdmin):
    list_display=['usernames','s_title','phone','email','date','time']
    list_filter =['date','s_title']
  #  prepopulated_fields={'slug':('fname','lname')}
class sub_(admin.ModelAdmin):
  list_display=['emails','date','time']
  list_filter= ['date']
class staff_(admin.ModelAdmin):
    list_display=['full_name','department','uploaded_on']
    list_filter =['department','uploaded_on']
class pplt(admin.ModelAdmin):
  prepopulated_fields={'slug':('title', )}
#admin.site.register(user, admincust)
#admin.site.register(address,admincust)
#admin.site.register(profession)
#admin.site.register(contact)
admin.site.register(gender)
admin.site.register(top)
admin.site.register(product,pplt)
admin.site.register(staff, staff_)
admin.site.register(order,admincust)
admin.site.register(comment)
admin.site.register(user)
admin.site.register(subscriber, sub_)
admin.site.register(faq)
admin.site.register(about_us)