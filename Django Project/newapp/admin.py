from django.contrib import admin
from newapp.models import  Image,Student,Admission,Marks
# Register your models here.

# @admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('id','photo','date')
admin.site.register(Image,ImageAdmin)

class student_admin(admin.ModelAdmin):
    
    list_display=('sname','regno','address','taluka','district','state','pincode','pincode')
admin.site.register(Student,student_admin) 

class Admission_admin(admin.ModelAdmin):
    list_display=('regno','sname','classes','branch','doa','semester')
admin.site.register(Admission,Admission_admin)

class marks_admin(admin.ModelAdmin):
    list_display=('regno','subject','mark','semester','year')
admin.site.register(Marks,marks_admin)

