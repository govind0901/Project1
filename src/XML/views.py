from django.shortcuts import render ,redirect
from django.core.files.storage import FileSystemStorage
from .genXML import genXML
from .XML_PAR import XML_PAR
from django.utils.safestring import mark_safe
from django.template import Library


def generateXMLFile(request,*args, **kwargs):

	my_diction ={}
	context={}
	model_list = []
	if request.method == 'POST':

		uploaded_file = request.FILES['document']
		fs=FileSystemStorage()
		name = fs.save(uploaded_file.name , uploaded_file)
		xmlfile_name = genXML(name)
		my_diction = XML_PAR(xmlfile_name)

		context = {'my_diction' : my_diction}

		return render(request,'createXML.html', context)

	else:

		return render(request, 'createXML.html',context)
