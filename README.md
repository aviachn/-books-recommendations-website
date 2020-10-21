# A books recommendations website based Python, HTML, CSS & JS
A public books vlog- all website users can share and post their opinions, ideas and insights about books they have read. They can add to their article their favorite quote from the book and upload an image.

### Motivation
As a book lover, I would like to know what people recommend reading and why, what made a book they read to be that great and also, share my ideas with others after reading book. I think that there is something unexplainable about sharing your thoughts after you read an enthusiastic book, a book that made you feel excited or inspired. That you can't keep your hands off of it and you want evreyone to enjoy it.   

### Frameworks
Django is a web application framework built on Python. Django allows to easily create dynamic web apps and have many features like:
* User authentication
* Templating language
* Routing and more


### Screenshots
As 
The articles available the users only after they logged in- the "Log in" and "Sign up" buttons disapir from the homepage and the "Read More" button appears instead.
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/72604721/96680121-949ba480-137d-11eb-9581-0d463638f2b0.gif)


![ezgif com-gif-maker](https://user-images.githubusercontent.com/72604721/96680349-0116a380-137e-11eb-8288-bef0a49a3ebd.gif)

### Code Example
The example I decided to show is creating an article-
The page where the user can upload his article required user authentication, therefore above the function we have a command that that making sure the user logged in. If the user is not, the "Log in" page will show up.
The function gets a request, if it's not a POST request the same page, with blank fields in the form will show up to the user again.
If it is a POST request the function will check rather the details in the fields are valid, if it is we will save them attached to the user who made the request and send the user back to the page where all the articles are, including the one that he created right now.
```
@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method =='POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user 
            instance.save()                 
            return redirect('articles:list')
    else: 
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})
```

### How To Use
