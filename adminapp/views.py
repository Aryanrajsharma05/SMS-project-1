import base64
import calendar
import random
import string
from asyncio import tasks
from datetime import datetime, timedelta
from io import BytesIO
from turtle import pd

from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Contact
from .forms import TaskForm, UploadFileForm,
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from .forms import StudentForm
from .models import StudentList
import pandas as pd
from .forms import ContactForm



def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')


def printpagecall(request):
    return render(request, 'adminapp/printer.html')


def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        print(f'User input: {user_input}')
        a1 = {'user_input': user_input}
        return render(request, 'adminapp/printer.html', a1)
    return render(request, 'adminapp/printer.html')


def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')


def exceptionalpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')


def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')


def randompagelogic(request):
    if request.method == "POST":
        number1 = int(request.POST.get('number1', 0))
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
        a1 = {'ran': ran}
        return render(request, 'adminapp/randomexample.html', a1)
    return render(request, 'adminapp/randomexample.html')


def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')


def calculatorpagelogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation', '')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num2 != 0 and num1 / num2 or 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})


def datetimepagecall(request):
    return render(request, 'adminapp/datepage.html')


def datetimepagelogic(request):
    if request.method == 'POST':
        number1 = int(request.POST['date1'])
        x = datetime.now()
        ran = x + timedelta(days=number1)
        ran1 = ran.year
        ran2 = calendar.isleap(ran1)
        if ran2 == False:
            ran3 = "Not Leap Year"
        else:
            ran3 = "Leap Year"
    a1 = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
    return render(request, 'adminapp/datepage.html', a1)


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html',
                  {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')


def UserRegisterPageCall(request):
    return render(request, 'adminapp/RegisterPage.html')


def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/RegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/RegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.success(request, 'Account created Successfully!')
                return redirect('projecthomepage')  # Redirect to the homepage after successful registration
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'adminapp/RegisterPage.html')
    else:
        return render(request, 'adminapp/RegisterPage.html')


def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/UserLoginPage.html')
    else:
        return render(request, 'adminapp/UserLoginPage.html')


def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')


'''def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})'''

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})


def upload_file(request, plt=None):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_sales = df['Sales'].sum
        average_sales = df['Sales'].mean()

        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution per Month')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request, 'adminapp/chart.html', {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'chart': image_data
        })

    return render(request, 'adminapp/chart.html', {'form': UploadFileForm()})

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()  # This line should now work correctly
            return redirect('feedback_success')  # Redirect after successful submission
    else:
        form = FeedbackForm()

    return render(request, 'adminapp/feedback.html', {'form': form})



def feedback_success(request):
    return render(request, 'adminapp/feedback.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import add_contact  # Assume you have a forms.py with a ContactForm defined
from django.contrib import messages


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_contact')  # Redirect to the same page after saving
    else:
        form = ContactForm()

    contacts = Contact.objects.all()  # Fetch all contacts to display
    return render(request, 'adminapp/add_contact.html',
                  {'form': form, 'contacts': contacts})


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('add_contact')  # Redirect to the add_contact view after deletion

