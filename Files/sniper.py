
import re
import mechanize
import helper
import string

class Snipe:
    def cap(self, s, l):
	return s if len(s)<=l else s[0:l-3]+'...'

    username = ''
    password = ''
    quarter = ''
    class_select = ''
    class_section = ''
    choice = ''
    
    
    class_data=[]
    class_title=''
    
    
    def set_data(self):
	myfile = open('settings.txt','r')
	data = myfile.read()
	myfile.close()

	self.username =  data[1:-1].split(',')[0][1:-1]
	self.password =  data[1:-1].split(',')[1][2:-1]
	self.quarter = [data[1:-1].split(',')[2][3:-2]]
	self.class_select = [data[1:-1].split(',')[3][3:-2]]
	self.class_section = data[1:-1].split(',')[4][2:-1]
	self.choice = int(data[1:-1].split(',')[5][1])

   
    
    def __do_action(self):
	username = self.username
	password = self.password
	quarter = self.quarter
	class_select = self.class_select
	class_section = self.class_section
	choice = self.choice
	
	
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent', 'Firefox')]
    
	url = "https://my.sa.ucsb.edu/gold/Login.aspx"
	print 'opening:\t', url
	response = br.open(url)
	br.form = list(br.forms())[0]
	control = br.form.find_control("ctl00$pageContent$userNameText")
	control.value = username
	control = br.form.find_control("ctl00$pageContent$passwordText")
	control.value = password
	control = br.form.find_control("ctl00$pageContent$CredentialCheckBox")
	control.items[0].selected = True
	print 'submitting:\t', url
	response = br.submit()


	url = 'https://my.sa.ucsb.edu/gold/BasicFindCourses.aspx'
	print 'opening:\t', url
	response = br.open(url)
	br.form = list(br.forms())[0]
	control = br.form.find_control("ctl00$pageContent$quarterDropDown")
	control.value = quarter
	control = br.form.find_control("ctl00$pageContent$subjectAreaDropDown")
	control.value = class_select
	control = br.form.find_control("ctl00$pageContent$courseNumberTextBox")
	control.value = class_section
	print 'submitting:\t', url
	response = br.submit()


	content = response.read()

	titles = helper.find_title(content)
	x = helper.get_info(content, choice)
	
	return x,titles[choice]
    def print_data(self):
	title = self.class_title
	
	
	print "\n\n" + title + "\n\n"
    
	matrix = self.class_data	    
	max_lens = [max([len(str(r[i])) for r in matrix]) for i in range(len(matrix[0]))]
	print "\n".join(["".join([string.ljust(self.cap(str(e), 30), l + 2) for e, l in zip(r, max_lens)]) for r in matrix])
	print ''

    def do_action(self):
	self.set_data()
	if helper.verify(self.username):
	    print 'You are verified as', self.username
	    self.class_data, self.class_title = self.__do_action()
	else:
	    print 'You are not verified (username %s). Contact owner.' % self.username
