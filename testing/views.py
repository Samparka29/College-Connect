from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import Question,Answer,Upvote,Downvote,JobPosting,Notes
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import AnswerForm,QuestionForm,UserDetail,PostingForm,NotesForm
from django.db.models import Count
from django.core.files.storage import FileSystemStorage


# Detail
def detail(request,id):
    quest=Question.objects.get(pk=id)
    tags=quest.tags.split(',')
    answers=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            answer=answerData.save(commit=False)
            answer.question=quest
            answer.user=request.user
            answer.save()
            messages.success(request,'Answer has been submitted.')
    return render(request,'detail.html',{
        'quest':quest,
        'tags':tags,
        'answers':answers,
        'answerform':answerform
    })  

# Home Page
def index(request):
    # for the searching functionality
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Question.objects.annotate(total_comments=Count('answer')).filter(title__icontains=q).order_by('-id')
    else:
        quests=Question.objects.annotate(total_comments=Count('answer')).all().order_by('-id')
    paginator=Paginator(quests,5)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'index.html',{'quests':quests})

  

# for the jobposting page
def jobPosting(request):
    jobs=JobPosting.objects.filter(user=request.user)
    form=PostingForm
    if request.method =='POST':
        postingform=PostingForm(request.POST)
        if postingform.is_valid():
            postingform=postingform.save(commit=False)
            postingform.user=request.user
            postingform.save()
            messages.success(request,'your post is added')
            return redirect("jobPosting")
    return render(request,'jobPosting.html',{'form':form,'jobs':jobs})

def ask_form(request):
    form=QuestionForm
    if request.method=='POST':
        questform=QuestionForm(request.POST)
        if questform.is_valid():
            questform=questform.save(commit=False)
            questform.user=request.user
            questform.save()
            messages.success(request,'Question has been added')
    return render(request,'askquestion.html',{'form':form})   

def user_form(request):
    quests=Question.objects.filter(user=request.user)
    answers=Answer.objects.filter(user=request.user)
    form=UserDetail(instance=request.user)
    if request.method=='POST':
        userform=UserDetail(request.POST)
        if userform.is_valid():
            userform=userform.save(commit=False)
            userform.user=request.user
            userform.save()
            messages.success(request,'Page is opned')
    return render(request,'userdetail.html',{'form':form,'quests':quests,'answers':answers})  


# Questions according to tag
def tag(request,tag):
    quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(tags__icontains=tag).order_by('-id')
    paginator=Paginator(quests,2)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'tag.html',{'quests':quests,'tag':tag})   


# Save Upvote
def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=Upvote.objects.filter(answer=answer,user=user).count()
        checkDownvote=Downvote.objects.filter(answer=answer,user=user).count()
        if check > 0 or checkDownvote > 0:
            return JsonResponse({'bool':False})
        else:
            Upvote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

# Save Downvote
def save_downvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=Downvote.objects.filter(answer=answer,user=user).count()
        checkUpvote=Upvote.objects.filter(answer=answer,user=user).count()
        if check > 0 or checkUpvote > 0:
            return JsonResponse({'bool':False})
        else:
            Downvote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

    
def aboutus(request):
    return render(request,'aboutus.html')


def notes(request):
    pdfs=Notes.objects.all()
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("notes")
    else:
        form = NotesForm() 
    return render(request, 'notes.html',{'form':form,'pdfs':pdfs})



def delete_notes(request,pk):
    if request.method=='POST':
        pdf=Notes.objects.get(pk=pk)      
        pdf.delete()
    return redirect('notes')     








    # def save_comment(request):
    # if request.method=='POST':
    #     # request.POST is a dictionary-like object that lets you access submitted data by key name.
    #     comment=request.POST['comment']
    #     answerid=request.POST['answerid']
    #     answer=Answer.objects.get(pk=answerid)
    #     user=request.user
    #     Comment.objects.create(
    #         answer=answer,
    #         comment=comment,
    #         user=user
    #     )
    #     return JsonResponse({'bool':True})
# comments=Comment.objects.filter(user=request.user)