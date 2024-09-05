from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.contrib.auth.decorators import login_required
from . filters import JobFilter




def job_list(request):
    job_list = Job.objects.all()
    ## filters
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    '''
    context= {
        "variable name in template": "variable name in view"
    }
    '''

    return render(request,"job/job_list.html",context = {'jobs' : page_obj, 'myfilter':myfilter})



def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method =="POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()

    else:
        form = ApplyForm()

    context={'job_detail' : job_detail, 'form' : form}
    return render(request,"job/job_detail.html",context)


@login_required 
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.onwer = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    context ={'job_form' : form}
    return render(request,"job/add_job.html",context)