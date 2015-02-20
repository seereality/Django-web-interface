
# Create your views here.
import json
from django.core.mail import send_mail
from django.core import serializers
from django.utils.timezone import now as utcnow
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from datetime import datetime as dt
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from webrtc.models import Consumer,Uploaded_file

# Create your views here.


def main(request):
    context={}
    return render(request,'webrtc/main.html',context)




@login_required
def home(request):
    context={}
    return render(request,'webrtc/home.html',context)


@login_required
def index(request):
    if request.user.is_authenticated():
        user=request.user.username
        email = request.user.email
        context = {'user': user, 'email': email}
    return render(request, 'webrtc/index.html', context)

def delete_file(request,file_id):
	query = Uploaded_file.objects.get(pk = file_id)
	query.delete()
	return HttpResponseRedirect('/webrtc/view_archive')
def upload_file(request):
	if request.method=='POST':
		form=Uploaded_file()
		form.file_name=request.POST['filename']
		form.Notes=request.POST['notes']
		form.Rating=request.POST['rating']
		docfi=request.FILES['docfile']
		valit = datetime.datetime.now();
		form.timestamp = valit
		form.user_id = request.user
		form.docfile.save(docfi.name,docfi)
		form.save()
		return HttpResponseRedirect('/webrtc/main')
	return render(request,'webrtc/file_upload.html')

def view_archive(request):
        order_list = Uploaded_file.objects.all().order_by('timestamp')
        context = {'order_list': order_list}
        return render(request, 'webrtc/archive.html', context)	

def faqs(request):
    return render(request, 'webrtc/faqs.html');

def feedback(request):
    return render(request, 'webrtc/feedback.html');

def contact(request):
    return render(request, 'webrtc/contact.html');

def about(request):
    return render(request, 'webrtc/about.html');


