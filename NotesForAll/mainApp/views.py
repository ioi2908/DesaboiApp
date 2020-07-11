from django.shortcuts import render, redirect
from forms import UploadNotesModelForm
from .models import UploadNotes
import os
from twilio.rest import Client
from django_twilio.utils import discover_twilio_credentials
from django.contrib.auth.models import User
from twilio.twiml.messaging_response import MessagingResponse
from decouple import config
from django.views.decorators.csrf import csrf_exempt


def upload_complete(request):
    return render(request, template_name='done.html')

def upload_notes(request):
    form = UploadNotesModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('done')
    
    form = UploadNotesModelForm()
    args = {'form':form}
    return render(request, template_name='home.html', context=args)


# def download_notes(request):

#     notes = UploadNotes.objects.filter(notes=needed_filename)
#     notes_size = os.path.getsize(notes)
#     print(notes_size)
    
#     return 'downloaded !'


    
def search(request):
    query_sets = UploadNotes.objects.all()
    query = request.GET.get('notes_code')
    if query:
        query_sets = query_sets.filter(filename__icontains=query)
        
    args = {'query_sets':query_sets}
    return render(request, template_name='index.html', context=args)


@csrf_exempt
def inbound_sms(request):
    acc_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    
    twilio_client = Client(acc_sid, auth_token)
    
    message = twilio_client.messages.create(to= '+255717614769',from_='+14155238886', body='mambo vipi?')
    
    print(message.sid) 
    return 'Imetumwa'


  