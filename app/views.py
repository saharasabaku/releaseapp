from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.template import loader

from .models import Image
from .forms import ImageForm
from .models import Question

def base(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('app/base.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('app/home.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def illust(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'app/illust.html', context)

def about(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('app/about.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album:showall')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'album/upload.html', context)


