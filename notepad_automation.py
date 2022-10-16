# reading a data from file on notepad or console window

from pywinauto import application
import time
app=application.Application()
app.start("Notepad.exe")#open file
time.sleep(2)
app.Notepad.menu_select("File->open") #click open option
app.Open.Edit.set_edit_text("Bal.txt") #writting data
time.sleep(2)
app.Open.Open.click(double=True) #double click
print(app.Notepad.Edit.window_text())#printing data on consol window

#writing a data in notepad and save as test.txt and

# from pywinauto import application
# import time
# app=application.Application()
# app.start("Notepad.exe")#open file
# app.Edit.set_edit_text("Hi My Name Is Balkumar")
