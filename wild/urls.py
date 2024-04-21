from django.urls import path
from . import views

urlpatterns =[
    
   path('', views.index, name='index'), 
   path('accounts/',views.accounts,name='accounts'),  
   path('contact/',views.contact,name='contact'),
   path('ask_question/',views.ask_question,name='ask_question'),
   path('success/', views.success_page, name='success_page'),
   path('question/<int:question_id>/', views.question_details, name='question_details'),
   path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
]


   

   

   
   
   



