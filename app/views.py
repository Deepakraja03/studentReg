from django.shortcuts import render,HttpResponse
from .models import Student
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        gen = request.POST['gender']
        cla = request.POST['className']
        regn = request.POST['reg']
        test = request.POST['test']
        if float(test) > 100:
            return HttpResponse("Test Score must be less than 100")
        obj = Student()
        obj.name = name
        obj.email = email
        obj.dob = dob
        obj.gender = gen
        obj.Stuclass = cla
        obj.reg = regn
        obj.test = test
        obj.save()
        return HttpResponse("<h1>Your entry have been saved</h1>")
    return render(request, 'index.html')

def list_stu(request):
    obj = Student.objects.all()
    return render(request, 'list.html', {'obj':obj})