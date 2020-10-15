from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
#from django.http import HttpResponse   
# Create your views here.

@login_required(login_url="/accounts/login/")
def article_list(request):
    articles = Article.objects.all().order_by('date')   #creating a dictionary that we're going to send to the template
    return render(request,'articles/article_list.html',{'articles' : articles}) #sending what we were retrive




@login_required(login_url="/accounts/login/")
def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})



@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method =='POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user  #attach the autohr to this instance, to this article
            instance.save() #commit
            return redirect('articles:list')
    else: 
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})










