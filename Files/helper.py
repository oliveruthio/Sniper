import mechanize
import re
from bs4 import BeautifulSoup

class Info:


    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [('User-agent', 'Firefox')]

    username = ''
    password = ''
    quarter = ''
    subject = ''
    section = ''
    selection = -1

    def logon(self, username, password):
	
	#br = self.br

	url = "https://my.sa.ucsb.edu/gold/Login.aspx"
	response = self.br.open(url)

	self.br.form = list(self.br.forms())[0]
	control = self.br.form.find_control("ctl00$pageContent$userNameText")
	control.value = username
	control = self.br.form.find_control("ctl00$pageContent$passwordText")
	control.value = password
	control = self.br.form.find_control("ctl00$pageContent$CredentialCheckBox")
	control.items[0].selected = True
	
	self.response = self.br.submit()
	
	self.username = username
	self.password = password

    def get_list_of_courses(self):
	
	url = 'https://my.sa.ucsb.edu/gold/BasicFindCourses.aspx'
	
	self.response = self.br.open(url)
	self.br.form = list(self.br.forms())[0]

	# Quarter -> quarter_list

	control = self.br.form.find_control("ctl00$pageContent$quarterDropDown")
	quarter_list=[]
	for item in control.items:
	    quarter_list.append(str([label.text  for label in item.get_labels()][0]))
	


	# Subject Area ->  subject_area_list

	control = self.br.form.find_control("ctl00$pageContent$subjectAreaDropDown")
	subject_area_list=[]
	for item in control.items:
	    if item.name != control.items[0].name:
		subject_area_list.append(str([label.text  for label in item.get_labels()][0]))


	return quarter_list, subject_area_list
    
    
    def set_list_of_courses(self, quarter_selection, subject_area_selection, class_number):
	url = 'https://my.sa.ucsb.edu/gold/BasicFindCourses.aspx'
    
	self.response = self.br.open(url)
	self.br.form = list(self.br.forms())[0]

	control = self.br.form.find_control("ctl00$pageContent$quarterDropDown")
	counter=0
	for item in control.items:
	    if quarter_selection == str([label.text  for label in item.get_labels()][0]):
		control.value = [control.items[counter].name]
	    counter += 1
	quarter_selection = control.value[0]
	
	
	
	control = self.br.form.find_control("ctl00$pageContent$subjectAreaDropDown")
	counter=0
	for item in control.items:
	    if subject_area_selection == str([label.text  for label in item.get_labels()][0]):
		control.value = [control.items[counter].name]
	    counter += 1
	subject_area_selection = control.value[0]
	
	
	
	
	control = self.br.form.find_control("ctl00$pageContent$courseNumberTextBox")
	control.value = class_number
	
	self.response = self.br.submit() 
	
	self.quarter=quarter_selection
	self.subject=subject_area_selection
	self.section=class_number
	    
    
    def get_specific_class(self):
	
	url = 'https://my.sa.ucsb.edu/gold/ResultsFindCourses.aspx'
	self.response = self.br.open(url)
	
	content = self.response.read()
	
	data=[]
    
	soup = BeautifulSoup(content)
	find_title = soup.find_all(id="pageContent_CourseList_PermNbr_0")
    
	count=1
	while find_title:
    
	    soup = BeautifulSoup(str(find_title))
	    find_title = soup.find_all("span")
	    title = re.sub(r'[\xc2\xa0]', " ", unicode(find_title[0].contents[0]))
	    title = re.sub(' +',' ', title)
	    data.append(str(title).rstrip())
	
	    soup = BeautifulSoup(content)
	    name ="pageContent_CourseList_PermNbr_"+str(count)
	    find_title = soup.find_all(id=name)
	    count+=1
	return data
    
    def save_data(self, final_int):
	data = [self.username.encode('utf-8'), self.password.encode('utf-8'), [self.quarter.encode('utf-8')], [self.subject.encode('utf-8')], self.section.encode('utf-8'), final_int]

	myfile = open('settings.txt','w')
	myfile.write(str(data))
	myfile.close()
    

	