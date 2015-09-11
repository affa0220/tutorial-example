from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from trips.models import Post as trip_post
from .forms import ContentForm
import datetime

def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})


def home(request):
    # get all the posts
    post_list = trip_post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list})


def post_detail(request, id):
    post = trip_post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})


def addcontent(request):
    template = 'add_cotent.html'

    if 'sub' in request.POST:
        title = request.POST['title']
        content = request.POST['content']
        photo = request.POST['photo']
        location = request.POST['location']
        date_time = datetime.datetime.now()

        c = trip_post(title=title, content=content, photo=photo, location=location, created_at=date_time)
        c.save()
        return HttpResponseRedirect('/')
    else:
        f = ContentForm()
    return render_to_response(template, locals())


def editcontent(request, id):
    template = 'edit_cotent.html'

    post = trip_post.objects.get(id=id)
    if 'sub' in request.POST:
        title = request.POST['title']
        content = request.POST['content']
        photo = request.POST['photo']
        location = request.POST['location']
        date_time = datetime.datetime.now()

        c = trip_post(title=title, content=content, photo=photo, location=location, created_at=date_time)
        c.save()
        return HttpResponseRedirect('/')
    else:
        form = ContentForm()
    return render_to_response(template, locals())

