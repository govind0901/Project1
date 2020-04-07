from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .genXML import genXML
from .XML_PAR import XML_PAR
from django.utils.safestring import mark_safe
from django.template import Library
import os


def generateXMLFile(request, *args, **kwargs):
    my_diction = {}
    i=0
    context = {}
    model_list = []
    if request.method == 'GET':
       
        print('get')
        if 'text' in request.FILES:
            print('yes there')
        return render(request, 'createXML.html', context)

    if request.method == 'POST':
        if 'text' not in request.POST:
            i=1
            uploaded_file = request.FILES['document']
            fs=FileSystemStorage(location = './statics')
            name = fs.save(uploaded_file.name, uploaded_file)
            xmlfile_name = genXML(name)
            my_diction = XML_PAR(xmlfile_name)
            context = {'my_diction': my_diction}
            return render(request, 'createXML.html', context)

        if 'text' in request.POST or i:
            content = request.POST.get('text')

            
            fields = content.split('&&&')
            modelnames = []
            definitions = []
           
            for f in fields:
                modelName = f.split('->')[0]
                modelnames.append(modelName)
                
                fieldDefinition = f.split('->')[1]
                definitions.append(fieldDefinition)
            name = 'outputXML.xml'
            file = open(os.path.join('statics', 'outputXML.xml'), 'w+')
            with open(os.path.join('statics', 'outputXML.xml')) as xmlFile:
                file.write('<XML_DOC>' + '\n\n')
                i = 0
                file.write('<Entities>' + '\n')
                for name in modelnames:
                    file.write("<Fields type='" + name + "' class='EntityProperties' displayProperty='" + name + "'>")
                    print("<Fields type='" + name + "' class='EntityProperties' displayProperty='" + name + "'>")
                    file.write(definitions[i])
                    file.write('</Fields>' + '\n')
                    i = i + 1
                file.write('</Entities>' + '\n\n')
                file.write('</XML_DOC>')
                file.close()
            
            return render(request, 'createXML.html', context)

    
    
        
