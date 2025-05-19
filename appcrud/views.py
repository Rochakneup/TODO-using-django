from django.shortcuts import redirect, render
from appcrud.models import user , Todo

# Create your views here.
def home_view(request):
    return render (request, "home.html")



def login_view(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")

        found_user = user.objects.filter(name=name, password=password).first()
        
        if found_user:
            return redirect('/form')
        else:
            context = {"error": "Please provide valid credentials"}
            return render(request, "login.html", context)

    return render(request, "login.html")



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")

        if not name or not password:
            context = {"error": "All fields should be filled"}
            return render(request, "register.html", context)

        if User.objects.filter(username=name).exists():
            context = {"error": "Username already taken"}
            return render(request, "register.html", context)

        User.objects.create_user(username=name, password=password)
        return redirect('/login')

    return render(request, "register.html")



def todo_view(request):   
    if request.method == "POST":
        summary = request.POST.get("summary")
        description = request.POST.get("description")
        time = request.POST.get("time")

        if not summary or not description or not time:
            all_data = Todo.objects.all()  
            context = {
                'error': "All fields should be filled",
                'all_data': all_data
            }
            return render(request, "form.html", context)

        Todo.objects.create(summary=summary, description=description, TIme=time)
        return redirect("/form")

    all_data = Todo.objects.all()
    context = { 'all_data': all_data }
    return render(request, "form.html", context)

def delete_todo(request, id):
    item = Todo.objects.get(id=id)
    item.delete()
    return redirect('/form')

def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == "POST":
        todo.summary = request.POST.get("summary")
        todo.description = request.POST.get("description")
        todo.time = request.POST.get("time")
       
        todo.iscomplete = 'iscomplete' in request.POST
        todo.save()
        return redirect("/form")  

    return render(request, "updateform.html", {"todo": todo})

   
