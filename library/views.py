from pyexpat.errors import messages
from library.forms import IssueBookForm
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from .forms import IssueBookForm
from django.contrib.auth import authenticate, login, logout
from . import forms, models
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404



def index(request):
    return render(request, "index.html")

@login_required(login_url = '/admin_login')
def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
        image = request.FILES['image']
       

        books = Book.objects.create(name=name, author=author, isbn=isbn, category=category ,image=image )
        books.save()
        alert = True
        return render(request, "add_book.html", {'alert':alert})
    return render(request, "add_book.html")

@login_required(login_url = '/admin_login')
def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {'books':books})


@login_required(login_url = '/admin_login')
def view_students(request):
    students = Student.objects.all()
    return render(request, "view_students.html", {'students':students})

@login_required(login_url = '/admin_login')
def issue_book(request):
    form = forms.IssueBookForm()
    if request.method == "POST":
        form = forms.IssueBookForm(request.POST)
        if form.is_valid():
            obj = models.IssuedBook()
            obj.student_id = request.POST['name2']
            obj.isbn = request.POST['isbn2']
            obj.save()
            alert = True
            return render(request, "issue_book.html", {'obj':obj, 'alert':alert})
    return render(request, "issue_book.html", {'form':form})

@login_required(login_url = '/admin_login')
def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(models.Book.objects.filter(isbn=i.isbn))
        students = list(models.Student.objects.filter(user=i.student_id))
        i=0
        for l in books:
            t=(students[i].user,students[i].user_id,books[i].name,books[i].isbn,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,fine)
            i=i+1
            details.append(t)
    return render(request, "view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})

@login_required(login_url = '/student_login')
def student_issued_books(request):
    student = Student.objects.filter(user_id=request.user.id)
    issuedBooks = IssuedBook.objects.filter(student_id=student[0].user_id)
    li1 = []

    for i in issuedBooks:
        books = Book.objects.filter(isbn=i.isbn)
        for book in books:
            days=(date.today()-i.issued_date)
            d=days.days
            fine=0
            if d>15:
                day=d-14
                fine=day*5
            t=(request.user.id, request.user.get_full_name, book.name, book.author, i.issued_date, i.expiry_date, fine)
            li1.append(t)

    return render(request,'student_issued_books.html',{'li1':li1})

@login_required(login_url = '/student_login')
def profile(request):
    return render(request, "profile.html")

@login_required(login_url = '/student_login')
def edit_profile(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']

        student.user.email = email
        student.phone = phone
        student.branch = branch
        student.classroom = classroom
        student.roll_no = roll_no
        student.user.save()
        student.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")

def delete_book(request, myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/view_books")

def delete_student(request, myid):
    students = Student.objects.filter(id=myid)
    students.delete()
    return redirect("/view_students")

def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "change_password.html")

def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        student = Student.objects.create(user=user, phone=phone, branch=branch, classroom=classroom,roll_no=roll_no, image=image)
        user.save()
        student.save()
        alert = True
        return render(request, "student_registration.html", {'alert':alert})
    return render(request, "student_registration.html")

def student_login(request):
    alert = success = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                alert = "You are not a student!!"
            else:
                success = "You have successfully logged in."
                
        else:
            alert = "Invalid username or password."
    return render(request, "student_login.html", {'alert': alert, 'success': success})

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                 success = True
                 return render(request, "add_book.html", {'success': success})
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")



def book_list(request):
    books = Book.objects.all()
    return render(request, "Book list.html", {'books': books})



from django.contrib.auth.decorators import login_required
from .models import Book

@login_required(login_url='/admin_login')
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
        image = request.FILES['image'] if 'image' in request.FILES else None

        book.name = name
        book.author = author
        book.isbn = isbn
        book.category = category
        if image:
            book.image = image
        book.save()
        alert = True
        return redirect('view_books')
    





def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        messages.success(request, 'Your message has been sent successfully.')
        return redirect('profile')  

    return render(request, 'contact.html')




def view_contacts(request):
    contacts = ContactMessage.objects.all()
    return render(request, 'view_contacts.html', {'contacts': contacts})

def Logout(request):
    logout(request)
    return redirect ("/")



def chatbot(request):
    return render(request, "chatbot.html")



    

def feedback(request):
    if request.method == 'POST':
        
        message = request.POST['message']

        feedback_message = FeedbackMessage( message=message)
        feedback_message.save()

        messages.success(request, 'Your feedback has been sent successfully.')
        return redirect('profile')  

    return render(request, 'feedback.html')



def view_feedbacks(request):
    feedbacks = FeedbackMessage.objects.all()
    return render(request, 'view_feedbacks.html', {'feedbacks': feedbacks})




# Import necessary modules
from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import json

# Load pre-trained RoBERTa model and tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Define the index view
def index(request):
    return render(request, 'index.html')



# Define the sentiment_analysis view
def sentiment_analysis(request):
    scores_dict = {}
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the input text from the request
        txt = request.POST.get('txt')


        # Tokenize the input text
        encoded_text = tokenizer(txt, return_tensors='pt')
        
        # Perform sentiment analysis using the pre-trained model
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        # Create a dictionary to store sentiment scores and input text
        scores_dict = {
            'neg': scores[0],
            'neu': scores[1],
            'pos': scores[2],
            'txt': json.dumps(txt),
        }
        

    # Render the sentiment_analyse.html template with sentiment scores
    return render(request, 'sentiment_analyse.html', scores_dict)