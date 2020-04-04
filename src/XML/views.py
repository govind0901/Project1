from django.shortcuts import render ,redirect
from django.core.files.storage import FileSystemStorage
from .genXML import genXML
from .XML_PAR import XML_PAR
import os
from django.utils.safestring import mark_safe
from django.template import Library
import json
  



def generateXMLFile(request,*args, **kwargs):

	my_diction ={}

	my_diction2 ={}
	context={} 
	uploaded_file_list = []

	model_list = []

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))	
	if request.method == 'POST':
		
		uploaded_file = request.FILES['document']

		fs=FileSystemStorage()

		name = fs.save(uploaded_file.name , uploaded_file)

		xmlfile_name = genXML(name)

		my_diction = XML_PAR(xmlfile_name)
		
		
		for f_name in os.listdir(BASE_DIR):
			if f_name.endswith('.py'):
				if f_name != 'manage.py':
					uploaded_file_list.append(f_name)


		for x in my_diction:
			model_list.append(x)


		my_diction2.update({name : model_list })
		

		context = {'url' :fs.url(name), 'my_diction' : my_diction , 'uploaded_file_list' : uploaded_file_list , 'link_to_file' : my_diction2}
		
		return render(request,'createXML.html', context)



	if bool(request.FILES.get('filepath', False)) == True:
		if my_diction:
			print(my_diction)

		
		#return render(request, 'createXML.html',my_diction)

	else:
		
		


		return render(request, 'createXML.html',context)





