from django.shortcuts import render,reverse,HttpResponseRedirect
from ghostpost.models import *
from ghostpost.form import addRorB
import random
import string


# Create your views here.
def index(request):
    data = RoastsAndBoasts.objects.order_by('-time')
    return render(request, 'index.html',{'data': data})

def roast_view(request):
    data = RoastsAndBoasts.objects.filter(roastorboast=False).order_by('-time')
    return render(request, 'index.html', {'data': data})

def boast_view(request):
    data = RoastsAndBoasts.objects.filter(roastorboast=True).order_by('-time')
    return render(request, 'index.html', {'data': data})

def sortscore(request):
    data = RoastsAndBoasts.objects.all().order_by('-score')
    return render(request, 'index.html', {'data': data})

def like_view(request,post_id):
    post = RoastsAndBoasts.objects.get(id=post_id)
    post.upVotes += 1
    post.save()
    return HttpResponseRedirect(reverse('score',kwargs={'post_id': post_id}))

def dislike_view(request,post_id):
    post = RoastsAndBoasts.objects.get(id=post_id)
    post.downVotes += 1
    post.save()
    return HttpResponseRedirect(reverse('score',kwargs={'post_id': post_id}))

def score_view(request, post_id):
    post = RoastsAndBoasts.objects.get(id=post_id)
    post.score = post.upVotes - post.downVotes
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'),reverse('homepage'))

def createRorB(request):
    if request.method == 'POST':
        form = addRorB(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            randomChars = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
            RoastsAndBoasts.objects.create(
                roastorboast=data['roastorboast'],
                content=data['content'],
                secretKey=randomChars
            )
            return HttpResponseRedirect(reverse('private', kwargs={'private_key': randomChars}))
    form = addRorB()
    return render(request, 'create.html', {'form': form})

def single_view(request, post_id):
    data = RoastsAndBoasts.objects.filter(id=post_id)
    return render(request, 'index.html', {'data': data})

def private_view(request, private_key):
    data = RoastsAndBoasts.objects.filter(secretKey=private_key)
    return render(request,'index.html', {'data': data})

def delete_post(request,pk):
    data = RoastsAndBoasts.objects.filter(secretKey=pk)
    data.delete()
    return HttpResponseRedirect(reverse('homepage'))
