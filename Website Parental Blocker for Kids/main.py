from pywinauto import Application 		#pywinauto grabs the current tab information
import os
import time 								#OS Module to Shut down Chrome


def kill_function():
	try:	
		app = Application(backend='uia') 		#an application may be using Win32/UIA backend i just tried and chose uia 
		app.connect(title_re=".*Chrome.*")		#Chrome is what we are looking for
		element_name="Address and search bar"   #this is what you want to grab
		dlg = app.top_window()

		url = dlg.child_window(title=element_name, control_type="Edit").get_value() # get url from database
		
		if "youtube"  in url :
			val1 = time.perf_counter()
			
			time.sleep(2700)   #2700 is 45mins in seconds

			if (time.perf_counter() - val1 > 2700 ) and ("youtube" in dlg.child_window(title=element_name, control_type="Edit").get_value() ):
				os.system("taskkill /im chrome.exe /f") #simply kills the chrome if you are viewing chromes
	except Exception as e:
		# print(e)

		# time.sleep(100)
		pass

while True:
	kill_function()

