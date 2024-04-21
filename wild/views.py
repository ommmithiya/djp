from django.conf import settings

from django.utils import timezone  
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question

def question_details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'question_details.html', {'question': question})


def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        # Process form submission
        answer_text = request.POST.get('answer_text')
        # Save answer to the database, assuming Answer model exists
        question.answer_set.create(answer_text=answer_text)
        return redirect('question_details', question_id=question_id)
    return render(request, 'answer_question.html', {'question': question})


def ask_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        
        question = Question(question_text=question_text, pub_date=timezone.now())
        question.save()
        return redirect('success_page') 
    else:
        return render(request, 'ask_question.html')

def success_page(request):
    return render(request, 'success_page.html')


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def accounts(request):
    return render(request, 'accounts.html')







