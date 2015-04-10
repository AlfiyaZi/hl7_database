from django.shortcuts import render
from hl7.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from hl7apy.parser import parse_message

def index(request):
	context = RequestContext(request)
	if request.method=='POST':
		text = request.POST['hl7doc']
		message = parse_message(text)
		doc = Document()
		doc.save()
		msh = ComponentMSH()
		msh.doc = doc
		msh.text = message.msh
		pid = ComponentPID()
		pid.doc = doc
		pid.text = message.pid
		evn = ComponentEVN()
		evn.doc = doc
		evn.text = message.evn
		msh.save()
		pid.save()
		evn.save()
		return HttpResponseRedirect('/')
	return render_to_response('index.html', {}, context)

# Create your views here.
