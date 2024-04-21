"""
URL configuration for wildlife project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from wild import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # Include home.urls
    path('',views.index, name='index'),
    path('accounts/',views.accounts,name='accounts'),
    path('contact/',views.contact,name='contact'),
    path('ask_question/',views.ask_question,name='ask_question'),
    path('success/', views.success_page, name='success_page'),
    path('question/<int:question_id>/', views.question_details, name='question_details'),
    path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),


  
   
    
             ]
   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

