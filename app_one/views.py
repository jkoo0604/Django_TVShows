from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def gotoshows(request):
    return redirect('/shows')

def index(request):
    #Display list of TV shows
    context = {
        'all_shows': Show.objects.all(),
    }
    return render(request,'index.html',context)

def new(request):
    #Show form to add new show
    return render(request,'newshow.html')

def create(request):
    #Add a new show
    #Process POST request and redirect to showid page
    
    # errors = Show.objects.basic_validator(request.POST, -1)
    # if len(errors) > 0:
    #     # print(errors)
    #     for key, value in errors.items():
    #         messages.error(request, value, extra_tags=key)
    #     return redirect('/shows/new')

    newshow=Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],desc=request.POST['desc'])

    return redirect(f'/shows/{newshow.id}')

def show(request,showid):
    #Show info about one show
    context = {
        'one_show': Show.objects.get(id=showid)
    }
    return render(request,'showinfo.html',context)

def edit(request,showid):
    #Show form to edit existing show
    context = {
        'one_show': Show.objects.get(id=showid)
    }
    return render(request,'editshow.html',context)

def update(request,showid):
    #Update a show
    #Process POST request and redirect to showinfo page
    # errors = Show.objects.basic_validator(request.POST, showid)
    # if len(errors) > 0:
    #     print(errors)
    #     for key, value in errors.items():
    #         messages.error(request, value, extra_tags=key)
    #     return redirect(f'/shows/{showid}/edit')

    updateshow=Show.objects.get(id=showid)
    updateshow.title=request.POST['title']
    updateshow.network=request.POST['network']
    updateshow.release_date=request.POST['release_date']
    updateshow.desc=request.POST['desc']
    updateshow.save()
    # Show.objects.filter(id=showid).update(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],desc=request.POST['desc'])
    # return redirect('showinfo',showid=showid)
    return redirect(f'/shows/{showid}')

def delete(request,showid):
    #Delete a show
    #Process POST request and redirect to all shows
    Show.objects.filter(id=showid).delete()
    return redirect('/shows')

def testunique(request):
    title = request.GET.get("title", None)
    showid = int(request.GET.get("showid", None))
    print(title)
    print(showid)
    if showid > 0:
        if Show.objects.filter(title__iexact=title).exclude(id=showid).exists():
            return JsonResponse({"used":True}, status = 200)
        else:
            return JsonResponse({"used":False}, status = 200)
    elif Show.objects.filter(title__iexact=title).exists():
        return JsonResponse({"used":True}, status = 200)
    else:
        return JsonResponse({"used":False}, status = 200)
    
    return JsonResponse({}, status = 400)