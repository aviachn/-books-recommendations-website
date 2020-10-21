# A books recommendations website based Python, HTML, CSS & JS
A public books vlog- all website users can share and post their opinions, ideas and insights about books they have read. They can add to their article their favorite quote from the book and upload an image.

### Motivation
As a book lover, I would like to know what people recommend reading and why, what made a book they read to be that great and also, share my ideas with others after reading book. I think that there is something unexplainable about sharing your thoughts after you read an enthusiastic book, a book that made you feel excited or inspired. That you can't keep your hands off of it and you want evreyone to enjoy it.   

### Framework
Django is a Python web application framework. Django allows to easily create dynamic web apps and have many features like:
* User authentication
* Templating language
* Routing and more


### Screenshots
As 
![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/72604721/96691368-7d64b300-138d-11eb-8337-4d7e092b7cfe.gif)
The articles available the users only after they logged in- the "Login" and "Signup" buttons disapir from the homepage and the "Read More" button appears instead.
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/72604721/96680121-949ba480-137d-11eb-9581-0d463638f2b0.gif)


### Code Example
The example I decided to show is creating an article-
The page where the user can upload his article required user authentication, therefore above the function we have a command that making sure the user logged in. If the user is not, the "Login" page will show up.
The function gets a request, if it's not a POST request the same page, with blank fields in the form will show up to the user again.
If it is a POST request the function will check rather the details in the fields are valid, if it is we will save them attached to the user who made the request and send the user back to the page where all the articles are, including the one that he created right now.
```
@login_required(login_url="/accounts/login/")                               #if the user isn't logged in send him to the login page
def article_create(request):                                            
    if request.method =='POST':                                             #if it's a GET request
        form = forms.CreateArticle(request.POST, request.FILES)             # save the request in form variable 
        if form.is_valid():                                                 #check if the data request that saved in the form is valid
            instance = form.save(commit=False)                              #the request validation saved in instance variable 
            instance.author = request.user                                  #save in author field the name of the user who created the article
            instance.save()                                                 
            return redirect('articles:list')                                #return the list article page after update
    else:                                                                   #if it's a POST request return the same page with an empty form
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})
```
![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/72604721/96689550-34136400-138b-11eb-9432-30c559aa07a0.gif)

### How To Use
1. After installing 
2. open your command line and run <cd THE_PATH> when THE_PATH is the path where you saved the project.
3. run <python manage.py runserver>
4. open you explorer and in the url line insert <http://localhost:8000/> 
