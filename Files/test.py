import helper
import sniper
'''
MyClass = helper.Info()

MyClass.logon('username', 'password')

quarter_list, subject_area_list = MyClass.get_list_of_courses()
print quarter_list
print subject_area_list[53]

print quarter_list[0]

MyClass.set_list_of_courses(quarter_list[0], subject_area_list[53], '4')
'''


MySniper = sniper.Snipe()
MySniper.set_data()
MySniper.do_action()
MySniper.print_data()


#print MyClass.get_specific_class()
