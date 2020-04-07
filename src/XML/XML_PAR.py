import xml.etree.ElementTree as ET

def XML_PAR(xmlfile_name):


	my_tree = ET.parse(xmlfile_name)
	my_root = my_tree.getroot()

	

	model_names_list = []
	for x in my_root[0]:
		
		model_name = str(x.attrib)
		model_name = model_name.split(': ')[1].split(', ')[0][1:-1]
		model_names_list.append(model_name)
	

	my_diction = {}
	my_list = []
	NAME =""

	
	
	for name in model_names_list:

		my_list = []

		for x in my_root[2]:

			
			
			name_model = str(x.attrib)
			name_model = name_model.split("{'class': 'DisplayText', 'fieldName': '")[1].split("',")[0].split('.')[0]
			name_field = str(x.attrib)
			name_field = name_field.split("{'class': 'DisplayText', 'fieldName': '")[1].split("',")[0].split('.')[1]
			
			if name_model==name:
				my_list.append(name_field)
				
		NAME = str(name)

		my_diction.update({NAME : my_list})

	return my_diction

	



