"""TY_IT_8Sept URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,re_path

from student.views import view_hello,view_record,view_hello_20,StudentList
from student.views import StudentListCreate,StudentListUpdate,StudentListDelete
from student.views import view_sy,view_fy,view_ty,view_index
# from student.views import view_django


# from django.conf.urls import re_path

#   https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html    REPORTS GEN

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^sy/', view_sy, name='link_sy'),
    re_path(r'^index/', view_index, name='link_index'),
    re_path(r'^ty/', view_ty, name='link_ty'),
    re_path(r'^fy/', view_fy, name='link_fy'),
    re_path(r'^HI/', view_hello, name='link_hello'),
    re_path(r'^hello1/', view_hello),
    re_path(r'^hello20/', view_hello_20),
    re_path(r'^record1/', view_record, name='link_record'),
    path('', StudentList.as_view(), name='student1_list'),

    path('new', StudentListCreate.as_view(), name='Student_new'),
	path('edit/<int:pk>', StudentListUpdate.as_view(), name='Student_edit'),
  	path('delete/<int:pk>', StudentListDelete.as_view(), name='Student_delete'),


    # url(r'^django/', view_django),




]
