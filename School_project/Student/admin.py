from django.contrib import admin
from .models import Country, City, Student,Courses,Fees
# from .models import CompanyProblems


# class Country = ['user','country_name']

class CountryAdmin(admin.ModelAdmin):

    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Country, CountryAdmin)


# class City = ['user','city_name','country_name_column','population']    


class CityAdmin(admin.ModelAdmin):
    list_per_page = 6

    exclude = ['user']

    list_display = ['user', 'city_name']

    # search_fields = ['name','population']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(City, CityAdmin)


# Company : ['user','company_name','website','city','location',
# 'person_name','mobile','estabilishment_year','email','company_type',
# 'company_name','company_product','company_branches']

# Student : ['user','student_name','City','address','branch','education','experience']

class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'city', 'address', 'branch', 'education', 'experience','fees_paid']

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Student, StudentAdmin)



class CoursesAdmin(admin.ModelAdmin):
    list_display = ['course_name' , 'level', 'fees']

    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Courses,CoursesAdmin)



class FeesAdmin(admin.ModelAdmin):
    list_display = [ 'fees_date' , 'total_amount', 'balance_amount', 'level']

    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Fees,FeesAdmin)


